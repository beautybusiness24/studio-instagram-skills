---
name: ig-plan
description: >-
  Baut die Instagram-Woche eines Kosmetikstudios: was gepostet wird, in
  welchem Format, wann, und mit wem man sich austauscht. Nutzen, wenn die
  Nutzerin sagt "plane meine Woche", "was soll ich posten", "Content-Plan",
  "Wochenplan", "ich habe keine Ideen", oder einen Posting-Plan und eine
  Liste zum Kommentieren will.
---

# ig-plan

Die Schaltzentrale. Alles andere in diesem Paket führt aus; das hier
entscheidet, was ausgeführt wird. Einmal pro Woche laufen lassen, am selben
Tag. Für ein Studio ist Sonntagabend oder Montag früh meistens richtig, vor
der ersten Kundin.

## Eingabe

Liegen `studio-profil.md`, `ideen.md` und `log.md` im Arbeitsordner, alle
drei lesen. Die Ideen-Datei ist der eigene Beleg der Nutzerin aus `/ig-viral`,
welche Formeln in ihrer Nische gerade landen, und sie schlägt alles in dieser
Datei. Das Log verhindert, dass der Plan ein Thema aus den letzten zwei
Wochen wiederholt. Fehlt `studio-profil.md`, `/ig-start` vorschlagen.

Dann nach genau einer Sache fragen, denn aus ihr kommen die Beiträge:

**Was ist diese Woche im Studio passiert?** Eine Kundin, die etwas gesagt hat,
eine Frage, die dreimal kam, ein Fehler, ein Gerät, das gestreikt hat, ein
Ergebnis, eine Absage, ein Preisgespräch. Fünf Minuten erzählen lassen, nicht
unterbrechen. Jeder Satz darin ist ein möglicher Beitrag.

Wenn gar nichts kommt: die drei häufigsten Kundinnen-Fragen aus dem
Studio-Profil nehmen. Die gehen immer.

## Was gepostet wird

Drei bis fünf Beiträge pro Woche, mindestens zwei davon Reels. Für ein Studio
mit Behandlungsalltag sind **drei Reels und ein Karussell** ein Takt, der sich
halten lässt. Reels sind das einzige Format auf Instagram, das verlässlich
Leute erreicht, die dem Account nicht folgen. Karussells gehen in die Tiefe
bei denen, die schon folgen. Stories sind täglich und werden getrennt geplant.

Über die Woche mischen, nie zwei vom gleichen Typ hintereinander:

| Typ | Anteil | Aufgabe |
| --- | --- | --- |
| **Beleg** | 1 pro Woche | etwas, das passiert ist, mit einer Zahl. Reel. Ein Ergebnis, ein Vorher-Nachher mit Einverständnis, eine Zählung aus dem Studio. |
| **Erklären** | 1 bis 2 pro Woche | eine Sache, die die Zuschauerin heute umsetzen kann. Reel oder Karussell. Vorbereitung, Pflege danach, was im ersten Termin passiert. |
| **Haltung** | 1 pro Woche | eine Meinung, die Follower kosten könnte. Reel. „Wer vor dem Termin zupft, verschenkt eine Sitzung.“ |
| **Geschichte** | 1 alle zwei Wochen | eine Szene mit einem Preis. Reel. Die Kundin, die nach 15 Jahren Wachs kam. |
| **Angebot** | 1 alle zwei Wochen | was das Studio verkauft, schlicht gesagt, ohne Entschuldigung. Karussell oder Stories. |

Für jeden Platz angeben: das Thema, den konkreten Blickwinkel aus dem, was
diese Woche passiert ist, das Format und die Hook-Formel-Nummer aus
`../ig-reel/hooks.json`. Kein Thema, ein Blickwinkel. „Haarentfernung“ ist
kein Plan. „Die Kundin, die nach Sitzung eins Panik bekam, weil mehr Haare da
waren“ ist ein Reel.

`../ig-start/nicht-versprechen.md` gilt für jeden Blickwinkel. Kein Platz im
Plan verspricht etwas, das das Studio nicht halten kann.

## Wann gepostet wird

Posten, wenn die Kundinnen wach sind und nicht arbeiten. Für Kundinnen eines
Kosmetikstudios ist das meistens früher Abend, 18 bis 20 Uhr, und
Sonntagabend. Die Insights des Accounts sagen es genauer, wenn es ein
Unternehmenskonto ist.

Aber das klar sagen: **Die Uhrzeit zählt viel weniger als die ersten zwei
Sekunden.** Instagram zeigt ein Reel tagelang weiter, wenn es läuft, und
begräbt ein gut getimtes, das nicht läuft. Wenn die Nutzerin an Uhrzeiten
feilt, bevor ihre Hooks funktionieren, poliert sie das Falsche, und das sollte
man ihr sagen.

## Die Austausch-Runde, die nicht freiwillig ist

20 Minuten am Tag, vor dem Posten, nicht danach. Eine Liste mit 10 Accounts
bauen:

- **5 Reichweite**: Accounts mit einem Publikum, das die Nutzerin will, wo ein
  guter Kommentar gesehen wird. Lokale Accounts der Stadt, Friseurinnen,
  Fotografinnen, Stadtteil-Seiten. Früh kommentieren, bevor 200 andere da
  sind.
- **3 Kolleginnen**: gleiche Größe, gleiches Fach, andere Stadt. Die Gruppe,
  die zurückkommentiert.
- **2 Kundinnen**: Leute, die wirklich buchen könnten. Wochenlang
  kommentieren, bevor eine DM kommt, und nie in einem Kommentar werben.

Die Liste an `/ig-comment` übergeben.

## Ausgabe

```
WOCHE VOM 13. OKTOBER

MO  nur Austausch  (20 Min, Liste unten)
DI  18:30  REEL      BELEG      #3  Das sagt dir keiner   mehr Haare nach Sitzung 1
MI  nur Stories + Austausch
DO  18:00  KARUSSELL ERKLÄREN   Caption Aufgabe B         die 5 Dinge vor dem ersten Termin
FR  18:30  REEL      HALTUNG    #2  Hör auf damit         zupfen vor dem Termin
SA  -
SO  19:00  REEL      GESCHICHTE #25 Jemand anderes        die Kundin nach 15 Jahren Wachs

STORIES  jeden Tag 3 bis 5 Bilder, Fragen-Sticker am Donnerstag.

AUSTAUSCH  (5 Reichweite / 3 Kolleginnen / 2 Kundinnen)
  ...

Sag „schreib Dienstag“, und ich entwerfe es.
```

Den Plan nach `wochenplan.md` im Arbeitsordner schreiben, damit die anderen
Skills ihn lesen können. Nichts wird irgendwo geplant oder gepostet. Das ist
ein Plan, und die Nutzerin führt ihn aus.
