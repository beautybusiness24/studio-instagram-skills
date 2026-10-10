#!/usr/bin/env python3
"""
beats.py - macht aus einem Reel-Skript einen Zeitplan, bevor du es aufnimmst.

Schätzt, wie lange jede Zeile gesprochen dauert, stapelt sie zu Zeitmarken
und meldet die vier Dinge, die ein Reel im Schnitt killen: ein Hook, der über
die Drei-Sekunden-Marke läuft, eine Stelle, die so lang ist, dass die
Zuschauerin geht, eine Folge von Zeilen ohne etwas Konkretes, und eine
Gesamtlänge, die nicht zu dem passt, was du vorhattest.

Die Zeiten sind eine Schätzung aus der Wortzahl bei einem Sprechtempo in
Wörtern pro Minute. Sie reichen, um den Schnitt zu planen, und ersetzen keine
Aufnahme. Dein eigenes Tempo setzt du mit --wpm, sobald du dich einmal beim
Vorlesen gestoppt hast: Die meisten liegen auf Deutsch zwischen 130 und 170,
Standard hier ist 150.

Deutsche Fassung des Originals aus dem instagram-agent-skill (MIT).

Aufruf
  python3 beats.py skript.txt
  python3 beats.py skript.txt --target 30
  python3 beats.py skript.txt --wpm 165 --target 45
  pbpaste | python3 beats.py -
  python3 beats.py skript.txt --json
"""

import argparse
import json
import re
import sys

WORD_RE = re.compile(r"[A-Za-zÄÖÜäöüß0-9€%'’-]+")
SENT_RE = re.compile(r"[^.!?]+[.!?]*")
CONCRETE_RE = re.compile(
    r"\d[\d.]*(?:,\d+)?\s?(?:€|euro)|\b\d[\d.,]*\b"
    r"|\b(?:zwei|drei|vier|fünf|sechs|sieben|acht|neun|zehn|zwölf|fünfzehn|zwanzig"
    r"|dreißig|vierzig|fünfzig|hundert|tausend|hälfte|doppelt)\b",
    re.IGNORECASE)
STOPWORDS = {
    "der", "die", "das", "den", "dem", "des", "ein", "eine", "einen", "einem",
    "einer", "und", "oder", "aber", "wenn", "von", "zu", "in", "im", "an", "am",
    "auf", "für", "mit", "dass", "es", "ist", "sind", "war", "waren", "sein",
    "du", "dir", "dich", "dein", "deine", "ich", "mir", "mich", "mein", "meine",
    "wir", "uns", "unser", "sie", "ihr", "euch", "er", "also", "einfach",
    "nicht", "nein", "kein", "keine", "mach", "macht", "hat", "habe", "haben",
    "wird", "kann", "bei", "aus", "nach", "vor", "so", "mal", "noch", "schon",
    "auch", "nur", "dann", "da", "wie", "was", "jetzt", "hier", "ja", "sich",
}

HOOK_WINDOW = 3.0        # Sekunden. Danach hat der Daumen schon entschieden.
MAX_BEAT = 4.0           # Sekunden auf einem Gedanken ohne Wechsel im Bild.
ABSTRACT_RUN = 3         # Zeilen hintereinander ohne etwas Nachprüfbares.


def words(text):
    # "4.000 €" ist gesprochen ein Wort, also auch hier.
    return WORD_RE.findall(re.sub(r"(?<=\d)\.(?=\d{3})", "", text))


def pretty(token):
    """Tausenderpunkt für die Anzeige zurücksetzen."""
    return re.sub(r"(\d)(?=(\d{3})+$)", r"\1.", token)


def tc(seconds):
    m, s = divmod(seconds, 60)
    return f"{int(m)}:{s:04.1f}"


def split_beats(raw, wps):
    """Eine Zeile ist ein Beat, außer sie ist zu lang für einen."""
    beats = []
    for line in [l.strip() for l in raw.splitlines()]:
        if not line:
            continue
        if len(words(line)) / wps <= MAX_BEAT * 1.5:
            beats.append(line)
            continue
        # Langer Absatz: an Satzenden trennen, damit die Zeiten etwas bedeuten.
        parts = [p.strip() for p in SENT_RE.findall(line) if p.strip()]
        buf = ""
        for part in parts:
            candidate = (buf + " " + part).strip()
            if buf and len(words(candidate)) / wps > MAX_BEAT:
                beats.append(buf)
                buf = part
            else:
                buf = candidate
        if buf:
            beats.append(buf)
    return beats


def analyse(raw, wpm=150, target=None):
    wps = wpm / 60.0
    beats = split_beats(raw, wps)
    if not beats:
        return None

    rows, clock = [], 0.0
    for i, text in enumerate(beats):
        n = len(words(text))
        dur = n / wps
        rows.append({
            "n": i + 1,
            "start": round(clock, 2),
            "dur": round(dur, 2),
            "words": n,
            "text": text,
            "concrete": len(CONCRETE_RE.findall(text)),
            "label": "",
            "flags": [],
        })
        clock += dur
    total = clock

    # Die Stellen markieren, um die ein Reel gebaut ist.
    for r in rows:
        if r["n"] == 1 or r["start"] + r["dur"] <= HOOK_WINDOW:
            r["label"] = "HOOK"
    rows[-1]["label"] = "CTA" if rows[-1]["label"] != "HOOK" else "HOOK/CTA"
    half = total / 2
    for r in rows:
        if not r["label"] and r["start"] <= half < r["start"] + r["dur"]:
            r["label"] = "MITTE"

    notes = []
    if rows[0]["dur"] > HOOK_WINDOW:
        rows[0]["flags"].append(f"Hook dauert {rows[0]['dur']:.1f} s, über der {HOOK_WINDOW:.0f}-s-Marke")
        notes.append(f"Zeile 1 braucht {rows[0]['dur']:.1f} s. Auf höchstens "
                     f"{int(HOOK_WINDOW * wps)} Wörter kürzen, sonst landet der Hook, "
                     "nachdem die Entscheidung schon gefallen ist.")
    if rows[0]["concrete"] == 0:
        notes.append("Zeile 1 hat keine Zahl, keinen Preis, keine Dauer. Hooks ohne etwas "
                     "Nachprüfbares werden weggescrollt.")

    for r in rows:
        if r["dur"] > MAX_BEAT:
            r["flags"].append(f"{r['dur']:.1f} s auf einem Beat")
    long_beats = [r["n"] for r in rows if r["dur"] > MAX_BEAT]
    if long_beats:
        notes.append(f"Zeile(n) {', '.join(map(str, long_beats))} laufen über {MAX_BEAT:.0f} s. "
                     "Entweder den Satz teilen oder mittendrin das Bild wechseln. "
                     "Ein stehendes Bild ist die Stelle, an der Leute gehen.")

    run, start = 0, None
    for r in rows:
        if r["concrete"] == 0:
            run += 1
            start = start if start is not None else r["n"]
            if run == ABSTRACT_RUN:
                notes.append(f"Zeilen {start} bis {r['n']} haben nichts Konkretes. "
                             "In eine davon gehört eine Zahl, ein Preis oder eine Dauer.")
        else:
            run, start = 0, None

    # Gibt die letzte Zeile zur ersten zurück?
    first = {w.lower() for w in words(rows[0]["text"]) if w.lower() not in STOPWORDS}
    last = {w.lower() for w in words(rows[-1]["text"]) if w.lower() not in STOPWORDS}
    loop = sorted(pretty(w) for w in first & last)
    if loop:
        notes.append(f"Schleife: Die letzte Zeile wiederholt „{', '.join(loop[:3])}“ aus dem Hook. "
                     "Zweite Ansichten sind kostenlose Reichweite.")
    else:
        notes.append("Keine Schleife. Die letzte Zeile teilt kein Wort mit dem Hook, das Video "
                     "endet flach. Ein Wort aus Zeile 1 am Ende ist die billigste Wiederholung, "
                     "die es gibt.")

    if target:
        delta = total - target
        if abs(delta) <= target * 0.1:
            notes.append(f"Länge passt ({total:.1f} s bei Ziel {target:g} s).")
        elif delta > 0:
            notes.append(f"{delta:.1f} s über dem Ziel. Etwa {int(delta * wps)} Wörter streichen.")
        else:
            notes.append(f"{-delta:.1f} s unter dem Ziel. Entweder {int(-delta * wps)} Wörter "
                         "ergänzen oder kurz drehen. Kurz ist meistens richtig.")

    return {
        "wpm": wpm, "target": target,
        "total_seconds": round(total, 2),
        "total_words": sum(r["words"] for r in rows),
        "beats": rows,
        "notes": notes,
    }


def render(a, out=sys.stdout):
    head = (f"ZEITPLAN  ·  {a['total_words']} Wörter  ·  ~{a['total_seconds']:.1f} s "
            f"bei {a['wpm']:g} Wörtern/Min" + (f"  ·  Ziel {a['target']:g} s" if a["target"] else ""))
    print("\n" + head, file=out)
    print("=" * max(len(head), 72), file=out)
    for r in a["beats"]:
        label = f"{r['label']:<8}" if r["label"] else " " * 8
        print(f"  {tc(r['start'])}  {r['dur']:4.1f}s  {label}{r['text']}", file=out)
        for f in r["flags"]:
            print(f"  {'':>6}  {'':>5}  {'':<8}^ {f}", file=out)
    print("-" * max(len(head), 72), file=out)
    for n in a["notes"]:
        print(f"  - {n}", file=out)
    print("", file=out)


def main():
    ap = argparse.ArgumentParser(description="Macht aus einem Reel-Skript einen Zeitplan.")
    ap.add_argument("input", nargs="?", default="-", help="Skript-Datei, oder - für stdin")
    ap.add_argument("--wpm", type=float, default=150, help="Sprechtempo in Wörtern/Min (Standard 150)")
    ap.add_argument("--target", type=float, help="Ziellänge in Sekunden")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    raw = sys.stdin.read() if args.input == "-" else open(args.input, encoding="utf-8").read()
    a = analyse(raw, wpm=args.wpm, target=args.target)
    if not a:
        print("leeres Skript", file=sys.stderr)
        sys.exit(2)
    if args.json:
        print(json.dumps(a, indent=2, ensure_ascii=False))
    else:
        render(a)
    sys.exit(0)


if __name__ == "__main__":
    main()
