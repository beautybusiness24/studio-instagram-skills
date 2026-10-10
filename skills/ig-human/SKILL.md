---
name: ig-human
description: >-
  Entfernt den Maschinen-Fingerabdruck aus jedem Entwurf (Gedankenstriche,
  KI-Floskeln, unsichtbare Zeichen, Studio-Phrasen wie "Wohlfühloase") und
  misst ihn mit fünf Prüfungen, bevor er rausgeht. Nutzen, wann immer ein Text
  menschlich klingen soll, wenn die Nutzerin "vermenschlichen", "klingt das
  nach KI", "Gedankenstriche raus", "klingt nach ChatGPT" sagt, oder bevor eine
  Caption, ein Skript, ein Kommentar, eine Antwort oder eine DM gezeigt wird.
---

# ig-human

Zwei Werkzeuge liegen in diesem Ordner und beide laufen wirklich. Benutze sie.
Nicht nach Gefühl.

```bash
python3 <skill-ordner>/humanize.py entwurf.txt --report     # bereinigen, zeigen, was sich geändert hat
python3 <skill-ordner>/detect.py entwurf.txt                  # messen, fünf Prüfungen
python3 <skill-ordner>/detect.py vorher.txt nachher.txt       # den Unterschied belegen
```

`<skill-ordner>` ist der Ordner dieses Skills, der Pfad steht oben beim Laden.
Unter Windows meist `python` statt `python3`. Ohne Python: `slop.json` lesen
und die Listen von Hand anwenden, Gedankenstriche von Hand ersetzen, und im
Ergebnis „von Hand bereinigt“ schreiben.

Beide lesen `slop.json`: deutsche Floskeln und Wendungen mit schlichten
Ersetzungen, 18 Klassen unsichtbarer Zeichen, typografische Ersetzungen und
Strukturmerkmale. Ein eigener Block ist für Kosmetikstudios: „Wohlfühloase“,
„Verwöhnmoment“, „Auszeit vom Alltag“, „du verdienst es“, und die
Versprechen, die kein Studio machen darf. Die Datei ist zum Bearbeiten
gedacht. Benutzt die Nutzerin ein Wort wirklich, das die Liste streicht, kommt
es raus.

## Warum das auf Instagram mehr zählt, als es aussieht

Captions sind kurz, und Skripte werden laut gesagt. Eine geschriebene Zeile in
einer Caption mit 600 Zeichen ist ein größerer Anteil des Textes als dieselbe
Zeile in einem Aufsatz, und ein Sprechtext, den niemand natürlich sagen
könnte, fällt beim ersten Take auf. Das Merkmal ist nicht ein Detektor, der
den Beitrag markiert. Das Merkmal ist eine Frau, die an etwas vorbeiscrollt,
das wie eine Marke klingt, oder eine Inhaberin, die über ihr eigenes Skript
stolpert.

## Was automatisch behoben wird

**1. Unsichtbare Zeichen.** Zero-Width-Zeichen, Word Joiner, weiche
Trennstriche, BOM, Unicode-Tag-Zeichen, geschützte und schmale Leerzeichen.
Eine Tastatur erzeugt die nicht. Sie überleben Kopieren und Einfügen, sind in
jedem Editor unsichtbar und sind das mechanischste Merkmal in generiertem
Text. `humanize.py` löscht jedes einzelne.

**2. Typografie.** Gedankenstrich zu Komma oder Punkt, englische
Anführungszeichen zu geraden, Auslassungszeichen zu drei Punkten,
Aufzählungspunkt zu Bindestrich. Deutsche Anführungszeichen („ “) bleiben,
die gehören zur Sprache. Der Gedankenstrich-Durchgang ist der wichtige: Er
macht den Strich zum Komma und räumt danach die doppelten Satzzeichen auf.

**3. Die Floskel-Liste.** eintauchen, nahtlos, entscheidend, revolutionär,
ganzheitlich, Game-Changer, „in der heutigen schnelllebigen Welt“, „lass uns
gemeinsam“, plus der Instagram-Block: „hör auf zu scrollen“, „in diesem
Video“, „folge mir für mehr“, „markiere eine Freundin“, plus der
Studio-Block. Einzelne Wörter werden ersetzt oder gelöscht. Eine
Mehrwort-Wendung ohne Ersatz wird nur gelöscht, wenn sie fast den ganzen Satz
ausmacht; steckt sie mitten in einem Satz, bleibt der Satz stehen und wird
zum Umschreiben gemeldet, weil ein halbierter Satz schlimmer liest als die
Floskel.

## Was NICHT automatisch behoben wird

Strukturmerkmale werden **gemeldet, nicht umgeschrieben**, weil die Form
eines Satzes zu ändern Urteil braucht:

- „Nicht nur X, sondern auch Y“ und „Es geht nicht um X, es geht um Y“
- Dreier-Aufzählungen
- Ein-Wort-Fragen als eigene Zeile: „Das Ergebnis?“
- Die Video-Vorrede: „In diesem Video zeige ich euch“
- Emoji als Aufzählungszeichen
- Drei oder mehr geschriene Wörter hintereinander
- Hashtag-Wände
- Reflex-Köder: „folge für mehr“, „markiere jemanden“, „doppeltipp“
- „Du verdienst es“ und die Wohlfühl-Floskeln
- Floskeln mitten im Satz, mit dem Satz, der neu geschrieben werden muss

Diese Liste ist deine Aufgabe. Jede gemeldete Zeile von Hand umschreiben, mit
derselben Bedeutung, dann `detect.py` noch einmal laufen lassen. Das ist der
Teil, der den Wert von DURCHSEHEN auf BESTANDEN hebt, und der Teil, den ein
Skript nicht kann.

## Die fünf Prüfungen

`detect.py` misst fünf Signale von 0 bis 100, höher ist menschlicher:

| Prüfung | was gemessen wird | so sieht Maschine aus |
| --- | --- | --- |
| STREUUNG | Schwankung der Satzlänge | jeder Satz gleich lang |
| KONKRET | Zahlen, Preise, Zeiten je 100 Wörter | abstrakte Begriffe, keine Zahlen |
| FLOSKELN | Treffer aus der Liste je 100 Wörter | Standard-Vokabular |
| FINGERABDRUCK | unsichtbare Zeichen, Gedankenstriche, englische Anführungszeichen je 1.000 Zeichen | typografisch perfekt |
| STIMME | Umgangssprache, Ansprache, Strukturmerkmale | keine Umgangssprache, inszenierte Enthüllungen |

Das Urteil gewichtet den Mittelwert mit 60 Prozent und die **schwächste
einzelne Prüfung** mit 40 Prozent, weil ein Signal reicht. BESTANDEN braucht
insgesamt 70 und keine Prüfung unter 55.

Im Deutschen werden alle Substantive großgeschrieben, deshalb zählen hier nur
Zahlen, Preise und Zeitangaben als konkret. Statt englischer Kurzformen zählen
umgangssprachliche Marker: hab, gibt's, mal, halt, echt, kriegst.

## Das ehrlich sagen

Das sind fünf lokale Prüfungen, angelehnt an die Signale, auf die
öffentliche Detektoren achten. Sie laufen vollständig auf dem Rechner der
Nutzerin, nichts wird hochgeladen. Sie sind **nicht** GPTZero, Originality,
Copyleaks oder Turnitin, sie rufen diese Dienste nicht auf und können deren
Urteil nicht versprechen. Was sie messen zu beheben, bewegt meist auch jene
Zahlen, weil es dieselben zugrunde liegenden Dinge sind. Das ist die Aussage.
Keine größere im Namen der Nutzerin machen, und keiner Nutzerin sagen, ihr
Text sei nicht erkennbar.

## Reihenfolge

1. `humanize.py entwurf.txt -o sauber.txt --report`
2. Die Strukturmeldungen lesen. Diese Zeilen selbst umschreiben.
3. `detect.py entwurf.txt sauber.txt`, um vorher und nachher zu zeigen.
4. Ist das Urteil nicht BESTANDEN, die schwächste genannte Prüfung beheben und
   noch einmal. Zwei Runden sind normal. Fünf heißt, der Entwurf wurde nach
   Schema geschrieben, und die Lösung ist ein anderer Entwurf, nicht mehr
   Durchgänge.
5. Der Nutzerin den bereinigten Text und den Wert zeigen. Nie den Wert allein.
