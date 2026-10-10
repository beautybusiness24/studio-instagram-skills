#!/usr/bin/env python3
"""
hookscore.py - bewertet die erste Zeile eines Reels nach fünf Eigenschaften,
die starke Hooks gemeinsam haben, und ordnet mehrere Hooks gegeneinander.

Was das ist:  fünf lokale Prüfungen, berechnet auf deinem Rechner, nur aus dem
Text. Sie messen Eigenschaften, die Hooks mit guter Haltequote meistens haben:
eine Länge, die man in unter drei Sekunden sagen kann, etwas Konkretes (eine
Zahl, ein Preis, eine Dauer), etwas, das auf dem Spiel steht, der wichtige
Teil vorne statt hinten, und eine Zuschauerin, die direkt angesprochen wird.

Was das NICHT ist:  ein Vorhersage-Werkzeug für Aufrufe. Es erkennt Begrüßungen,
Vorreden, Hooks ohne Konkretes und Hooks, die fünf Sekunden dauern. Es sagt
dir nicht, welcher von zwei guten Hooks besser läuft. Das entscheiden dein
Gesicht, dein Schnitt, dein Ton und wem Instagram das Reel zeigt. Die
Haltekurve in den Insights zählt mehr als dieses Skript.

Deutsche Fassung des Originals aus dem instagram-agent-skill von Jake
Schincariol (MIT). Wortlisten und Muster sind für gesprochenes Deutsch
umgebaut, die Hilfsverben und Artikel zählen nicht als Nutzlast.

Jede Prüfung gibt 0 bis 100. Höher ist besser.

Aufruf
  python3 hookscore.py hooks.txt              # ein Hook pro Zeile, als Rangliste
  python3 hookscore.py --hook "4.000 Euro hat mich ein Gerät gekostet."
  pbpaste | python3 hookscore.py -
  python3 hookscore.py hooks.txt --json
"""

import argparse
import json
import re
import statistics
import sys

WORD_RE = re.compile(r"[A-Za-zÄÖÜäöüß0-9€%'’-]+")
NUMBER_RE = re.compile(
    r"\d[\d.]*(?:,\d+)?\s?(?:€|euro)"                       # Geld
    r"|\b\d[\d.]*(?:,\d+)?\s?"                                # eine Zahl, mit oder
    r"(?:%|prozent|x|mal|min\b|minuten|std\b|stunden"         # ohne Einheit
    r"|tage?|wochen?|monate?|jahre?n?|sitzungen?|cm|mm|kg|grad)?",
    re.IGNORECASE)
HASHTAG_RE = re.compile(r"(?:^|\s)#\w+")
EMOJI_RE = re.compile(r"[\U0001F300-\U0001FAFF☀-➿]")

# Gesprochene Hooks sagen Zahlen laut. "zwanzig Euro" ist so konkret wie
# "20 €". "ein" und "erste" fehlen absichtlich: das sind meistens Füllwörter.
SPOKEN_NUMBERS = {
    "null", "zwei", "drei", "vier", "fünf", "sechs", "sieben", "acht", "neun",
    "zehn", "elf", "zwölf", "fünfzehn", "zwanzig", "dreißig", "vierzig",
    "fünfzig", "sechzig", "siebzig", "achtzig", "neunzig", "hundert", "tausend",
    "million", "millionen", "dutzend", "hälfte", "halbe", "doppelt", "dreifach",
    "zweite", "dritte", "vierte", "fünfte", "jede", "jeder", "jedes",
}
MONEY_WORDS = {
    "euro", "€", "prozent", "cent", "umsatz", "gewinn", "miete", "preis",
    "rechnung", "gehalt", "kosten", "gutschein", "rabatt",
}

# Wörter, die etwas aufs Spiel setzen. Ein Hook ohne eines davon ist eine
# Feststellung; ein Hook mit einem ist ein Grund weiterzuschauen.
STAKES = {
    "hör", "hört", "stopp", "stop", "nie", "niemals", "falsch", "fehler",
    "verloren", "verlierst", "verliert", "kostet", "gekostet", "kosten",
    "kaputt", "gescheitert", "scheitert", "versagt", "keiner", "niemand",
    "kein", "keine", "keinen", "nicht", "nichts", "aufgehört", "gekündigt",
    "gelöscht", "ersetzt", "weg", "weggeworfen", "gratis", "umsonst",
    "bezahlt", "gespart", "sparst", "verboten", "schlimmste", "schlimmsten",
    "hasse", "verschwendet", "verschwendung", "abzocke", "lüge", "lügen",
    "wahrheit", "geheimnis", "versteckt", "verschweigt", "verschwiegen",
    "bevor", "bis", "stattdessen", "statt", "aber", "außer", "problem",
    "risiko", "gefahr", "gefährlich", "warnung", "bereue", "bereut",
    "wünschte", "sollte", "solltest", "trotzdem", "schon", "nur", "ohne",
    "gegen", "versus", "vs", "wirklich", "ehrlich", "tut", "weh", "schmerz",
    "schmerzen", "brennt", "eingewachsen", "narben", "pickel", "rot",
    "schuld", "peinlich", "angst", "zu", "spät", "teuer", "billig",
}

# Satzanfänge, die die erste Sekunde mit nichts füllen.
WEAK_OPENERS = [
    "also", "ok", "okay", "hey", "hi", "hallo", "ihr lieben", "leute",
    "willkommen", "heute", "im grunde", "ehrlich gesagt", "schau mal",
    "hört mal", "ähm", "einfach", "lass uns", "lasst uns", "ich wollte",
    "ich will", "ich möchte", "eine der", "einer der", "eines der",
    "hast du", "habt ihr", "kennst du", "kennt ihr", "bist du", "seid ihr",
    "in diesem", "in dem video", "im heutigen", "die sache", "viele",
    "es gibt", "das ist", "es ist", "als", "wenn es", "wie ihr wisst",
    "wie du weißt", "herzlich willkommen", "guten morgen", "schönen",
    "wusstest du", "wusstet ihr", "ich", "wir", "mein", "meine", "unser",
]

# Befehle, die den Platz ganz vorne verdienen.
IMPERATIVES = {
    "hör", "hört", "nimm", "nehmt", "kopier", "kopiert", "lösch", "löscht",
    "probier", "probiert", "schau", "schaut", "guck", "guckt", "lies", "lest",
    "speicher", "speichert", "benutz", "benutzt", "bau", "baut", "mach",
    "macht", "schreib", "schreibt", "schick", "schickt", "fang", "fangt",
    "vergiss", "vergesst", "stopp", "lass", "lasst", "pass", "passt", "achte",
    "achtet", "rasier", "rasiert", "nie", "niemals", "immer", "teste",
    "testet", "frag", "fragt", "geh", "geht", "komm", "kommt", "zeig", "zeigt",
}

DEALBREAKERS = [
    (re.compile(r"(?i)^\s*(?:hör auf zu scrollen|nicht weiterscrollen|stopp? scrollen|scroll nicht weiter)"),
     "Beginnt mit „hör auf zu scrollen“. Wer um Aufmerksamkeit bittet, hat sie noch nicht verdient."),
    (re.compile(r"(?i)\b(?:in (?:diesem|dem heutigen) (?:video|reel)|ich zeig(?:e)? (?:dir|euch)(?: heute| jetzt)?,? wie|heute zeig(?:e)? ich)\b"),
     "Video-Vorrede. Streichen und direkt mit dem Ergebnis anfangen."),
    (re.compile(r"(?i)^\s*(?:hey |hi |hallo |servus |moin |ihr lieben|willkommen|herzlich willkommen)"),
     "Begrüßung. Niemand kommt in den Feed, um begrüßt zu werden."),
    (HASHTAG_RE,
     "Hashtag im Hook. Hashtags gehören ans Ende der Caption, wenn überhaupt."),
    (EMOJI_RE,
     "Emoji im Hook. Im Bild ist in Hook-Größe Platz für Wörter oder für ein Emoji, nicht für beides."),
    (re.compile(r"(?i)\b(?:für immer|garantiert|100\s?%|hundertprozentig|schmerzfrei|heilt|heilung|wunder)\b"),
     "Versprechen, das kein Studio halten darf (für immer, garantiert, 100 %, schmerzfrei, Heilung). Umformulieren, siehe nicht-versprechen.md."),
]


def clamp(n):
    return max(0.0, min(100.0, n))


def words(text):
    # "4.000 €" ist gesprochen ein Wort, also auch hier.
    return WORD_RE.findall(re.sub(r"(?<=\d)\.(?=\d{3})", "", text))


def check_length(text):
    """Ein Hook muss landen, bevor der Daumen weiterzieht. Etwa zwei Sekunden."""
    w = words(text)
    n = len(w)
    secs = n / 2.5                       # ~150 Wörter pro Minute, deutsch gesprochen
    chars = len(text.strip())
    if 4 <= n <= 11:
        score = 100.0
    elif n < 4:
        score = clamp(100 - (4 - n) * 20)
    else:
        score = clamp(100 - (n - 11) * 11)
    if chars > 65:                       # zwei Zeilen großer Bild-Text
        score -= 12
    return clamp(score), f"{n} Wörter, {chars} Zeichen, ~{secs:.1f} s gesprochen (Ziel 4 bis 11 Wörter)"


def check_specificity(text):
    """Eine konkrete Sache schlägt drei abstrakte."""
    nums = [n.strip() for n in NUMBER_RE.findall(text) if n.strip()]
    low = [w.lower().strip("'’") for w in words(text)]
    spoken = [w for w in low if w in SPOKEN_NUMBERS or w in MONEY_WORDS]
    hits = len(nums) + len(spoken)
    score = 15.0 if hits == 0 else clamp(45 + hits * 30)
    found = ", ".join(nums[:2] + spoken[:2])
    return score, (f"{hits} konkrete Angabe(n)" + (f": {found}" if found else
                   ", keine Zahl, kein Preis, keine Dauer, nichts Nachprüfbares"))


def check_stakes(text):
    """Spannung, Kosten, Verneinung. Etwas, das die Zuschauerin verlieren könnte."""
    w = [x.lower().strip("'’") for x in words(text)]
    hits = [x for x in w if x in STAKES]
    markers = sorted(set(hits))
    if re.search(r"\d[\d.]*\s?(?:€|euro)", text, re.I):
        markers.append("ein Preis")
    n = len(markers)
    score = {0: 20.0, 1: 70.0}.get(n, 100.0)
    detail = f"{n} Spannungswort/-wörter" + (f": {', '.join(markers[:4])}" if markers else
                                              ", in dieser Zeile steht nichts auf dem Spiel")
    return clamp(score), detail


def check_frontload(text):
    """Das interessante Wort darf nicht an Position neun stehen."""
    w = words(text)
    if not w:
        return 0.0, "leer"
    low = [x.lower().strip("'’") for x in w]
    opener = " ".join(low[:2])
    penalty = 0
    hit_opener = None
    for weak in WEAK_OPENERS:
        if opener.startswith(weak + " ") or opener == weak or low[0] == weak:
            penalty, hit_opener = 30, weak
            break
    payload = None
    for i, token in enumerate(low):
        if (token in STAKES or token in SPOKEN_NUMBERS or token in MONEY_WORDS
                or NUMBER_RE.match(w[i])):
            payload = i
            break
    if payload is None:
        base = 30.0
        where = "kein tragendes Wort in der ganzen Zeile"
    elif payload <= 3:
        base = 100.0
        where = f"tragendes Wort an Position {payload + 1}"
    elif payload <= 6:
        base = 70.0
        where = f"tragendes Wort an Position {payload + 1}, könnte weiter nach vorn"
    else:
        base = 40.0
        where = f"tragendes Wort an Position {payload + 1}, zu spät"
    detail = where + (f"; schwacher Anfang „{hit_opener}“" if hit_opener else "")
    return clamp(base - penalty), detail


def check_address(text):
    """Auf eine Zuschauerin gerichtet, oder in der Luft hängend."""
    low = text.lower()
    w = [x.lower().strip("'’") for x in words(text)]
    if re.search(r"\b(du|dir|dich|dein|deine|deinen|deiner|deinem|ihr|euch|euer|eure|sie|ihnen|ihre|ihrem|ihren)\b", low):
        return 100.0, "spricht die Zuschauerin an"
    if w and w[0] in IMPERATIVES:
        return 90.0, f"beginnt mit einem Befehl („{w[0]}“)"
    if re.search(r"\b(ich|mich|mir|mein|meine|meinen|wir|uns|unser|unsere)\b", low):
        return 70.0, "erste Person, keine Zuschauerin genannt"
    return 35.0, "dritte Person, niemand im Raum"


CHECKS = ["LÄNGE", "KONKRET", "EINSATZ", "VORNE", "ANSPRACHE"]


def run(text):
    results = {
        "LÄNGE": check_length(text),
        "KONKRET": check_specificity(text),
        "EINSATZ": check_stakes(text),
        "VORNE": check_frontload(text),
        "ANSPRACHE": check_address(text),
    }
    flags = [msg for pattern, msg in DEALBREAKERS if pattern.search(text)]
    scores = [results[c][0] for c in CHECKS]
    # Die schwächste Eigenschaft deckelt den Hook: eine schlechte reicht,
    # damit der Daumen weiterzieht.
    overall = statistics.mean(scores) * 0.6 + min(scores) * 0.4 - len(flags) * 15
    overall = clamp(overall)
    verdict = "STARK" if overall >= 70 and min(scores) >= 55 and not flags else (
        "OK" if overall >= 50 else "SCHWACH")
    return results, overall, verdict, flags


def bar(score, width=24):
    filled = round(score / 100 * width)
    return "#" * filled + "." * (width - filled)


def render_one(text, results, overall, verdict, flags, out=sys.stdout):
    print("\nHOOK-WERTUNG", file=out)
    print("=" * 62, file=out)
    print(f"  „{text.strip()}“\n", file=out)
    for name in CHECKS:
        score, detail = results[name]
        print(f"  {name:<11} {bar(score)} {score:5.1f}", file=out)
        print(f"  {'':<11} {detail}", file=out)
    print("-" * 62, file=out)
    print(f"  {'GESAMT':<11} {bar(overall)} {overall:5.1f}   {verdict}", file=out)
    for f in flags:
        print(f"\n  K.O.-KRITERIUM  {f}", file=out)
    if verdict != "STARK":
        weakest = min(CHECKS, key=lambda c: results[c][0])
        print(f"\n  Schwächste Eigenschaft: {weakest}. Die zuerst beheben, dann neu bewerten.", file=out)
    print("", file=out)


def render_table(rows, out=sys.stdout):
    print("\nHOOK-RANGLISTE\n" + "=" * 78, file=out)
    for i, r in enumerate(rows, 1):
        mark = "->" if i == 1 else "  "
        hook = r["hook"] if len(r["hook"]) <= 62 else r["hook"][:59] + "..."
        print(f"{mark} {r['score']:5.1f} {r['verdict']:<7} {hook}", file=out)
        print(f"        schwächste: {r['weakest']} ({r['checks'][r['weakest']]['score']:.0f})", file=out)
        for f in r["flags"]:
            print(f"        K.O.: {f}", file=out)
    print("\nDen obersten drehen. Liegt der oberste unter 50, ist keiner davon der Hook.\n",
          file=out)


def main():
    ap = argparse.ArgumentParser(description="Bewertet einen Reel-Hook nach fünf Eigenschaften.")
    ap.add_argument("input", nargs="?", default="-", help="Datei mit einem Hook pro Zeile, oder -")
    ap.add_argument("--hook", help="einen einzelnen Hook direkt bewerten")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    if args.hook:
        lines = [args.hook]
    else:
        raw = sys.stdin.read() if args.input == "-" else open(args.input, encoding="utf-8").read()
        lines = [l.strip() for l in raw.splitlines() if l.strip()]
    if not lines:
        print("nichts zu bewerten", file=sys.stderr)
        sys.exit(2)

    payload = []
    for line in lines:
        results, overall, verdict, flags = run(line)
        payload.append({
            "hook": line,
            "checks": {k: {"score": round(v[0], 1), "detail": v[1]} for k, v in results.items()},
            "weakest": min(CHECKS, key=lambda c: results[c][0]),
            "flags": flags,
            "score": round(overall, 1),
            "verdict": verdict,
        })

    if args.json:
        print(json.dumps(payload if len(payload) > 1 else payload[0], indent=2, ensure_ascii=False))
        return

    if len(payload) == 1:
        results, overall, verdict, flags = run(lines[0])
        render_one(lines[0], results, overall, verdict, flags)
    else:
        render_table(sorted(payload, key=lambda r: -r["score"]))

    sys.exit(0 if max(p["score"] for p in payload) >= 70 else 1)


if __name__ == "__main__":
    main()
