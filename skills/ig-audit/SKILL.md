---
name: ig-audit
description: >-
  Rückblick auf das, was das Studio schon gepostet hat: welche Reels wirklich
  funktioniert haben, warum, und was es nicht mehr machen sollte. Nutzen, wenn
  die Nutzerin ihre Instagram-Insights oder alte Beiträge einfügt und fragt
  "was läuft", "warum ist das gefloppt", "lies meine Zahlen", "schau dir meine
  Beiträge an", oder wissen will, wovon sie mehr machen soll.
---

# ig-audit

Die einzige ehrliche Quelle dafür, was für einen Account funktioniert, ist
dieser Account. Jede Regel in jedem Instagram-Ratgeber, auch die in diesem
Paket, ist eine Annahme. Die letzten 30 Beiträge der Nutzerin sind der Beleg.

## Eingabe

Nach dem fragen, was die Nutzerin hat:

- Insights je Beitrag: Aufrufe, Reichweite, Interaktionen, Wiedergabezeit,
  Speicherungen, Teilen, neue Follower, und der Anteil der Reichweite von
  Nicht-Followern. Screenshots reichen. Das gibt es nur bei einem
  Unternehmenskonto; bei einem privaten Konto zuerst umstellen lassen.
- Oder die Haltekurve ihrer besten und schlechtesten Reels der letzten Zeit.
  Dieser eine Screenshot ist mehr wert als alles andere zusammen.
- Oder nur die Beiträge und ihre Aufrufzahlen, das reicht für einen ersten
  Durchgang.

Außerdem `log.md` im Arbeitsordner lesen, falls vorhanden, denn dort steht,
welche Hook-Formel jeder Beitrag benutzt hat.

## Was wirklich gemessen wird

Rohe Aufrufe sind die am wenigsten nützliche Zahl auf der Seite, weil sie
vor allem davon abhängen, wie viele dem Account schon folgen. Stattdessen das
hier rechnen und die Rechnung zeigen:

| Kennzahl | wie | was sie sagt |
| --- | --- | --- |
| **Vielfaches** | Aufrufe geteilt durch den Normalwert des eigenen Accounts | ob das ein echter Treffer war oder ein normaler Tag |
| **Reichweite bei Fremden** | Prozent der Reichweite von Leuten, die nicht folgen | ob es überhaupt gereist ist |
| **Halten bei 3 s** | Zuschauer, die bei 3 s noch da sind, geteilt durch alle, die angefangen haben | ob der Hook funktioniert hat. Das ist die Note des Hooks. |
| **Mittlere Wiedergabezeit** | direkt aus den Insights | ob die Mitte funktioniert hat |
| **Teilen je Reichweite** | Teilen geteilt durch Reichweite | das stärkste Signal, das man bekommen kann. Teilen heißt, jemand setzt seinen Namen darunter. |
| **Follower je Reichweite** | neue Follower geteilt durch Reichweite | ob das Profil die Aufmerksamkeit umgewandelt hat |
| **Anfragen** | DMs, Kommentare mit Terminwunsch, Buchungen nach dem Beitrag | das, worum es bei einem Studio am Ende geht |

Nach Vielfachem und Teilen je Reichweite ordnen, nicht nach Aufrufen. Ein
Reel mit 4.000 Aufrufen und 90 Mal Teilen schlägt eines mit 60.000 Aufrufen
und 11.

## Dann das Muster finden

Mit den besten fünf und den schlechtesten fünf nebeneinander nach dem
suchen, was sie trennt, und bereit sein, etwas zu folgern, das die Nutzerin
nicht mag:

- **Halten bei 3 Sekunden.** Unterscheiden sich oben und unten hier, ist es
  der Hook und sonst nichts, und alles danach ist Ablenkung.
- **Hook-Formel.** Welche Nummern aus `../ig-reel/hooks.json` sind in den Top 5?
- **Format.** Reel, Karussell, einzelnes Bild.
- **Länge.** In Gruppen: unter 15 s, 15 bis 30 s, 30 bis 60 s, über 60 s.
- **Thema.** Beleg, Erklären, Haltung, Geschichte, Angebot.
- **Gesicht oder kein Gesicht.** Bei Studios oft der größte Unterschied.
- **Ob die Nutzerin in der ersten Stunde auf Kommentare geantwortet hat.**
- **Tag und Uhrzeit.** Das **zuletzt** prüfen und nur, wenn die anderen nichts
  zeigen. Es ist fast nie die Ursache, und es ist die Stelle, an der alle sie
  haben wollen.

Den Befund als Aussage mit Beleg formulieren und sagen, wie sicher er ist.
Mit 30 Beiträgen sieht man ein Muster. Mit 6 nicht, und das zu sagen ist
besser, als eines zu erfinden.

## Der Unterschied, der Monate spart

**Ein Reel mit Aufrufen und ohne neue Follower ist kein gescheitertes Reel,
es ist ein Profil-Problem.** Ein Reel ohne Aufrufe ist ein Hook-Problem. Beides
trennen, bevor irgendetwas empfohlen wird. Ist die Reichweite bei Fremden hoch
und Follower je Reichweite niedrig, aufhören, Hooks umzuschreiben, und zu
`/ig-profile` gehen.

Bei einem Studio gibt es eine dritte Stufe: **Follower, aber keine Anfragen.**
Dann fehlt im Profil die Tür (Link, Adresse, Stichwort) oder in den Beiträgen
die Aufforderung, und beides ist in einer Stunde behoben.

## Ausgabe

```
RÜCKBLICK  ·  31 Beiträge  ·  12. Juni bis 5. September  ·  Normalwert 1.100 Aufrufe

TOP 5 NACH VIELFACHEM
  18,2x  #3  Das sagt dir keiner   20.100 Aufrufe  62 % Fremde  Halten 3 s 71 %  128 Mal geteilt
   6,4x  #1  Das Lehrgeld           7.000 Aufrufe  48 % Fremde  Halten 3 s 64 %   71 Mal geteilt
  ...

UNTERE 5
   0,3x  #11 Nummeriert               330 Aufrufe   9 % Fremde  Halten 3 s 31 %    2 Mal geteilt
  ...

WAS DIE ZAHLEN SAGEN
1. Halten bei 3 Sekunden ist die ganze Geschichte. Top 5 im Schnitt 66 %, untere 5 33 %.
   Alles andere, worüber du dir Sorgen machst, hängt an den ersten zwei Sekunden.
2. Die Beiträge, in denen du selbst schlecht dastehst: im Schnitt 8,1x gegen 0,9x
   bei allen anderen. n=5. Stärkstes Signal hier, und es ist nicht knapp.
3. Produkt-Listen bekommen Aufrufe und sonst nichts. Hohe Reichweite, kein Teilen,
   keine Follower. Drei deiner unteren fünf.
4. Wochentag zeigt nichts. Dienstag und Freitag liegen im Rauschen. Nicht mehr daran drehen.

AUFHÖREN: Produkt-Listen.
MEHR DAVON: die mit einem Preis, den du bezahlt hast, und einer Zahl dran.
```

Dann die Schlüsse an `/ig-plan` übergeben, damit die nächste Woche auf den
eigenen Belegen der Nutzerin steht statt auf Standardwerten, und an
`/ig-viral`, damit die Ideen-Datei auf die Formeln gefiltert wird, die für
diesen Account funktionieren.
