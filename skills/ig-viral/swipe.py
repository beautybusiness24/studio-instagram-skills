#!/usr/bin/env python3
"""
swipe.py - ordnet gesammelte Reels danach, wie weit jedes über dem Normalwert
seines eigenen Accounts lag, benennt die Hook-Formel und schreibt die
Ideen-Datei.

Der Kern ist eine Korrektur: Rohe Aufrufe sind kein Beleg. Ein Account mit
2.000.000 Followern und 400.000 Aufrufen hatte einen ruhigen Tag. Ein Account
mit 4.000 Followern und 400.000 Aufrufen hat etwas gefunden. Dieses Skript
ordnet nach dem Vielfachen über dem eigenen Normalwert des Accounts, denn das
ist die einzige Version von „ist viral gegangen“, aus der man etwas lernen
kann.

Eingabe ist eine tab-getrennte Datei, die du beim Durchsehen füllst, ein Reel
pro Zeile, mit einer Kopfzeile:

    account   follower   median   aufrufe   hook
    @studio   4800       1100     41200     keiner sagt dir dass nach sitzung eins mehr haare da sind

`median` ist der typische Aufrufwert dieses Accounts in letzter Zeit und die
bessere Basis. Wenn du nur `follower` hast, lass median weg, das Skript sagt es.
`hook` ist die erste Zeile des Reels, gesprochen oder im Bild, in deren Worten.
Englische Spaltennamen (followers, views) gehen auch.

Deutsche Fassung des Originals aus dem instagram-agent-skill (MIT).

Aufruf
  python3 swipe.py gesammelt.tsv
  python3 swipe.py gesammelt.tsv --out ideen.md
  python3 swipe.py gesammelt.tsv --json
"""

import argparse
import json
import os
import re
import statistics
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
HOOKS = os.path.join(HERE, "..", "ig-reel", "hooks.json")
WORD_RE = re.compile(r"[A-Za-zÄÖÜäöüß0-9€%'’-]+")

try:                                              # optional: Hooks auch bewerten
    sys.path.insert(0, os.path.join(HERE, "..", "ig-reel"))
    from hookscore import run as score_hook       # noqa: E402
except Exception:                                 # ig-viral allein kopiert
    score_hook = None

ALIASES = {
    "konto": "account", "profil": "account", "handle": "account",
    "followers": "follower", "abonnenten": "follower", "abos": "follower",
    "mittel": "median", "normal": "median", "normalwert": "median",
    "views": "aufrufe", "aufruf": "aufrufe", "plays": "aufrufe",
    "erste zeile": "hook", "zeile": "hook",
}


def load_formulas(path):
    try:
        d = json.load(open(path, encoding="utf-8"))
    except Exception:
        return None
    by_id = {h["id"]: h for h in d["hooks"]}
    order = d.get("classify_order") or sorted(by_id)
    return [(by_id[i]["id"], by_id[i]["name"],
             re.compile(by_id[i]["match"], re.IGNORECASE)) for i in order if i in by_id]


def classify(hook, formulas):
    if not formulas:
        return None, "ohne Formel"
    for fid, name, pattern in formulas:
        if pattern.search(hook):
            return fid, name
    return None, "ohne Formel"


def read_rows(path):
    raw = sys.stdin.read() if path == "-" else open(path, encoding="utf-8").read()
    lines = [l for l in raw.splitlines() if l.strip() and not l.lstrip().startswith("#")]
    if not lines:
        return []
    head = [ALIASES.get(c.strip().lower(), c.strip().lower()) for c in lines[0].split("\t")]
    if "aufrufe" in head and "hook" in head:
        cols, body = head, lines[1:]
    else:
        cols, body = ["account", "follower", "aufrufe", "hook"], lines
    rows = []
    for line in body:
        cells = line.split("\t")
        if len(cells) < len(cols):
            cells += [""] * (len(cols) - len(cells))
        r = dict(zip(cols, [c.strip() for c in cells]))
        try:
            r["aufrufe"] = int(re.sub(r"[^\d]", "", r.get("aufrufe", "")) or 0)
        except ValueError:
            continue
        for k in ("follower", "median"):
            digits = re.sub(r"[^\d]", "", r.get(k, "") or "")
            r[k] = int(digits) if digits else None
        if r["aufrufe"] and r.get("hook"):
            rows.append(r)
    return rows


def analyse(rows, formulas):
    used_median = any(r.get("median") for r in rows)
    for r in rows:
        base = r.get("median") or r.get("follower") or 0
        r["basis"] = base
        r["vielfaches"] = round(r["aufrufe"] / base, 2) if base else None
        r["formel_id"], r["formel"] = classify(r["hook"], formulas)
        r["woerter"] = len(WORD_RE.findall(r["hook"]))
        if score_hook:
            _, overall, verdict, _ = score_hook(r["hook"])
            r["hook_score"], r["hook_urteil"] = round(overall, 1), verdict
        else:
            r["hook_score"], r["hook_urteil"] = None, None
    ranked = sorted(rows, key=lambda r: -(r["vielfaches"] or 0))
    third = max(1, len(ranked) // 3)
    top, bottom = ranked[:third], ranked[-third:]

    def med(items, key):
        vals = [i[key] for i in items if i.get(key) is not None]
        return round(statistics.median(vals), 1) if vals else None

    counts = {}
    for r in top:
        counts[r["formel"]] = counts.get(r["formel"], 0) + 1
    return {
        "basis": "Normalwert des Accounts" if used_median else "Followerzahl",
        "n": len(ranked),
        "accounts": len({r.get("account", "") for r in ranked}),
        "reels": ranked,
        "top_formeln": sorted(counts.items(), key=lambda kv: -kv[1]),
        "top_hook_score": med(top, "hook_score"),
        "bottom_hook_score": med(bottom, "hook_score"),
        "top_woerter": med(top, "woerter"),
        "bottom_woerter": med(bottom, "woerter"),
        "ohne_formel": sum(1 for r in ranked if r["formel"] == "ohne Formel"),
    }


def render(a, out=sys.stdout):
    head = (f"IDEEN-DATEI  ·  {a['n']} Reels  ·  {a['accounts']} Accounts  ·  "
            f"Basis: {a['basis']}")
    print("\n" + head, file=out)
    print("=" * max(len(head), 78), file=out)
    for r in a["reels"]:
        mult = f"{r['vielfaches']:.1f}x" if r["vielfaches"] else "   ?"
        score = f"{r['hook_score']:.0f}" if r["hook_score"] is not None else " -"
        fid = f"#{r['formel_id']:<2}" if r["formel_id"] else "-  "
        print(f"  {mult:>7}  Hook {score:>3}  {fid} {r['formel'][:24]:<24} "
              f"{r.get('account', '')[:16]:<16} {r['aufrufe']:>9,}".replace(",", "."), file=out)
        print(f"           „{r['hook'][:96]}“", file=out)
    print("-" * max(len(head), 78), file=out)
    print("WAS IN DIESEM STAPEL FUNKTIONIERT", file=out)
    if a["top_formeln"]:
        print("  oberes Drittel:        "
              + ", ".join(f"{n} x{c}" for n, c in a["top_formeln"][:4]), file=out)
    if a["top_hook_score"] is not None:
        print(f"  Hook-Wertung (Median): oben {a['top_hook_score']:.0f}  "
              f"vs. unten {a['bottom_hook_score']:.0f}", file=out)
    print(f"  Hook-Länge (Median):   oben {a['top_woerter']} Wörter  "
          f"vs. unten {a['bottom_woerter']} Wörter", file=out)
    print(f"  ohne Formel:           {a['ohne_formel']} von {a['n']}. Die von Hand lesen, "
          "dort versteckt sich eine Formel, die du noch nicht hast.", file=out)
    print("\n  Ein von Hand gesammelter Stapel ist ein Hinweis, kein Beweis. Zwölf Reels zeigen "
          "dir nichts,\n  vierzig über sechs Accounts zeigen dir etwas. Erst mehr sammeln, "
          "dann glauben.\n", file=out)


def to_markdown(a):
    lines = ["# Ideen-Datei", "",
             f"{a['n']} Reels aus {a['accounts']} Accounts. "
             f"Geordnet nach Vielfachem über {a['basis']}.", ""]
    for r in a["reels"]:
        mult = f"{r['vielfaches']:.1f}x" if r["vielfaches"] else "?"
        lines += [f"## {mult}  {r['formel']}  ({r.get('account', '')})",
                  f"- Aufrufe: {r['aufrufe']:,}  Basis: {r['basis']:,}".replace(",", "."),
                  f"- Hook-Wertung: {r['hook_score']}  Wörter: {r['woerter']}",
                  f"- Hook: „{r['hook']}“", ""]
    return "\n".join(lines) + "\n"


def main():
    ap = argparse.ArgumentParser(description="Ordnet gesammelte Reels nach Vielfachem über dem Normalwert.")
    ap.add_argument("input", nargs="?", default="-", help="TSV-Datei, oder - für stdin")
    ap.add_argument("--hooks", default=HOOKS, help="Pfad zu ig-reel/hooks.json")
    ap.add_argument("--out", help="Ideen-Datei zusätzlich als Markdown hierhin schreiben")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    rows = read_rows(args.input)
    if not rows:
        print("keine brauchbaren Zeilen. Es braucht eine tab-getrennte Datei mit mindestens aufrufe und hook.",
              file=sys.stderr)
        sys.exit(2)
    formulas = load_formulas(args.hooks)
    a = analyse(rows, formulas)
    if not formulas:
        print("Hinweis: hooks.json nicht gefunden, Formeln nicht benannt. --hooks angeben.", file=sys.stderr)
    if score_hook is None:
        print("Hinweis: hookscore.py nicht importierbar, Hook-Wertung übersprungen.", file=sys.stderr)

    if args.json:
        print(json.dumps(a, indent=2, ensure_ascii=False))
    else:
        render(a)
    if args.out:
        path = os.path.expanduser(args.out)
        os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
        open(path, "w", encoding="utf-8").write(to_markdown(a))
        print(f"geschrieben: {path}", file=sys.stderr)


if __name__ == "__main__":
    main()
