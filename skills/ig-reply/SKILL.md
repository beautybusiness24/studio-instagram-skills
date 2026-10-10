---
name: ig-reply
description: >-
  Kümmert sich um die Kommentare unter den eigenen Reels und Beiträgen des
  Studios: sortiert sie danach, welche eine Antwort wert sind, und entwirft
  die Antworten. Nutzen, wenn die Nutzerin ihre Kommentare einfügt, "antworte
  darauf", "beantworte meine Kommentare", "jemand hat X unter mein Reel
  geschrieben" sagt, oder mit einer Kritikerin, einem Hater oder einer
  Interessentin in den Kommentaren zu tun hat.
---

# ig-reply

Die Kommentarspalte unter dem eigenen Beitrag ist der Ort, an dem Reichweite
entschieden wird. Jede Antwort ist eine weitere Interaktion auf dem Beitrag,
Antworten in der ersten Stunde leisten den größten Teil der Arbeit, und auf
Instagram kann eine Antwort auch ein Reel sein, der am wenigsten genutzte Zug
auf der Plattform.

## Mit Zernio: Kommentare direkt holen und beantworten

Ist Zernio verbunden (`/ig-verbinden`), muss die Nutzerin nichts einfügen:
die Kommentare des neuesten Beitrags (oder des genannten) mit
`comments_list_inbox_comments` bzw. `comments_get_inbox_post_comments` holen,
sortieren und Antworten entwerfen wie unten. Dann **jede Antwort zeigen und
einzeln oder als Block bestätigen lassen** („Diese 6 Antworten so senden?“).
Erst nach Ja mit `comments_reply_to_inbox_post` senden. Ausblenden oder
löschen nur auf ausdrücklichen Wunsch zu genau diesem Kommentar.

Ohne Zernio: Die Nutzerin fügt die Kommentare ein und kopiert die Antworten
selbst zurück.


Aber der Wert ist nicht bei allen Kommentaren gleich, also sortiert dieser
Skill, bevor er schreibt.

## Eingabe

Die Nutzerin fügt die Kommentare ein, am besten mit Handles. Screenshots
reichen. Die Kommentarspalte nicht mit einem Browser-Werkzeug abgreifen.

`studio-profil.md` lesen für Stimme, Stichwort und das, was das Stichwort
liefert. `../ig-start/nicht-versprechen.md` gilt auch in Antworten, gerade
bei Fragen zu Schmerz, Ergebnis und Dauer.

## Zuerst sortieren

Jeden Kommentar in einen von sechs Körben legen und die Zahlen laut sagen:

| Korb | was es ist | was es bekommt |
| --- | --- | --- |
| **STICHWORT** | das Wort, um das du gebeten hast | das versprochene Ding, von Hand oder über dein zugelassenes Werkzeug geschickt |
| **INTERESSENTIN** | jemand beschreibt das Problem, das du löst, oder fragt nach Preis oder Termin | eine echte Antwort öffentlich, dann eine Tür |
| **SUBSTANZ** | ergänzt, widerspricht, denkt weiter | die längste Antwort im Thread |
| **FRAGE** | eine Frage, die viele haben | die wird ein Reel, nicht nur eine Antwort |
| **ZUSPRUCH** | „🔥“, „toll“, eine Markierung | ein Like, und höchstens 3 bis 8 Wörter |
| **RAUSCHEN** | Werbung, Spam, Bösartiges, Köder | nichts, oder eine Zeile und raus |

In dieser Reihenfolge schreiben und aufhören, wenn der Wert aufhört.

## Der Zug, den die meisten übersehen

Ist eine Frage in den Kommentaren eine, die dreißig andere auch haben,
**mit einem Reel darauf antworten**. Instagram heftet den Kommentar als
Sticker an das neue Video, die Person, die gefragt hat, wird benachrichtigt,
und eine Frage mit echter Nachfrage wird ein Beitrag, dessen Hook schon
geschrieben ist. Jede FRAGE, die das erfüllt, markieren und an `/ig-reel`
als Formel #16 geben.

## Wie antworten

- **Die tatsächliche Frage beantworten.** Fragt jemand wie, dann sagen wie, in
  der Antwort. Nicht in die DMs schicken für eine Antwort, die man hätte
  haben können. Ausnahme: Preise, wenn die Nutzerin sie nicht öffentlich
  nennen will, dann „schreib mir, dann schick ich dir die Liste“.
- **Den Namen einmal nennen**, am Anfang, ohne Ausrufezeichen.
- **Die Länge angleichen.** Ein Vier-Wort-Kommentar bekommt keine vier Zeilen.
- **Bei Kritik:** zuerst den wahren Teil zugeben, in ihren Worten, dann die
  Linie halten. Nie löschen, nie verteidigen, nie zweimal im selben Thread.
- **Bei einer Kundin, die unzufrieden war:** öffentlich ernst nehmen, in einem
  Satz, und ins Gespräch holen: „Ruf mich an oder schreib mir, ich schau mir
  das an.“ Keine Diskussion über ihre Haut in der Kommentarspalte.
- **Bei einem Hater:** nichts. Eine Antwort ist Reichweite, und Reichweite ist
  das, wofür er gekommen ist. Den Kommentar ausblenden, wenn er beleidigend
  ist. Die Kommentar-Einstellungen von Instagram gibt es dafür, und sie zu
  nutzen ist kein Verlieren.
- **Bei einer Interessentin:** vollständig öffentlich antworten. Die Tür ist
  ein Satz am Ende, und sie ist ein Hilfsangebot, keine Werbung. Die
  öffentliche Antwort ist das, was die nächste Person zum Schreiben bringt.
- **Bei medizinischen Fragen** (Medikamente, Schwangerschaft, Hauterkrankung):
  nicht in der Kommentarspalte beantworten. „Das klären wir vor dem ersten
  Termin im Gespräch“ und an die Hautärztin verweisen, wenn es eine
  Diagnose braucht.

## Stichwort-Kommentare

Hat der Beitrag um ein Stichwort gebeten, sind diese Kommentare der ganze
Zweck des Beitrags. Jeder davon ist eine Person, die die Hand gehoben hat.
Jeder antworten, dann das Versprochene schicken. Hat die Nutzerin eine
Automatisierung über Instagrams eigene Werkzeuge oder einen zugelassenen
Partner, das sagen und laufen lassen; wenn nicht, sind die Antworten von Hand,
und das ist bei dieser Menge in Ordnung. Nie Leute in Menge anschreiben, die
nicht kommentiert haben.

## Ausgabe

Ein Block, nach Körben gruppiert, jede Antwort kopierfertig und schon durch
`/ig-human`:

```
ANTWORTEN  ·  84 Kommentare  ·  41 STICHWORT, 2 INTERESSENTIN, 3 SUBSTANZ, 2 FRAGE, 34 ZUSPRUCH, 2 RAUSCHEN

STICHWORT  (41)  den Zettel schicken. Eine Zeile je Person, gleiche Wärme, kein Kopieren.

INTERESSENTIN
@handle - „genau das ist mir im Juni passiert, dachte ich mach was falsch“
> Machst du nicht. Nach Sitzung eins sieht es bei fast allen so aus, die
> schlafenden Haare kommen jetzt nach. Wenn du magst, schreib mir, wo du
> gerade stehst, dann sag ich dir, wann die nächste Sitzung Sinn macht.

FRAGE -> REEL
@handle - „und was, wenn ich zwischendurch in die Sonne muss?“
  34 Likes auf diesem Kommentar. Das ist ein Reel, keine Antwort. Formel #16.

RAUSCHEN  (2)  übersprungen. Antworten gibt ihnen Reichweite.
```

Dann die Schranke: Nichts wird gepostet, bis die Nutzerin ja sagt. Sie fügt
die Antworten ein.

## Lernen

`lernen.md` im Arbeitsordner vor dem Schreiben lesen und beachten. Korrigiert
die Nutzerin etwas, das über ihren Geschmack sagt („würde ich nie sagen“, „zu
werblich“, „genau so“), danach eine Zeile mit Datum in `lernen.md` eintragen
und kurz sagen: „Hab ich mir gemerkt.“
