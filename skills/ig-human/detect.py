#!/usr/bin/env python3
"""
detect.py - fünf Prüfungen, die messen, wie sehr ein Entwurf nach Maschine klingt.

Was das ist:  fünf lokale Prüfungen, angelehnt an die Signale, die öffentliche
KI-Detektoren tatsächlich messen: Streuung der Satzlänge, Konkretheit,
Floskeldichte, typografischer Fingerabdruck und Stimme. Alles wird auf deinem
Rechner aus dem Text berechnet. Nichts wird hochgeladen.

Was das NICHT ist:  GPTZero, Originality, Copyleaks oder Turnitin. Es ruft
deren Schnittstellen nicht auf und kann deren Urteil nicht versprechen. Es
erkennt die Dinge, auf die alle achten, weshalb ihre Werte sich meistens
mitbewegen, wenn man diese behebt. Mehr lässt sich ehrlich nicht behaupten.

Jede Prüfung gibt einen MENSCH-Wert von 0 bis 100. Höher ist besser.

Deutsche Fassung des Originals aus dem instagram-agent-skill (MIT). Im
Deutschen werden alle Substantive großgeschrieben, deshalb zählen hier nur
Zahlen, Preise und Zeitangaben als konkret, keine Großschreibung. Statt
englischer Kurzformen (don't, it's) zählen umgangssprachliche Marker
(hab, gibt's, mal, halt, echt).

Aufruf
  python3 detect.py entwurf.txt
  pbpaste | python3 detect.py -
  python3 detect.py entwurf.txt --json
  python3 detect.py vorher.txt nachher.txt      # zwei Fassungen vergleichen
"""

import argparse
import json
import os
import re
import statistics
import sys
import unicodedata

HERE = os.path.dirname(os.path.abspath(__file__))
LEX = os.path.join(HERE, "slop.json")

SENT_RE = re.compile(r"[^.!?\n]+[.!?]*")
WORD_RE = re.compile(r"[A-Za-zÄÖÜäöüß']+")
COLLOQUIAL = re.compile(
    r"\b(?:hab|habs|hab's|gibt's|gibts|geht's|gehts|ist's|'ne|'nen|'n|nen|ne|mal|halt|eh|echt|"
    r"eigentlich|irgendwie|ziemlich|okay|naja|tja|klar|krass|ehrlich|so was|sowas|bisschen|"
    r"bissl|kriegst|kriegt|kriege|guck|schau)\b", re.IGNORECASE)
PRONOUNS = re.compile(
    r"\b(ich|mir|mich|mein|meine|meinen|wir|uns|unser|unsere|du|dir|dich|dein|deine|deinen|ihr|euch|euer|eure)\b",
    re.IGNORECASE)
NUMBERS = re.compile(
    r"\d[\d.]*(?:,\d+)?\s?(?:€|euro|%|prozent|min\b|minuten|std\b|stunden|tage?|wochen?|monate?|jahre?n?|sitzungen?|cm|mm|kg)?"
    r"|\b(?:zwei|drei|vier|fünf|sechs|sieben|acht|neun|zehn|zwölf|fünfzehn|zwanzig|dreißig|fünfzig|hundert|tausend)\b",
    re.IGNORECASE)


def clamp(n):
    return max(0.0, min(100.0, n))


def scale(value, human, machine):
    """Wert auf 0-100 abbilden, wobei `human` -> 100 und `machine` -> 0."""
    if human == machine:
        return 50.0
    return clamp((value - machine) / (human - machine) * 100)


def sentences(text):
    return [s.strip() for s in SENT_RE.findall(text) if len(s.split()) > 2]


def words(text):
    return WORD_RE.findall(text)


def check_burstiness(text):
    """Menschen variieren die Satzlänge stark. Modelle schreiben gleichmäßig."""
    lens = [len(s.split()) for s in sentences(text)]
    if len(lens) < 4:
        return 50.0, "zu kurz für ein Urteil"
    mean = statistics.mean(lens)
    cv = statistics.pstdev(lens) / mean if mean else 0
    score = scale(cv, human=0.65, machine=0.20)
    return score, f"Streuung {cv:.2f} über {len(lens)} Sätze (Ziel 0,55 und mehr)"


def check_specificity(text):
    """Zahlen, Preise, Zeiten. Floskeln sind abstrakt."""
    w = words(text)
    if len(w) < 25:
        return 50.0, "zu kurz für ein Urteil"
    per100 = 100 / len(w)
    hits = len([m for m in NUMBERS.findall(text) if m.strip()])
    density = hits * per100
    score = scale(density, human=3.5, machine=0.3)
    return score, f"{hits} konkrete Angaben, {density:.1f} je 100 Wörter (Ziel 2,5 und mehr)"


def check_slop(text, lex):
    """Floskeldichte gegen die Liste."""
    w = words(text)
    if not w:
        return 50.0, "leer"
    hits, found = 0, []
    for entry in lex["words"] + lex["phrases"]:
        pattern = re.compile(r"(?<![\wÄÖÜäöüß])" + re.escape(entry["find"]).replace(r"\ ", r"\s+") + r"(?![\wÄÖÜäöüß])",
                             re.IGNORECASE)
        n = len(pattern.findall(text))
        if n:
            hits += n
            found.append(entry["find"])
    density = hits * 100 / len(w)
    score = scale(density, human=0.0, machine=4.0)
    detail = f"{hits} Floskeln, {density:.1f} je 100 Wörter"
    if found:
        detail += " (" + ", ".join(sorted(found)[:4]) + (", ..." if len(found) > 4 else "") + ")"
    return score, detail


def check_fingerprint(text):
    """Zeichen, die eine Handy-Tastatur nicht erzeugt."""
    invisible = sum(1 for c in text if unicodedata.category(c) == "Cf")
    em = text.count("—")
    en = len(re.findall(r"\s–\s", text))
    curly = sum(text.count(c) for c in "‘’“”")
    ellip = text.count("…")
    nbsp = sum(text.count(c) for c in "\u00a0\u202f\u2009")
    total = invisible * 4 + em * 2 + en * 2 + curly + ellip + nbsp
    per1k = total * 1000 / max(len(text), 1)
    score = scale(per1k, human=0.0, machine=12.0)
    detail = (f"{invisible} unsichtbar, {em + en} Gedankenstrich(e), {curly} englische Anführungszeichen, "
              f"{ellip} Auslassungszeichen, {nbsp} geschützte Leerzeichen")
    return score, detail


def check_voice(text, lex):
    """Umgangssprache, Ansprache und die Formen, zu denen Modelle neigen."""
    w = words(text)
    if len(w) < 25:
        return 50.0, "zu kurz für ein Urteil"
    per100 = 100 / len(w)
    colloquial = len(COLLOQUIAL.findall(text)) * per100
    person = len(PRONOUNS.findall(text)) * per100
    tells = 0
    names = []
    for s in lex["structures"]:
        try:
            n = len(re.compile(s["regex"], re.MULTILINE).findall(text))
        except re.error:
            continue
        if n:
            tells += n
            names.append(s["id"])
    bullets = [len(b.split()) for b in re.findall(r"(?m)^\s*[-*•]\s+(.+)$", text)]
    uniform = (len(bullets) >= 3 and statistics.pstdev(bullets) < 1.6)
    score = (scale(colloquial, human=2.5, machine=0.0) * 0.30
             + scale(person, human=8.0, machine=1.0) * 0.40
             + clamp(100 - tells * 22) * 0.30)
    if uniform:
        score -= 12
        names.append("gleichförmige-aufzählung")
    detail = (f"{colloquial:.1f} Umgangssprache, {person:.1f} persönliche Anrede "
              f"je 100 Wörter, {tells} Strukturmerkmal(e)")
    if names:
        detail += " [" + ", ".join(names[:4]) + "]"
    return clamp(score), detail


CHECKS = ["STREUUNG", "KONKRET", "FLOSKELN", "FINGERABDRUCK", "STIMME"]


def run(text, lex):
    results = {}
    results["STREUUNG"] = check_burstiness(text)
    results["KONKRET"] = check_specificity(text)
    results["FLOSKELN"] = check_slop(text, lex)
    results["FINGERABDRUCK"] = check_fingerprint(text)
    results["STIMME"] = check_voice(text, lex)
    scores = [results[c][0] for c in CHECKS]
    # Die schwächste Prüfung zieht das Urteil: Ein Detektor braucht nur ein Signal.
    overall = statistics.mean(scores) * 0.6 + min(scores) * 0.4
    verdict = "BESTANDEN" if overall >= 70 and min(scores) >= 55 else (
        "DURCHSEHEN" if overall >= 50 else "AUFFÄLLIG")
    return results, overall, verdict


def bar(score, width=24):
    filled = round(score / 100 * width)
    return "#" * filled + "." * (width - filled)


def render(results, overall, verdict, label=None, out=sys.stdout):
    title = "KI-PRÜFUNG" + (f"  -  {label}" if label else "")
    print("\n" + title, file=out)
    print("=" * max(len(title), 62), file=out)
    for name in CHECKS:
        score, detail = results[name]
        print(f"  {name:<14} {bar(score)} {score:5.1f}", file=out)
        print(f"  {'':<14} {detail}", file=out)
    print("-" * 62, file=out)
    print(f"  {'MENSCH-WERT':<14} {bar(overall)} {overall:5.1f}   {verdict}", file=out)
    if verdict != "BESTANDEN":
        weakest = min(CHECKS, key=lambda c: results[c][0])
        print(f"\n  Schwächstes Signal: {weakest}. Das zuerst beheben.", file=out)
    print("", file=out)


def main():
    ap = argparse.ArgumentParser(description="Misst, wie sehr ein Entwurf nach Maschine klingt.")
    ap.add_argument("input", nargs="?", default="-", help="Datei, oder - für stdin")
    ap.add_argument("compare", nargs="?", help="zweite Datei für Vorher/Nachher")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--lexicon", default=LEX)
    args = ap.parse_args()

    lex = json.load(open(args.lexicon, encoding="utf-8"))
    read = lambda p: sys.stdin.read() if p == "-" else open(p, encoding="utf-8").read()

    targets = [(args.input, read(args.input))]
    if args.compare:
        targets.append((args.compare, read(args.compare)))

    payload = []
    for name, text in targets:
        results, overall, verdict = run(text, lex)
        payload.append({
            "source": name,
            "checks": {k: {"score": round(v[0], 1), "detail": v[1]} for k, v in results.items()},
            "human_score": round(overall, 1),
            "verdict": verdict,
        })

    if args.json:
        print(json.dumps(payload if args.compare else payload[0], indent=2, ensure_ascii=False))
        return

    for (name, text), p in zip(targets, payload):
        results, overall, verdict = run(text, lex)
        render(results, overall, verdict, label=os.path.basename(name) if args.compare else None)
    if args.compare:
        a, b = payload
        delta = b["human_score"] - a["human_score"]
        print(f"  {a['human_score']:.1f} {a['verdict']}  ->  "
              f"{b['human_score']:.1f} {b['verdict']}   ({delta:+.1f})\n")

    sys.exit(0 if payload[-1]["verdict"] == "BESTANDEN" else 1)


if __name__ == "__main__":
    main()
