#!/usr/bin/env python3
"""
humanize.py - entfernt den Maschinen-Fingerabdruck aus einem Entwurf.

Drei Durchgänge, in dieser Reihenfolge:

  1. UNSICHTBAR    löscht oder ersetzt Zeichen, die keine Tastatur erzeugt:
                   Zero-Width-Zeichen, Word Joiner, weiche Trennstriche, BOM,
                   Unicode-Tag-Zeichen, geschützte und schmale Leerzeichen.
                   Sie überleben Kopieren und Einfügen und sind das
                   mechanischste Merkmal in generiertem Text.
  2. TYPOGRAFIE    Gedankenstrich -> Komma oder Punkt, englische
                   Anführungszeichen -> gerade, Auslassungszeichen -> drei
                   Punkte, Aufzählungspunkt -> Bindestrich. Deutsche
                   Anführungszeichen („ “) bleiben stehen.
  3. WÖRTER        ersetzt die Floskeln aus slop.json durch schlichte Wörter,
                   behält die Groß-/Kleinschreibung und lässt Links in Ruhe.

Strukturelle Merkmale (Dreier-Aufzählung, „nicht nur X, sondern Y“,
Hashtag-Wände) werden GEMELDET, nie automatisch umgeschrieben. Die Form eines
Satzes zu ändern braucht Urteil, und das ist Aufgabe des Modells, nicht
eines Musters.

Deutsche Fassung des Originals aus dem instagram-agent-skill (MIT).

Aufruf
  python3 humanize.py entwurf.txt
  python3 humanize.py entwurf.txt --report
  pbpaste | python3 humanize.py - --report
  python3 humanize.py entwurf.txt --json
  python3 humanize.py entwurf.txt -o sauber.txt
"""

import argparse
import json
import os
import re
import sys
import unicodedata

HERE = os.path.dirname(os.path.abspath(__file__))
LEX = os.path.join(HERE, "slop.json")

URL_RE = re.compile(r"https?://\S+|www\.\S+|\S+@\S+\.\S+")
SENT_RE = re.compile(r"[^.!?\n]+[.!?]*")


def load_lexicon(path=LEX):
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def _cp(spec):
    """'U+200B' -> '\\u200b';  'U+E0000-U+E007F' -> (start, end)."""
    if "-" in spec:
        a, b = spec.split("-")
        return (int(a[2:], 16), int(b[2:], 16))
    return int(spec[2:], 16)


def protect_urls(text):
    """Links gegen Platzhalter tauschen, damit kein Durchgang in einen Link schreibt."""
    found = []

    def stash(m):
        found.append(m.group(0))
        return f"\x00URL{len(found) - 1}\x00"

    return URL_RE.sub(stash, text), found


def restore_urls(text, found):
    for i, url in enumerate(found):
        text = text.replace(f"\x00URL{i}\x00", url)
    return text


def pass_invisible(text, lex):
    """Unsichtbare Zeichen löschen oder zu Leerzeichen machen. Gibt (text, treffer) zurück."""
    hits = []
    for entry in lex["invisible"]:
        cp = _cp(entry["cp"])
        if isinstance(cp, tuple):
            pattern = "[" + re.escape(chr(cp[0])) + "-" + re.escape(chr(cp[1])) + "]"
        else:
            pattern = re.escape(chr(cp))
        n = len(re.findall(pattern, text))
        if n:
            hits.append({"name": entry["cp"] + " " + entry["name"], "count": n,
                         "action": entry["action"]})
            text = re.sub(pattern, "" if entry["action"] == "delete" else " ", text)
    # Jedes übrige Cf-Zeichen (Format) ist per Definition unsichtbar.
    stray = [c for c in text if unicodedata.category(c) == "Cf"]
    if stray:
        hits.append({"name": "weitere unsichtbare Formatzeichen", "count": len(stray),
                     "action": "delete"})
        text = "".join(c for c in text if unicodedata.category(c) != "Cf")
    return text, hits


def pass_typographic(text, lex):
    hits = []
    for entry in lex["typographic"]:
        ch = entry["from"]
        n = text.count(ch)
        if not n:
            continue
        hits.append({"name": f"{ch} {entry['name']}", "count": n, "to": entry["to"].strip() or "(Leerzeichen)"})
        if ch == "—":
            # " Wort — Wort " und "Wort—Wort" werden beide zu Komma plus Leerzeichen.
            text = re.sub(r"\s*—\s*", ", ", text)
        elif ch == "–":
            text = re.sub(r"(?<=\d)\s*–\s*(?=\d)", "-", text)      # 5 – 10  -> 5-10
            text = re.sub(r"\s+–\s+", ", ", text)                   # als Gedankenstrich
            text = text.replace("–", "-")
        else:
            text = text.replace(ch, entry["to"])
    # Ein Komma vor vorhandener Interpunktion liest sich falsch.
    text = re.sub(r",\s*([,.;:!?])", r"\1", text)
    text = re.sub(r",\s*\n", "\n", text)
    return text, hits


def _match_case(src, repl):
    if not repl:
        return repl
    if src.isupper() and len(src) > 1:
        return repl.upper()
    if src[0].isupper():
        return repl[0].upper() + repl[1:]
    return repl


def _sentence_span(text, pos):
    """Anfang und Ende des Satzes, in dem Position pos liegt."""
    start = max(text.rfind(c, 0, pos) for c in ".!?\n") + 1
    ends = [text.find(c, pos) for c in ".!?\n"]
    ends = [e for e in ends if e != -1]
    end = min(ends) + 1 if ends else len(text)
    return start, end


def pass_lexical(text, lex):
    """Floskel-Wörter und -Wendungen ersetzen. Längste zuerst, damit Wendungen gewinnen.

    Eine Wendung ohne Ersatz wird nur gelöscht, wenn sie (fast) den ganzen Satz
    ausmacht; dann fällt der Satz. Steckt sie mitten in einem Satz, bleibt der
    Satz stehen und die Stelle wird zum Umschreiben gemeldet, weil ein
    halbierter Satz schlimmer liest als die Floskel.
    """
    hits = []
    flagged = []
    entries = sorted(lex["phrases"] + lex["words"],
                     key=lambda e: len(e["find"]), reverse=True)
    for entry in entries:
        find = entry["find"]
        pattern = re.compile(r"(?<![\wÄÖÜäöüß])" + re.escape(find).replace(r"\ ", r"\s+") + r"(?![\wÄÖÜäöüß])",
                             re.IGNORECASE)
        found = list(pattern.finditer(text))
        if not found:
            continue
        repl = entry["replace"]
        if repl or len(find.split()) == 1:
            hits.append({"find": find, "replace": repl or "(gelöscht)",
                         "count": len(found), "family": entry["family"]})
            text = pattern.sub(lambda m: _match_case(m.group(0), repl), text)
            continue
        # Mehrwort-Wendung ohne Ersatz: Satz prüfen, von hinten nach vorn ersetzen.
        removed, kept = 0, 0
        for m in reversed(found):
            s, e = _sentence_span(text, m.start())
            sent = text[s:e]
            share = (m.end() - m.start()) / max(len(sent.strip()), 1)
            if share >= 0.6:
                text = text[:s] + text[e:]
                removed += 1
            else:
                kept += 1
                flagged.append({"name": f"Floskel im Satz: „{find}“", "count": 1,
                                "fix": f"Den Satz „{sent.strip()[:70]}“ ohne diese Wendung neu schreiben."})
        if removed:
            hits.append({"find": find, "replace": "(Satz gelöscht)", "count": removed,
                         "family": entry["family"]})
    text = re.sub(r"(?m)^[ \t]+", "", text)
    # Aufräumen nach Löschungen. Ein gelöschter Satzteil lässt verwaiste
    # Satzzeichen zurück, und das liest sich schlechter als die Floskel.
    text = re.sub(r"[ \t]{2,}", " ", text)
    text = re.sub(r"(?m)^[ \t]*(?:[,.;:]+[ \t]*)+", "", text)
    text = re.sub(r"(?m)^[ \t](?=\S)", "", text)       # ein Leerzeichen von einer Löschung.
                                                      # Tiefere Einzüge sind Absicht.
    text = re.sub(r"\s+([,.;:!?])", r"\1", text)
    text = re.sub(r",\s*([,.;:!?])", r"\1", text)      # ein Gedankenstrich wurde Komma,
                                                      # dann ging der Satzteil dahinter
    text = text.replace("...", "\x00ELL\x00")          # echte Auslassungen schützen
    text = re.sub(r"\.\s*\.+", ".", text)
    text = re.sub(r"([!?])\s*\.", r"\1", text)
    text = text.replace("\x00ELL\x00", "...")
    text = re.sub(r"(?m)^[ \t]+$", "", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    # Ein Gedankenstrich, der zum Komma wurde, gefolgt von einem Verbindungswort,
    # hinterlässt einen Schnitzer („ist wichtig, außerdem, es beweist“). Zum Punkt machen.
    text = re.sub(r",\s*(außerdem|also|trotzdem|im grunde|am ende|denn|aber)\s*,\s*",
                  lambda m: ". " + m.group(1)[0].upper() + m.group(1)[1:] + ", ", text)
    return text, hits, flagged


def scan_structures(text, lex):
    flags = []
    for s in lex["structures"]:
        try:
            pattern = re.compile(s["regex"], re.MULTILINE)
        except re.error:
            continue
        found = pattern.findall(text)
        if found:
            flags.append({"name": s["name"], "count": len(found), "fix": s["fix"]})
    # Gleichmäßige Satzlänge ist auch ein Strukturmerkmal.
    lens = [len(s.split()) for s in SENT_RE.findall(text) if len(s.split()) > 2]
    if len(lens) >= 4:
        mean = sum(lens) / len(lens)
        var = sum((n - mean) ** 2 for n in lens) / len(lens)
        cv = (var ** 0.5) / mean if mean else 0
        if cv < 0.35:
            flags.append({
                "name": f"Gleichmäßige Satzlänge (Streuung {cv:.2f})",
                "count": len(lens),
                "fix": "Einen Satz halbieren. Einen anderen lang laufen lassen. Maschinen schreiben gleichmäßig.",
            })
    return flags


def restore_capitals(original, text):
    """Eine gelöschte Einleitung lässt das nächste Wort klein zurück.

    Nur für Texte korrigieren, die ihre Sätze ohnehin groß beginnen: Eine
    bewusst kleingeschriebene Stimme ist ein Stil, kein Artefakt.
    """
    starts = re.findall(r"(?:^|[.!?]\s+|\n)\s*([A-Za-zÄÖÜäöü])", original)
    if not starts or sum(1 for c in starts if c.isupper()) * 2 < len(starts):
        return text
    return re.sub(r"(?:^|(?<=[.!?] )|(?<=[.!?]\n)|(?<=\n))\s*([a-zäöü])",
                  lambda m: m.group(0)[:-1] + m.group(1).upper(), text)


def humanize(text, lex):
    raw_for_case = text
    text, urls = protect_urls(text)
    text, inv = pass_invisible(text, lex)
    text, typo = pass_typographic(text, lex)
    text, lexi, flagged = pass_lexical(text, lex)
    text = restore_capitals(raw_for_case, text)
    text = restore_urls(text, urls)
    return text.strip() + "\n", {
        "invisible": inv,
        "typographic": typo,
        "lexical": lexi,
        "structures": scan_structures(text, lex) + flagged,
    }


def render_report(report, out=sys.stderr):
    def head(title):
        print(f"\n{title}\n" + "-" * len(title), file=out)

    total = sum(h["count"] for h in report["invisible"]) \
        + sum(h["count"] for h in report["typographic"]) \
        + sum(h["count"] for h in report["lexical"])

    head("HUMANIZER-BERICHT")
    print(f"{total} Maschinen-Artefakte entfernt, "
          f"{len(report['structures'])} Strukturmerkmal(e) zum Umschreiben gemeldet", file=out)

    if report["invisible"]:
        head("1. UNSICHTBARE ZEICHEN")
        for h in report["invisible"]:
            print(f"  {h['count']:>3}x  {h['name']}  -> {h['action']}", file=out)
    if report["typographic"]:
        head("2. TYPOGRAFIE")
        for h in report["typographic"]:
            print(f"  {h['count']:>3}x  {h['name']}  -> {h['to']}", file=out)
    if report["lexical"]:
        head("3. FLOSKELN")
        for h in report["lexical"]:
            print(f"  {h['count']:>3}x  {h['find']}  -> {h['replace']}   [{h['family']}]", file=out)
    if report["structures"]:
        head("4. STRUKTURMERKMALE  (nicht automatisch behoben, selbst umschreiben)")
        for h in report["structures"]:
            print(f"  {h['count']:>3}x  {h['name']}\n        {h['fix']}", file=out)
    if not any(report.values()):
        head("SAUBER")
        print("  Nichts zu entfernen.", file=out)
    print("", file=out)


def main():
    ap = argparse.ArgumentParser(description="Entfernt den Maschinen-Fingerabdruck aus einem Entwurf.")
    ap.add_argument("input", nargs="?", default="-", help="Datei, oder - für stdin")
    ap.add_argument("-o", "--out", help="bereinigten Text hierhin schreiben statt nach stdout")
    ap.add_argument("--report", action="store_true", help="Änderungen auf stderr ausgeben")
    ap.add_argument("--json", action="store_true", help="{text, report} als JSON ausgeben")
    ap.add_argument("--lexicon", default=LEX, help="Pfad zu slop.json")
    args = ap.parse_args()

    raw = sys.stdin.read() if args.input == "-" else open(args.input, encoding="utf-8").read()
    lex = load_lexicon(args.lexicon)
    clean, report = humanize(raw, lex)

    if args.json:
        print(json.dumps({"text": clean, "report": report}, indent=2, ensure_ascii=False))
        return
    if args.out:
        with open(args.out, "w", encoding="utf-8") as fh:
            fh.write(clean)
        print(f"geschrieben: {args.out}", file=sys.stderr)
    else:
        sys.stdout.write(clean)
    if args.report:
        render_report(report)


if __name__ == "__main__":
    main()
