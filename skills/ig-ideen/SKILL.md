---
name: ig-ideen
description: >-
  Findet Reel-Ideen für ein Kosmetikstudio, wenn der Nutzerin nichts einfällt:
  recherchiert zur Behandlung in Foren, Fragen-Seiten und Bewertungen, was
  Frauen fragen, befürchten und falsch glauben, und macht daraus eine Liste
  mit fertigen Hooks in ideen.md. Nutzen, wenn die Nutzerin sagt "ich hab keine
  Ideen", "recherchiere Themen zu X", "was soll ich posten", "Ideen für
  Reels", "/ig-ideen", oder bevor /ig-reel ohne Idee aufgerufen wird.
---

# ig-ideen

Die meisten Studio-Inhaberinnen scheitern nicht am Drehen, sondern an der
Frage, worüber. Dieser Skill beantwortet sie mit dem, was Kundinnen wirklich
wissen wollen, statt mit dem, was sich ein Marketing-Plan ausdenkt.

## Vor dem Start

1. `studio-profil.md` lesen. Fehlt sie, `/ig-start` vorschlagen.
2. `lernen.md` lesen, falls vorhanden: Themen, die die Nutzerin nicht mag,
   fallen raus.
3. `recherche.md` lesen, falls vorhanden. Ist sie jünger als drei Monate und
   passt zur gewünschten Behandlung, darauf aufbauen und nur ergänzen.
4. `../ig-reel/hooks.json`, `../ig-reel/hook-regeln.md` und
   `../ig-start/nicht-versprechen.md` lesen.

Fragen, für welche Behandlung, falls nicht gesagt. Standard ist die
Hauptbehandlung aus dem Profil.

## Recherchieren

Mit der Websuche dieser Sitzung, 10 bis 20 Quellen:

- **Fragen-Seiten und Foren:** gutefrage.net, reddit (r/de, r/FragReddit,
  r/beauty), Erdbeerlounge, urbia, Kommentare unter Ratgeberartikeln.
- **Bewertungen** von Studios mit derselben Behandlung (Google, Treatwell):
  Was loben Frauen, was hat sie enttäuscht?
- **Ein bis zwei Fachquellen** für Fakten (Fachgesellschaft, Verbraucherzentrale,
  Bundesamt für Strahlenschutz bei Laser und IPL).

Festhalten, wörtlich und mit Link:
- Fragen, so wie Frauen sie stellen
- Ängste und Einwände
- Mythen und was stimmt
- Alltagsszenen und Gefühle (Freibad, Partner, Urlaub, morgens keine Zeit)
- ihre Wörter (Stoppeln, Rasurpickel) gegenüber Fachwörtern (Follikel, Anagen)

Ergänzend in `recherche.md` schreiben (oder anlegen), mit Datum. Nur Belegtes.

Gibt es keine Websuche, sagen, dass die Ideen dann nur aus dem Profil kommen,
und mit den Kundinnen-Fragen, Haltungen und Befürchtungen aus
`studio-profil.md` arbeiten. Ergänzend `../ig-plan/ideen-vorrat.md`.

## Aus Recherche werden Ideen

15 Ideen, gemischt nach Typ:

| Typ | Woher | Beispiel-Formel |
| --- | --- | --- |
| **Frage** | eine Frage aus Foren oder dem Profil, wörtlich | #16 Die Original-Frage |
| **Angst** | eine Befürchtung, ehrlich beantwortet | #12 Der Einwand, #7 Falsch und nicht deine Schuld |
| **Mythos** | ein Irrtum, richtiggestellt | #3 Das sagt dir keiner, #2 Hör auf damit |
| **Szene** | ein Gefühl aus dem Alltag | #14 Der Zuruf, #25 Jemand anderes |
| **Fakt** | eine Zahl oder ein Ablauf aus dem Studio | #23 Die Zahl, #5 Zeitsprung |

Für jede Idee:
- **Thema** in einem Satz
- **gesprochener Hook**, vollständig, 4 bis 11 Wörter, nach `hook-regeln.md`:
  emotional, der Gegenstand (Laser, Haare, Sitzung, Haut) steht vorne,
  „du“, keine Begrüßung
- **Formel-Nummer**
- **warum sie trägt**: der O-Ton oder die Quelle dahinter
- **Wertung** aus `../ig-reel/hookscore.py` (alle 15 Hooks in eine Datei, ein
  Durchlauf)

Jeden Hook gegen `nicht-versprechen.md` prüfen. Kein „für immer“, kein
„schmerzfrei“, keine Garantie, auch wenn Frauen in Foren genau danach fragen:
Die Frage darf zitiert werden, das Versprechen nicht.

## Ausgabe

Die besten fünf zuerst, dann der Rest kurz:

```
IDEEN  ·  dauerhafte Haarentfernung  ·  15 Ideen aus 14 Quellen

TOP 5
  86  #16  „‚Tut das weh?‘ Die Frage kriege ich jede Woche.“
           Frage Nr. 1 in fast jedem Forum. Ehrliche Antwort: Wärme, kurzes Zwicken.
  ...

WEITERE 10
  ...

Welche nimmst du? Sag die Nummer, dann schreibe ich mit /ig-reel das Skript.
Oder sag, was dir nicht gefällt, dann suche ich andere.
```

In `ideen.md` speichern (anhängen, nicht überschreiben), mit Datum und Status
`offen`. `/ig-reel` setzt den Status auf `gedreht`, wenn daraus ein Skript wird.
`/ig-plan` zieht sich daraus die Woche.

Was die Nutzerin ablehnt („das Thema mag ich nicht“), in `lernen.md` unter
„Mag ich nicht“ eintragen.

Nichts wird gepostet. Dieser Skill sammelt und schlägt vor.
