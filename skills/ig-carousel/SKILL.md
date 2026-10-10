---
name: ig-carousel
description: >-
  Baut ein Instagram-Karussell: das Cover, das zum Wischen bringt, den Text
  Folie für Folie, und die 1080x1350-Dateien zum Hochladen. Nutzen, wenn die
  Nutzerin sagt "Karussell", "Folien", "Wisch-Beitrag", "mach daraus ein
  Karussell", oder eine Idee in Schritten oder als Liste hat, die als
  einzelnes Bild untergehen würde.
---

# ig-carousel

Karussells sind das Format mit der längsten Verweildauer im Raster, weil
Wischen eine Interaktion ist und Scrollen nicht. Sie bekommen außerdem eine
zweite Chance: Instagram kann ein Karussell jemandem, der beim ersten Mal
nicht reagiert hat, noch einmal ab einer späteren Folie zeigen, also muss
Folie zwei auch allein stehen.

Das Format belohnt einen Gedanken in Schritten. Es bestraft eine Caption, die
in Stücke geschnitten wurde.

## Wann Karussell statt Reel

Ein Karussell, wenn die Idee **eine Reihenfolge hat und nachgelesen werden
muss**: Schritte, ein Ablauf mit Teilen, ein Vorher und Nachher, eine Liste,
die es wert ist, abfotografiert zu werden. Im Studio: die fünf Dinge vor dem
ersten Termin, der Ablauf einer Sitzung, die Pflege in den Tagen danach, die
Preisliste erklärt. Ein Reel, wenn die Idee Bewegung hat, ein Gesicht, oder
ein Ergebnis, das man passieren sehen muss.

Ist die Idee eine einzelne Behauptung, ist sie keins von beidem. An `/ig-reel`
geben und das sagen.

`studio-profil.md` lesen; fehlt sie, `/ig-start` vorschlagen.
`../ig-start/nicht-versprechen.md` gilt für jede Folie.

## Aufbau

6 bis 10 Folien. Die Obergrenze sind 20, und 20 ist fast immer ein Buch, das
niemand zu Ende liest. Unter 5 fängt das Wischen nie an.

```
1         COVER     der Hook. 6 Wörter oder weniger, in einer Größe, die im
                    Raster als Daumennagel lesbar ist. Eine Zeile Versprechen darunter.
2         EINSATZ   warum das zählt, in einem Satz. Diese Folie ist auch ein
                    zweites Cover, also darf sie keine Einleitung sein.
3 bis N   EIN GEDANKE JE FOLIE. Eine Überschrift mit 3 bis 7 Wörtern, höchstens
                    25 Wörter darunter. Braucht eine Folie einen Absatz, sind es zwei Folien.
N+1       ÜBERSICHT das Ganze als Liste. Das ist die Folie, die abfotografiert wird.
LETZTE    CTA       eine Handlung. Speichern, ein Stichwort kommentieren, Termin, oder folgen. Eine.
```

## Regeln für den Folientext

- **Das Cover ist 80 Prozent des Ergebnisses.** Sechs Wörter. Groß. Nichts im
  Rest rettet ein Cover, bei dem niemand wischt.
- **Für den Raster-Ausschnitt gestalten.** Das Profilraster schneidet auf ein
  Hochformat, das höher als breit ist, und das genaue Verhältnis hat sich
  mehr als einmal geändert. In 1080 x 1350 bauen und den Cover-Text gut in
  der Mitte halten, frei von den äußeren 120 Pixeln auf jeder Seite, dann ist
  der Ausschnitt egal.
- **Folien nummerieren** (3/8). Mehr Leute lesen zu Ende, wenn sie das Ende
  sehen.
- **Keine Folie ist ein Absatz.** Wenn es nicht in 25 Wörtern geht, teilen.
- **Die Übersichtsfolie ist die, die abfotografiert und weitergeschickt
  wird.** Teilen ist das stärkste Signal, das man bekommen kann. Sie muss
  ohne Zusammenhang lesbar sein.
- **Der Handle auf jeder Folie**, klein, unten in der Ecke. Screenshots reisen
  ohne dich.
- **Alt-Text mindestens auf dem Cover.** Er wird von Vorlese-Programmen und
  von Instagram gelesen.
- **Vorher-Nachher nur mit eigenen Bildern und Einverständnis.**

## Die Dateien bauen

Instagram will 1080 x 1350 (4:5), JPEG oder PNG, bis zu 20 Stück. Als HTML
bauen und jede Folie drucken:

```bash
# ein <section> je Folie, 1080x1350, page-break-after: always
# dann Chrome headless --print-to-pdf, oder ein HTML-zu-Bild-Werkzeug, das schon da ist
```

Das HTML mit `width:1080px; height:1350px` schreiben, einer Akzentfarbe aus
dem Studio (nachfragen, wenn sie nicht im Profil steht), und Schrift nicht
kleiner als 32 px, weil das auf einem Handy in einem Drittel der echten Größe
gelesen wird. Ist kein Werkzeug zum Rendern da, die Folientexte so ausgeben,
dass die Nutzerin sie in Canva oder CapCut einsetzen kann, mit der Angabe
„Folie 1: Überschrift / Text“.

## Nach dem Rendern prüfen

Den Kontaktbogen oder jede Folie einmal ansehen, bevor sie der Nutzerin
gezeigt wird: Ist jeder Text lesbar, auch auf dunklen Folien? Stimmen
Nummern und Handle? Eine Folie mit unsichtbarem Text ist schlimmer als keine.
Fällt etwas auf, HTML korrigieren und neu rendern. Die Folientexte
zusätzlich in die Markdown-Datei in `beitraege/` schreiben, damit sie auch
ohne Bilder weiterverwendet werden können.

## Ausgabe

Zuerst der Text Folie für Folie, als nummerierte Liste, die die Nutzerin in
zehn Sekunden lesen und ändern kann, bevor etwas gerendert wird. Dann die
**Caption**, die bei einem Karussell Aufgabe B in `/ig-caption` ist: Die
Caption arbeitet hier, weil das Cover seine sechs Wörter schon verbraucht hat.

Beides durch `/ig-human`. Die Dateien erst bauen, wenn die Nutzerin den Text
freigegeben hat. Bei „ja“ in `beitraege/JJJJ-MM-TT-<kurzname>.md` speichern
und in `log.md` eine Zeile anhängen.

```
KARUSSELL  ·  8 Folien

1  COVER     5 DINGE VOR SITZUNG 1
             Was ich jeder Kundin vorher sage.
2  EINSATZ   Wer eines davon vergisst, verschenkt die erste Sitzung.
3            RASIEREN, NICHT ZUPFEN
             Am Abend davor. Die Wurzel muss drin bleiben, sonst trifft der Laser nichts.
...
7  ÜBERSICHT Alle fünf, in Reihenfolge.
8  CTA       Schreib ZETTEL in die Kommentare, dann schick ich dir die Liste.

Caption: Aufgabe B, Hook in Zeile 1, eine Aufforderung, 3 Hashtags.
```

Nichts wird hochgeladen. Die Nutzerin postet es.

## Lernen

`lernen.md` im Arbeitsordner vor dem Schreiben lesen und beachten. Korrigiert
die Nutzerin etwas, das über ihren Geschmack sagt („würde ich nie sagen“, „zu
werblich“, „genau so“), danach eine Zeile mit Datum in `lernen.md` eintragen
und kurz sagen: „Hab ich mir gemerkt.“
