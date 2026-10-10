#!/usr/bin/env python3
"""
caption.py - prüft eine Instagram-Caption und zeigt genau das, was der Feed
vor dem „... mehr“ anzeigt.

Instagram zeigt im Feed etwa 125 Zeichen einer Caption und versteckt den Rest
hinter einem Tipp. Fast jede Caption, die nicht funktioniert, scheitert
genau dort: Der wichtige Satz steht in Zeile drei, die erste Zeile ist eine
Begrüßung, oder das Ganze fängt mit einem Hashtag an. Dieses Skript zeigt das
sichtbare Fenster als Kasten, damit du es so liest wie jemand, der vorbeiscrollt,
und prüft danach die Dinge, die sich zu prüfen lohnen.

Die 125 Zeichen sind eine Näherung. Der echte Wert hängt vom Gerät, von der
Schriftgröße und von den Zeilenumbrüchen ab, deshalb lieber Luft lassen als
eine Caption auf genau 125 bauen. Mit --truncate lässt sich ein engerer Wert
testen.

Deutsche Fassung des Originals aus dem instagram-agent-skill (MIT).

Aufruf
  python3 caption.py caption.txt
  python3 caption.py caption.txt --keywords "dauerhafte haarentfernung berlin,laser achseln"
  pbpaste | python3 caption.py -
  python3 caption.py caption.txt --json
"""

import argparse
import json
import re
import sys
import textwrap

LIMIT = 2200             # Hartes Limit von Instagram.
TRUNCATE = 125           # Ungefähr die Stelle, an der der Feed zu „... mehr“ kürzt.
HASHTAG_LIMIT = 5        # Obergrenze von Instagram je Beitrag seit 18. Dezember 2025,
                         # vorher 30. Begründung von Instagram: wenige, passende
                         # Hashtags statt vieler allgemeiner.

HASHTAG_RE = re.compile(r"(?:^|\s)(#[A-Za-zÄÖÜäöüß0-9_]+)")
MENTION_RE = re.compile(r"(?:^|\s)(@[A-Za-z0-9_.]+)")
LINK_RE = re.compile(r"https?://\S+|\bwww\.\S+|\b[a-z0-9-]+\.(?:com|de|at|ch|co|io|net|org|ai|app|shop)/\S*",
                     re.IGNORECASE)
EMOJI_RE = re.compile(r"[\U0001F300-\U0001FAFF☀-➿←-⇿️]")
CONCRETE_RE = re.compile(r"\d[\d.]*(?:,\d+)?\s?(?:€|euro)|\b\d[\d.,]*\b", re.IGNORECASE)

ASKS = [
    (re.compile(r"\b(?:[Kk]ommentier\w*|[Ss]chreib\w*|[Tt]ipp\w*)\s+(?:das [Ww]ort |einfach |nur |mir |uns )?[„\"']?[A-ZÄÖÜ0-9]{2,}[\"“']?(?=[\s.,!?]|$)"), "ein Stichwort kommentieren"),
    (re.compile(r"\b[A-ZÄÖÜ]{3,}\s+(?:in die|unter|als|in den) (?:[Kk]ommentar|[Kk]ommentare|[Kk]ommis)\b"), "ein Stichwort kommentieren"),
    (re.compile(r"(?i)\b(?:schreib|schreibt|schick|schickt)\s+(?:mir|uns)\s+(?:eine |'ne |ne )?(?:dm|nachricht|pn)\b|\bper (?:dm|nachricht|pn)\b"), "DM schreiben"),
    (re.compile(r"(?i)\b(?:speicher|speichert|merk|merkt)\s+(?:dir|euch|es|das|ihn|sie)\b|\bzum (?:speichern|abspeichern|merken)\b"), "speichern"),
    (re.compile(r"(?i)\b(?:teil|teilt|schick|schickt)\s+(?:das|es|den beitrag|das reel)\b[^.!?]{0,30}\b(?:an|mit|deiner|deinem|einer)\b"), "teilen"),
    (re.compile(r"(?i)\bfolg(?:e|t)\s+(?:mir|uns|für|@)\b"), "folgen"),
    (re.compile(r"(?i)\blink in (?:der |meiner |unserer )?bio\b"), "Link in der Bio"),
    (re.compile(r"(?i)\b(?:wisch|wischt|swipe|tipp|tippt)\s+(?:nach|weiter|durch|rüber|auf)\b"), "wischen oder tippen"),
    (re.compile(r"(?i)\b(?:erzähl|erzählt|verrat|verratet|sag|sagt) (?:mir|uns)\b|\bwelche[rsn]? (?:von|davon)\b|\bwas (?:würdest du|würdet ihr|meinst du|meint ihr)\b"), "eine Frage beantworten"),
    (re.compile(r"(?i)\b(?:termin|probetermin|beratung|beratungstermin|erstgespräch)\b[^.!?]{0,40}\b(?:buchen|sichern|vereinbaren|anfragen|ausmachen)\b|\b(?:buch|bucht|sicher|sichert) (?:dir|euch)\b"), "Termin buchen"),
]

FILLER_TAGS = {"#viral", "#fyp", "#explore", "#explorepage", "#foryou", "#foryoupage",
               "#trending", "#instagood", "#love", "#follow", "#like4like", "#reels",
               "#reelsinstagram", "#viralreels", "#instadaily", "#beauty", "#beautiful",
               "#schönheit", "#selfcare", "#instabeauty", "#picoftheday", "#likeforlike",
               "#followme", "#happy", "#photooftheday"}


def visible_window(text, cut):
    """Was der Feed zeigt. Instagram kürzt mitten im Wort, also hier auch."""
    flat = text.strip()
    return flat if len(flat) <= cut else flat[:cut]


def render_box(window, truncated, out=sys.stdout, width=52):
    print("\n  SO ZEIGT ES DER FEED", file=out)
    print("  +" + "-" * (width + 2) + "+", file=out)
    lines = []
    for raw in window.split("\n"):
        lines.extend(textwrap.wrap(raw, width) or [""])
    for line in lines[:8]:
        print(f"  | {line:<{width}} |", file=out)
    tail = "... mehr" if truncated else "(ganze Caption passt)"
    print("  +" + "-" * (width + 2 - len(tail) - 2) + f" {tail} " + "+", file=out)


def analyse(text, cut=TRUNCATE, keywords=None):
    text = text.rstrip()
    stripped = text.strip()
    chars = len(stripped)
    lines = [l for l in stripped.split("\n")]
    first_line = lines[0].strip() if lines else ""
    tags = HASHTAG_RE.findall(stripped)
    mentions = MENTION_RE.findall(stripped)
    links = LINK_RE.findall(stripped)
    emoji = EMOJI_RE.findall(stripped)
    window = visible_window(stripped, cut)
    truncated = chars > cut
    asks = []
    for pattern, name in ASKS:
        if pattern.search(stripped) and name not in asks:
            asks.append(name)
    filler = [t for t in tags if t.lower() in FILLER_TAGS]
    keywords = [k.strip() for k in (keywords or []) if k.strip()]

    checks = []

    def add(name, status, detail):
        checks.append({"check": name, "status": status, "detail": detail})

    add("LÄNGE", "FEHLER" if chars > LIMIT else "OK",
        f"{chars} / {LIMIT} Zeichen" + (f", {chars - LIMIT} über dem Limit"
                                        if chars > LIMIT else ""))

    if not first_line:
        add("ERSTE ZEILE", "FEHLER", "die Caption beginnt mit einer Leerzeile")
    elif first_line.startswith("#") or first_line.startswith("@"):
        add("ERSTE ZEILE", "FEHLER",
            "beginnt mit Hashtag oder Erwähnung, an der einen Stelle, die einen Satz verdient")
    elif len(first_line) > cut:
        add("ERSTE ZEILE", "PRÜFEN",
            f"{len(first_line)} Zeichen, wird bei {cut} mitten im Gedanken gekürzt. "
            "In Ordnung, wenn die Kürzung ein Cliffhanger ist, schlecht, wenn sie in einem Nebensatz landet")
    else:
        add("ERSTE ZEILE", "OK", f"{len(first_line)} Zeichen, kommt ganz an")

    add("KONKRET", "OK" if CONCRETE_RE.search(window) else "PRÜFEN",
        f"{len(CONCRETE_RE.findall(window))} Zahl(en) im sichtbaren Fenster"
        + ("" if CONCRETE_RE.search(window) else ", vor dem Tipp steht nichts Nachprüfbares"))

    if len(tags) > HASHTAG_LIMIT:
        add("HASHTAGS", "FEHLER", f"{len(tags)} Hashtags, über der Grenze von {HASHTAG_LIMIT}. "
                                  "Alles ab dem sechsten zählt nicht, und der Block wirkt alt")
    elif len(tags) == HASHTAG_LIMIT and filler:
        add("HASHTAGS", "PRÜFEN", f"{len(tags)} Hashtags, an der Grenze, und "
                                  f"{len(filler)} davon allgemein. Die fünf für Themen ausgeben")
    elif filler:
        add("HASHTAGS", "PRÜFEN", f"{len(tags)} Hashtags, {len(filler)} davon allgemein "
                                  f"({', '.join(filler[:3])}). Die beschreiben nichts")
    else:
        add("HASHTAGS", "OK", f"{len(tags)} Hashtag(s)" + (f": {' '.join(tags)}" if tags else ""))

    if not tags:
        add("HASHTAG-PLATZ", "OK", "keine Hashtags zu platzieren")
    elif any(re.search(r"(?:^|\s)" + re.escape(t) + r"\b", window) for t in tags):
        add("HASHTAG-PLATZ", "PRÜFEN", "ein Hashtag steht im sichtbaren Fenster und "
                                       "verbraucht Platz, der einem Satz gehört")
    else:
        add("HASHTAG-PLATZ", "OK", "Hashtags stehen unterhalb der Kürzung")

    add("LINKS", "PRÜFEN" if links else "OK",
        f"{len(links)} Link(s) in der Caption, und Captions sind nicht klickbar. "
        f"In die Bio oder in die DM" if links else "keine toten Links im Text")

    if len(asks) == 1:
        add("EINE AUFFORDERUNG", "OK", f"eine Aufforderung: {asks[0]}")
    elif not asks:
        add("EINE AUFFORDERUNG", "PRÜFEN", "keine Aufforderung. Entscheiden, wofür dieser Beitrag da ist")
    else:
        add("EINE AUFFORDERUNG", "PRÜFEN", f"{len(asks)} Aufforderungen ({', '.join(asks)}). "
                                           "Zwei Aufforderungen wirken wie keine")

    density = len(emoji) * 100 / max(chars, 1)
    add("EMOJI", "PRÜFEN" if density > 4 else "OK",
        f"{len(emoji)} Emoji, {density:.1f} je 100 Zeichen"
        + (", wirkt wie Dekoration" if density > 4 else ""))

    if keywords:
        low = stripped.lower()

        def present(k, where):
            # Wortgenau, oder alle Wörter des Begriffs kommen vor (deutsche
            # Flexion: "Haarentfernung in Berlin" deckt "haarentfernung berlin").
            k = k.lower()
            if k in where:
                return "genau"
            parts = [p for p in re.split(r"\s+", k) if p]
            if parts and all(re.search(r"\b" + re.escape(p), where) for p in parts):
                return "als Wörter"
            return None

        found = [k for k in keywords if present(k, low)]
        exact = [k for k in found if present(k, low) == "genau"]
        missing = [k for k in keywords if not present(k, low)]
        in_window = [k for k in found if present(k, window.lower())]
        status = "OK" if not missing else ("PRÜFEN" if found else "FEHLER")
        add("SUCHBEGRIFFE", status,
            f"{len(found)}/{len(keywords)} vorhanden"
            + (f" ({len(exact)} wortgenau)" if found and len(exact) < len(found) else "")
            + (f", {len(in_window)} im sichtbaren Fenster" if found else "")
            + (f". Fehlt: {', '.join(missing)}" if missing else ""))

    fails = sum(1 for c in checks if c["status"] == "FEHLER")
    warns = sum(1 for c in checks if c["status"] == "PRÜFEN")
    verdict = "NACHBESSERN" if fails else ("DURCHSEHEN" if warns else "FERTIG")

    return {
        "characters": chars, "limit": LIMIT, "truncate_at": cut,
        "visible": window, "truncated": truncated,
        "first_line_chars": len(first_line),
        "hashtags": tags, "mentions": mentions, "links": links,
        "emoji": len(emoji), "asks": asks,
        "checks": checks, "verdict": verdict,
    }


def render(a, out=sys.stdout):
    head = (f"CAPTION-PRÜFUNG  ·  {a['characters']} / {a['limit']} Zeichen  ·  "
            f"{len(a['hashtags'])} Hashtags  ·  {len(a['asks'])} Aufforderung(en)")
    print("\n" + head, file=out)
    print("=" * max(len(head), 62), file=out)
    render_box(a["visible"], a["truncated"], out=out)
    print("", file=out)
    for c in a["checks"]:
        print(f"  {c['status']:<7} {c['check']:<18} {c['detail']}", file=out)
    print("-" * max(len(head), 62), file=out)
    print(f"  ERGEBNIS  {a['verdict']}\n", file=out)


def main():
    ap = argparse.ArgumentParser(description="Prüft eine Instagram-Caption.")
    ap.add_argument("input", nargs="?", default="-", help="Caption-Datei, oder - für stdin")
    ap.add_argument("--truncate", type=int, default=TRUNCATE,
                    help=f"Zeichen vor „... mehr“ (Standard {TRUNCATE})")
    ap.add_argument("--keywords", default="", help="Suchbegriffe, kommagetrennt, für die du gefunden werden willst")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    raw = sys.stdin.read() if args.input == "-" else open(args.input, encoding="utf-8").read()
    a = analyse(raw, cut=args.truncate, keywords=args.keywords.split(","))
    if args.json:
        print(json.dumps(a, indent=2, ensure_ascii=False))
    else:
        render(a)
    sys.exit(0 if a["verdict"] == "FERTIG" else 1)


if __name__ == "__main__":
    main()
