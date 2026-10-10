---
name: ig-caption
description: >-
  Schreibt die Instagram-Caption: die Zeile, die vor dem "... mehr" überlebt,
  den Text, die eine Aufforderung, die Suchbegriffe und bis zu fünf Hashtags,
  und prüft sie, bevor sie rausgeht. Nutzen, wenn die Nutzerin sagt "schreib
  die Caption", "Text unter das Reel", "was schreibe ich drunter", ein Reel
  oder Karussell fertig hat und den Text braucht, oder nach Hashtags fragt.
---

# ig-caption

Ein Werkzeug liegt in diesem Ordner und läuft:

```bash
python3 <skill-ordner>/caption.py caption.txt
python3 <skill-ordner>/caption.py caption.txt --keywords "dauerhafte haarentfernung berlin,laser achseln"
```

`<skill-ordner>` ist der Ordner dieses Skills, der Pfad steht oben beim Laden.
Unter Windows meist `python` statt `python3`. Ohne Python: die ersten 125
Zeichen von Hand abzählen und zeigen, Hashtags zählen, Aufforderungen zählen,
und sagen, dass es von Hand war.

Es zeigt die Caption so, wie der Feed sie zeigt: die ersten 125 Zeichen in
einem Kasten, alles andere hinter dem Tipp. Diesen Kasten lesen, bevor
irgendetwas anderes gelesen wird.

## Zuerst: Welche Aufgabe hat diese Caption?

Diese Entscheidung ruiniert Captions, wenn sie übersprungen wird.

**Aufgabe A: Das Video hat schon gepackt.** Ein Reel trägt seinen Hook in den
ersten zwei Sekunden, gesprochen und im Bild. Die Caption ist kein zweiter
Hook, und mit dem Video zu konkurrieren ist der Weg, beides zu verlieren. Ihre
Aufgabe ist die Aufforderung, der Zusammenhang, der die Aufforderung sinnvoll
macht, und die Wörter, nach denen gesucht wird.

**Aufgabe B: Die Caption ist der Inhalt.** Ein Foto, ein einzelnes Bild, ein
Karussell-Cover, das eine Frage aufmacht. Hier ist Zeile eins der Hook und
funktioniert genau wie ein Reel-Hook: konkret, kurz, und an einer Klippe
abgeschnitten statt mitten im Nebensatz.

Fragen, welche geschrieben wird. Hat die Nutzerin ein Reel mit starkem Hook,
A schreiben und sagen, warum.

## Die Form

```
Zeile 1     125 Zeichen sichtbarer Platz. Aufgabe A: die Aufforderung, klar.
            Aufgabe B: der Hook.
            Nie eine Begrüßung, nie ein Hashtag, nie ein Emoji als erstes Zeichen.
Text        kurze Absätze, eine Leerzeile dazwischen. Zwei bis sechs. Hier
            wohnen die Suchbegriffe und die Behandlung mit Stadt.
Aufforderung eine. Ein Stichwort kommentieren, speichern, Termin buchen oder
            DM. Eine.
Hashtags    bis zu fünf, in einer eigenen Zeile ganz unten, oder keine.
```

Das Limit sind 2.200 Zeichen, und fast nichts braucht 2.200. Eine Caption,
die den Tipp verdient und dann 600 Zeichen liefert, schlägt eine mit 1.800.

## Hashtags, ehrlich

Hashtags bringen keine Reichweite mehr, und Instagram hat das mit einer
Produktänderung bestätigt: **Seit dem 18. Dezember 2025 sind höchstens fünf
Hashtags je Beitrag erlaubt**, vorher dreißig. Begründung von Instagram:
wenige, passende Hashtags statt vieler allgemeiner. Schon im Februar 2025
hatte Instagram-Chef Adam Mosseri gesagt, Hashtags seien ein Etikett, kein
Hebel für Reichweite.

Also: bis zu fünf, konkret, als Themen-Etikett. Wenn die Nutzerin einen Block
mit zwanzig in ihrer Notizen-App hat, ist der Block jetzt toter Ballast, und
die Prüfung lässt ihn durchfallen.

`#viral`, `#fyp`, `#explorepage`, `#beauty`, `#love` beschreiben nichts.
Streichen. `#dauerhaftehaarentfernungberlin` beschreibt etwas.

## Suchbegriffe zählen jetzt mehr als Hashtags

Die Instagram-Suche liest den Caption-Text. Also gehört der Begriff, für den
die Nutzerin gefunden werden will, als Wortfolge in die Caption, so wie ein
Mensch ihn tippen würde, in einem Satz, der normal klingt. „Dauerhafte
Haarentfernung in Berlin“ als Wörter in Zeile drei, nicht
„#dauerhaftehaarentfernung“ in einem Block unten. Die Behandlung und die
Stadt stehen im Studio-Profil.

Zwei oder drei solcher Begriffe erfragen oder aus `studio-profil.md` nehmen,
dann an die Prüfung übergeben:

```bash
python3 <skill-ordner>/caption.py entwurf.txt --keywords "dauerhafte haarentfernung berlin,laser achseln"
```

## Regeln

- **Kein Link in der Caption.** Captions sind nicht klickbar. Eine Adresse im
  Text ist toter Text, der sagt „ich benutze diese Plattform nicht“. In die
  Bio oder in die DM.
- **Eine Aufforderung.** Zwei Aufforderungen sind so viel wie keine.
  `caption.py` zählt sie.
- **Keine erfundene Aufforderung.** Die Aufforderung der Caption ist die
  aus dem Video. Hat das Video keine (kein Stichwort, kein „speicher dir
  das“), keine erfinden, kein „schreib mir X in die DMs“, das ins Leere
  führt. Stattdessen eine **offene Frage zum Thema**, die zum Kommentieren
  einlädt: „Wie lange hast du gewachst, bevor du umgestiegen bist?“ Echte
  Kommentare sind mehr wert als ein Trichter ohne Grund.
- **Das Stichwort muss tippbar sein.** Ein Wort, keine Leerzeichen, kein
  Emoji, und im Video auch laut gesagt. `Schreib ZWEIFEL in die Kommentare`
  funktioniert. `Schreib „den Zettel für zwischendurch“` nicht.
- **Den ersten Kommentar getrennt schreiben**, wenn ein Link nötig ist. Das im
  Ergebnis sagen.
- **Emoji als Satzzeichen, nicht als Dekoration.** Die Prüfung meldet alles
  über 4 je 100 Zeichen. Das Studio-Profil sagt, ob die Inhaberin überhaupt
  welche benutzt.
- **Alt-Text ist 20 Sekunden wert.** Für Karussells und Fotos schreiben. Er
  wird von Vorlese-Programmen und von Instagram gelesen.
- **`../ig-start/nicht-versprechen.md` gilt auch hier.** Keine Garantie, kein
  „für immer“, kein „schmerzfrei“.

## Der Ablauf

1. Aufgabe A oder B entscheiden und sagen, welche.
2. Entwerfen, in der Stimme aus `studio-profil.md`. Fehlt die Datei,
   `/ig-start` vorschlagen.
3. `/ig-human` darüber laufen lassen. Captions sind kurz, also fällt jede
   Floskel hier lauter auf als irgendwo sonst im Paket.
4. `caption.py` mit den Suchbegriffen der Nutzerin laufen lassen. Jeden
   FEHLER beheben. Über jedes PRÜFEN laut entscheiden statt stumm.
5. Den kopierfertigen Block ausgeben, dann die Quittung:

```
CAPTION FERTIG
Aufgabe:    A, das Reel trägt den Hook
Sichtbar:   118 von 125 Zeichen vor der Kürzung genutzt
Aufforderung: eine, ZWEIFEL kommentieren
Hashtags:   3
Suche:      „dauerhafte Haarentfernung Berlin“ in Zeile 3, „Laser Achseln“ in Zeile 5
Prüfung:    FERTIG
```

6. Bei „ja“ die Caption unter das zugehörige Skript in `reels/` anhängen,
   damit beides zusammen liegt.

Nichts wird gepostet. Die Nutzerin kopiert es.

## Lernen

`lernen.md` im Arbeitsordner vor dem Schreiben lesen und beachten. Korrigiert
die Nutzerin etwas, das über ihren Geschmack sagt („würde ich nie sagen“, „zu
werblich“, „genau so“), danach eine Zeile mit Datum in `lernen.md` eintragen
und kurz sagen: „Hab ich mir gemerkt.“
