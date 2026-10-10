---
name: ig-reel
description: >-
  Schreibt ein Instagram-Reel aus einer rohen Idee: drei Hook-Vorschläge aus 26
  Formeln, bewertet, dann das gesprochene Skript, der Text im Bild und ein
  Zeitplan pro Satz, in der Stimme des Studios. Nutzen, wenn die Nutzerin ein
  Reel, ein kurzes Videoskript, einen Hook oder einen Sprechtext will, "mach
  ein Reel über X", "was soll ich in dem Video sagen", oder gleich drehen will
  und noch keinen ersten Satz hat.
---

# ig-reel

Macht aus einer Idee ein Reel, das jemand bis zum Ende schaut.

In diesem Ordner liegen zwei Werkzeuge, und beide laufen wirklich. Benutze
sie. Den Hook nicht nach Gefühl beurteilen, die Länge nicht schätzen.

```bash
python3 <skill-ordner>/hookscore.py hooks.txt           # Hook-Vorschläge ordnen
python3 <skill-ordner>/hookscore.py --hook "eine Zeile"  # einen einzelnen bewerten
python3 <skill-ordner>/beats.py skript.txt --target 30   # Zeitplan vor dem Dreh
```

`<skill-ordner>` ist der Ordner dieses Skills, der Pfad steht oben beim Laden.
Immer mit vollem Pfad aufrufen. Unter Windows heißt der Befehl meist `python`
statt `python3`. Wenn kein Python da ist: einmal sagen, die fünf Kriterien
(Länge, konkret, Einsatz, vorne, Ansprache) von Hand durchgehen und im
Ergebnis „von Hand bewertet“ schreiben.

## Vor dem Schreiben

1. `studio-profil.md` im Arbeitsordner lesen. Das ist die Stimme des Studios:
   wie die Inhaberin spricht, was sie nie sagt, wen sie anspricht, was sie
   belegen kann. Fehlt die Datei, `/ig-start` vorschlagen und nicht ohne sie
   schreiben. Ein Skript in der falschen Stimme ist unbrauchbar, weil sie es
   laut sagen muss.
2. `hooks.json` in diesem Ordner lesen. 26 Formeln, jede mit Vorlage,
   Beispiel aus dem Studio, Bild-Version, Einsatzzweck und der Art, wie sie
   kaputtgeht.
3. `../ig-start/nicht-versprechen.md` lesen. Kein Skript verlässt diesen
   Skill mit „für immer“, „garantiert“, „schmerzfrei“ oder einer Heilung.
4. Wenn die Idee dünn ist, nicht auffüllen. Eine gebündelte Frage stellen: Was
   ist passiert, wem, und was hat es gekostet oder gebracht? Ein Reel braucht
   eine konkrete wahre Sache. Die holen, bevor geschrieben wird.
5. Liegt `ideen.md` im Arbeitsordner, lesen. `/ig-viral` schreibt sie, und sie
   ist der eigene Beleg der Nutzerin, welche Formeln in ihrer Nische gerade
   laufen. Sie schlägt die Standardwerte in dieser Datei.

## Die Form

Ein Reel wird in den ersten zwei Sekunden entschieden und in den nächsten
fünf gehalten.

```
0:00 - 0:02   HOOK         die Behauptung. Gesprochene Zeile und Bild-Zeile,
                           getrennt geschrieben. Bewegung im ersten Bild,
                           kein stehendes Gesicht.
0:02 - 0:07   DER EINSATZ  warum das die Zuschauerin betrifft. Ein Satz.
0:07 - ...    DER KERN     ein Gedanke je Beat, und das Bild wechselt je Beat.
LETZTE 3 s    DIE EINLÖSUNG liefern, was der Hook versprochen hat, dann die
                           eine Aufforderung.
LETZTE ZEILE  DIE SCHLEIFE ein Wort aus dem Hook wiederholen, damit die
                           Wiederholung sauber einrastet.
```

Länge: 15 bis 45 Sekunden ist der Arbeitsbereich. Für ein Studio-Reel sind
25 bis 35 Sekunden meistens richtig. Unter 7 Sekunden steigen die
Wiederholungen und sonst nichts.

## Der Ablauf

**1. Drei Hooks, nicht einen.** Die Idee durch `hooks.json` laufen lassen,
drei Formeln wählen, die wirklich passen, und für jede die gesprochene Zeile
plus die Bild-Zeile schreiben. Drei verschiedene Formeln, nicht drei Fassungen
derselben.

**2. Bewerten.** Die drei gesprochenen Zeilen in eine Datei, eine je Zeile,
und `hookscore.py` laufen lassen. Der Nutzerin die Rangliste zeigen. Liegt
der oberste unter 50, ist der Hook noch nicht da, und kein Feilen ändert das.

**3. Das Skript schreiben** auf dem besten Hook. Gesprochenes Deutsch, so wie
die Inhaberin wirklich redet. Kurze Sätze. Kein Satz, den sie üben müsste.
Eine Zeile je Beat, damit `beats.py` damit arbeiten kann.

**4. Zeit nehmen.** `beats.py skript.txt --target {Länge}` laufen lassen, mit
dem Sprechtempo aus dem Studio-Profil (`--wpm`), wenn eines drinsteht. Jede
Meldung beheben: ein Hook über 3 Sekunden, ein Beat über 4 Sekunden, drei
Zeilen ohne etwas Konkretes, keine Schleife. Wiederholen, bis es sauber ist.

**5. Vermenschlichen.** Das Skript durch `/ig-human` schicken, bevor es gezeigt
wird. Eine geschriebene Zeile fällt auf, sobald jemand sie laut sagt.

**6. Den Block ausgeben.** Das Skript als Codeblock, der Bild-Text als eigene
Liste mit Zeiten, dann:

```
REEL FERTIG
Hook:        #3 Das sagt dir keiner, Wertung 78 STARK
Länge:       28,4 s über 8 Beats bei 150 Wörtern/Min
Im Bild:     6 Karten
Humanizer:   3 Artefakte entfernt, Mensch-Wert 81 BESTANDEN
Caption:     als Nächstes /ig-caption

Sag „ja“, dann speichere ich es, oder sag mir, was anders soll.
```

**7. Nie posten.** Dieser Skill erzeugt ein Skript. Die Nutzerin dreht es und
postet es. Bei „ja“: Skript und Bild-Text in `reels/JJJJ-MM-TT-<kurzname>.md`
speichern und in `log.md` eine Zeile anhängen mit Datum, Hook-Formel und
erster Zeile, damit `/ig-audit` später eine Geschichte hat.

## Der Bild-Text ist ein eigenes Skript

Jedes Mal getrennt schreiben. Er wird gelesen, bevor er gehört wird.

- **Höchstens sechs Wörter je Karte.** Jemand liest das auf Armlänge, ohne
  Ton, bevor er zuhört.
- **Die Hook-Karte steht ab Bild 1**, nicht nach einer Sekunde Stille.
- **Im sicheren Bereich bleiben.** Auf 1080 x 1920 nichts über y=230 und
  nichts unter y=1440, und die rechten 230 Pixel frei lassen. Dort liegen
  Caption, Knöpfe und Tonleiste drüber.
- **Den Hook nie dorthin, wo die Caption sitzt.** Das ist unten, und es ist
  verdeckt.
- **Untertitel für den Kern einbrennen.** Die meisten schauen zuerst ohne Ton.
  In CapCut geht das mit automatischen Untertiteln.

## Regeln, die den Unterschied machen

- **Ein Gedanke je Reel.** Hat das Skript zwei, sind es zwei Reels. Das sagen.
- **Zahlen statt Adjektive.** „6 Sitzungen“ schlägt „ein paar“. Hat die
  Nutzerin keine Zahl genannt, danach fragen, statt um das Loch herum zu
  schreiben.
- **Die Einleitung streichen.** Keine Begrüßung, kein „in diesem Video“, kein
  Name, kein Logo. Das Video beginnt beim Satz, den man sonst in Sekunde
  sechs erreicht.
- **Das Bild je Beat wechseln.** Acht Sekunden dieselbe Einstellung ist die
  Stelle, an der Leute gehen, und `beats.py` meldet es. Im Studio geht das
  einfach: Gerät, Hände, Liege, Spiegel, Tür.
- **Eine Aufforderung am Ende.** Ein Stichwort kommentieren, speichern oder
  folgen. Eine.
- **Nichts erfinden.** Keine erfundenen Zahlen, Kundinnen, Ergebnisse oder
  Zitate unter dem Namen der Nutzerin, auch nicht als Platzhalter. Fehlt
  eine Zahl, `{{deine Zahl}}` ins Skript setzen und es sagen.
- **Keine Versprechen aus `nicht-versprechen.md`.** Fällt eins auf, umformulieren
  und in einer Zeile sagen, warum.
- **Kein Skript um einen Trend-Ton bauen, den die Nutzerin nicht nutzen kann.**
  Wenn die Idee ihre eigene Stimme braucht, das sagen.

## Beispiel

```
/ig-reel Kundin hat nach der ersten Sitzung Panik bekommen, weil mehr Haare da waren
```

```
HOOKS  (bewertet)
  78  STARK  #3  Das sagt dir keiner  „Keiner sagt dir, dass nach Sitzung eins erstmal 20 Prozent mehr Haare da sind.“
                                      im Bild: MEHR HAARE NACH SITZUNG 1
  74  STARK  #16 Original-Frage       „Lena, es ist schlimmer geworden. Die Nachricht kriege ich jede Woche.“
                                      im Bild: „ES IST SCHLIMMER GEWORDEN“
  61  OK     #7  Falsch, nicht deine  „Du gibst nach Sitzung eins auf, und es ist nicht deine Schuld.“
                                      im Bild: NICHT DEINE SCHULD

Gedreht wird #3: Die Zahl ist deine, der Satz liest sich im Bild in einem
Blick, und er beantwortet die Frage, die deine Kundin wirklich hatte.
```
