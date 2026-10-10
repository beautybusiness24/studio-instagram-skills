---
name: ig-viral
description: >-
  Findet heraus, welche Reels in der Nische des Studios gerade wirklich laufen,
  ordnet sie danach, wie weit jedes über dem Normalwert seines eigenen
  Accounts lag, benennt die Hook-Formel und macht daraus eine Ideen-Datei, aus
  der gedreht werden kann. Nutzen, wenn die Nutzerin sagt "was läuft gerade",
  "finde virale Videos", "was posten andere Studios", "Ideen sammeln",
  "warum läuft dieses Reel so gut", Reel-Links einfügt, oder fragt, was sie
  als Nächstes machen soll und keine Belege dafür hat.
---

# ig-viral

Der Recherche-Skill. Alles andere in diesem Paket schreibt; dieser schaut
nach. Einmal im Monat laufen lassen, nicht täglich. Formeln halten eine
Saison.

Ein Werkzeug liegt in diesem Ordner und läuft:

```bash
python3 <skill-ordner>/swipe.py gesammelt.tsv --out ideen.md
```

`<skill-ordner>` ist der Ordner dieses Skills, der Pfad steht oben beim Laden.
Unter Windows meist `python` statt `python3`. Ohne Python: das Vielfache von
Hand rechnen (Aufrufe geteilt durch Normalwert), die Formel aus
`../ig-reel/hooks.json` von Hand zuordnen, und das sagen.

## Der eine Gedanke, der das Ganze lohnt

**Rohe Aufrufe sind kein Beleg.** Ein Account mit zwei Millionen Followern und
400.000 Aufrufen hatte einen ruhigen Dienstag. Ein Studio mit 4.000 Followern
und 40.000 Aufrufen hat etwas gefunden, und das lässt sich nachbauen.

Deshalb ordnet hier alles nach dem **Vielfachen**: Aufrufe geteilt durch den
üblichen Wert dieses Accounts. Alles über 3x ist ein Signal. Alles unter 1,5x
ist der normale Tag dieses Accounts und lehrt nichts, egal wie groß die Zahl
aussieht.

Accounts sammeln, die **etwa in der zehnfachen Größe des eigenen** liegen.
Eine Formel, die bei 2 Millionen Followern läuft, läuft oft, weil es
2 Millionen Follower sind.

## Schritt 1: Accounts auswählen

Die Nutzerin um 6 bis 12 Accounts bitten oder welche vorschlagen und
freigeben lassen:

- **4 direkte**: gleiche Behandlung, gleiche Art Studio, etwas weiter.
  Studios aus anderen Städten sind hier besser als die Konkurrenz um die Ecke,
  weil man sich bei denen nichts wegnimmt.
- **4 benachbarte**: andere Behandlung, dieselbe Kundin. Friseurinnen,
  Nagelstudios, Hautärztinnen auf Instagram. Von dort kommen die Formate,
  bevor sie jemand in der eigenen Nische hat.
- **2 bis 4 große**: viel größere Accounts, nur für die Form, nie für Takt
  oder Ton.

Außerdem: die eigene **Gespeichert-Sammlung** öffnen lassen. Das ist die
schnellste und passendste Sammlung, die es gibt, und sie ist schon nach dem
Geschmack der Nutzerin gefiltert.

## Schritt 2: Hinschauen

**Der einfache Weg, den die meisten nehmen:** Die Nutzerin fügt 5 bis 15
Reel-Links oder Captions ein, die ihr aufgefallen sind, und schreibt zu jedem
dazu, was sie sich gemerkt hat: Account, ungefähr wie viele Follower, Aufrufe
des Reels, und die erste Zeile. Daraus baut dieser Skill die Tabelle. Den
Normalwert (die mittleren Aufrufe der letzten 12 Reels dieses Accounts)
schätzt sie beim Durchscrollen des Profils, das dauert eine Minute je Account.

**Der gründliche Weg:** Mit dem Browser-Werkzeug dieser Sitzung (eingebauter
Browser, Browser-Erweiterung oder Bildschirmsteuerung) die Profile gemeinsam
mit der Nutzerin durchsehen. Es gibt keine Schnittstelle dafür, und es braucht
keine, weil die Menge klein genug zum Lesen ist.

**Regeln, über die nicht verhandelt wird:**

- **Nie bei Instagram einloggen und nie nach einem Passwort fragen.** Wenn
  eine Seite eine Anmeldung braucht, ist die Nutzerin diejenige, die schon
  angemeldet ist. Ihren Browser mit ihr zusammen bedienen, oder sie einfügen
  lassen.
- **Das ist Lesen, nicht Abgreifen.** Zehn Accounts, ein Dutzend Reels je
  Account, in Menschentempo. Automatisches Sammeln in Menge verstößt gegen
  die Nutzungsbedingungen von Instagram und führt zur Sperre. Keinen
  Crawler bauen, keinen Dienst dafür nutzen, nichts im Hintergrund laufen
  lassen.
- **Die Formel kopieren, nie das Video.** Die Form des Hooks, den Aufbau, die
  Länge, das Muster der Schnitte. Nicht den Text, nicht die Stimme, nicht den
  Schnitt. Jede Zeile in der Ideen-Datei dem Account zuordnen, von dem sie
  kommt.

**Was je Reel festgehalten wird**, in den Worten der Macherin:

| Spalte | Hinweis |
| --- | --- |
| account | Handle |
| follower | vom Profil |
| median | die letzten 12 Reels überfliegen, den mittleren Aufrufwert nehmen |
| aufrufe | dieses Reel |
| hook | die erste Zeile, gesprochen oder im Bild, wörtlich, auch mit Fehlern |
| im Bild | die erste Textkarte, falls anders |
| länge | Sekunden |
| cta | worum am Ende gebeten wurde |

Der Normalwert (median) ist die wichtige Spalte. Ohne ihn ordnet man wieder
nach Followerzahl, und genau das soll dieser Skill verhindern.

**Wenn Instagram nicht genug zeigt:** Dieselbe Hook-Grammatik läuft auf
YouTube Shorts, wo Aufrufzahlen und Untertitel öffentlich sind und keine
Anmeldung nötig ist. Ein legitimer zweiter Stapel, und die gesprochene erste
Zeile ist dort leichter zu bekommen:

```bash
# Aufrufe der Shorts eines Kanals
python3 -m yt_dlp --flat-playlist --playlist-end 40 -J \
  "https://www.youtube.com/@HANDLE/shorts" > kanal.json

# die gesprochene erste Zeile eines Shorts, aus den automatischen Untertiteln
python3 -m yt_dlp --skip-download --write-auto-subs --sub-langs "de.*" \
  --sub-format json3 -o hook "https://www.youtube.com/watch?v=VIDEO_ID"
```

Jedes Untertitel-Wort mit Zeitstempel unter 3,0 Sekunden nehmen. Das ist der
Hook, wie er gesagt wurde, nicht wie er geschrieben steht. Nur, wenn yt_dlp
installiert ist; sonst diesen Teil überspringen.

## Schritt 3: Ordnen

Eine tab-getrennte Datei mit Kopfzeile füllen und das Skript laufen lassen:

```
account	follower	median	aufrufe	hook
@studio_x	4800	1100	41200	keiner sagt dir dass nach sitzung eins mehr haare da sind
```

```bash
python3 <skill-ordner>/swipe.py gesammelt.tsv --out ideen.md
```

Es berechnet das Vielfache, benennt die Hook-Formel mit denselben 26 Formeln,
aus denen `/ig-reel` schreibt, bewertet jeden Hook mit `hookscore.py` und
zeigt, was das obere Drittel vom unteren unterscheidet.

## Schritt 4: Sagen, was es bedeutet, vorsichtig

Drei Dinge berichten und nicht mehr:

1. **Welche Formeln im oberen Drittel gehäuft auftreten**, mit Zahlen. Zwei
   Formeln, die je viermal über sechs Accounts auftauchen, sind ein Befund.
   Eine, die zweimal auftaucht, ist keiner.
2. **Was das obere Drittel im Aufbau gemeinsam hat** und das untere nicht:
   Hook-Länge, ob das Ergebnis zu sehen ist, ob sich das erste Bild bewegt,
   wo die Aufforderung steht.
3. **Die Zeilen ohne Formel.** Jeder Hook, den das Skript nicht zuordnen
   konnte, ist entweder Rauschen oder eine Formel, die noch nicht in
   `hooks.json` steht. Die von Hand lesen. Das ist die wertvollste Spalte in
   der Ausgabe, und deshalb zählt das Skript sie.

Dann die Stichprobengröße und das Vertrauen in klaren Worten nennen. Vierzig
Reels über sechs Accounts tragen eine Aussage. Zwölf nicht, und das zu sagen
ist der Unterschied zwischen Recherche und Horoskop.

## Schritt 5: Daraus etwas machen, das gedreht wird

Für die besten drei Formeln **die Fassung der Nutzerin** schreiben: ihre
Geschichte, ihre Zahl aus `studio-profil.md`, in der Form, die gerade läuft.
Jede an `/ig-reel` übergeben, mit der Formel-Nummer schon gewählt.

Nie „mach ein Reel wie dieses hier“ zurückgeben. Eine Hook-Zeile zurückgeben,
die sie morgen sagen könnte. Dabei `../ig-start/nicht-versprechen.md`
beachten: Was andere Studios versprechen, ist kein Freibrief.

## Ausgabe

```
IDEEN  ·  38 Reels  ·  7 Accounts  ·  Basis: Normalwert des Accounts

AUSREISSER (über 3x)
  38,4x  Hook 78  #3  Das sagt dir keiner   @studio_a    41.200  (Normalwert 1.070)
  11,2x  Hook 72  #16 Original-Frage        @studio_c    18.000  (Normalwert 1.610)
  ...

WAS GEHÄUFT AUFTRITT
  #3 Das sagt dir keiner   5x im oberen Drittel, 0 im unteren
  #2 Hör auf damit         4x
  Hook-Länge (Median)      7 Wörter oben, 18 unten

OHNE FORMEL (6)
  Zwei davon haben dieselbe Form, und sie steht nicht in hooks.json: Ein Hook,
  der mit dem vorgelesenen Kommentar einer Kundin beginnt. Lohnt sich.

DEINE FASSUNG
  #3  „Keiner sagt dir, dass nach Sitzung eins erstmal mehr Haare da sind.“
  ...
```

Die Ideen-Datei nach `ideen.md` im Arbeitsordner schreiben. `/ig-reel` und
`/ig-plan` lesen sie beide, und das ist der Punkt: Sobald das einmal gelaufen
ist, arbeitet der Rest des Pakets mit den eigenen Belegen der Nutzerin statt
mit Standardwerten.

Dieser Skill postet nichts, folgt niemandem, liket nichts und schreibt
niemanden an. Er liest.
