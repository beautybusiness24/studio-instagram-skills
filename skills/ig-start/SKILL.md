---
name: ig-start
description: >-
  Richtet das Instagram-System für ein Kosmetikstudio ein: legt im Gespräch das
  Studio-Profil an (studio-profil.md), aus dem alle anderen ig-Skills lesen,
  bietet danach eine Recherche zu den Behandlungen an (recherche.md) und
  erstellt Ordner und Lern-Datei. Nutzen, wenn die Nutzerin "/ig-start",
  "einrichten", "mein Studio anlegen", "Profil anlegen", "los geht's" sagt, oder
  wenn ein anderer ig-Skill feststellt, dass noch keine studio-profil.md im
  Arbeitsordner liegt.
---

# ig-start

Der erste Befehl. Alles andere in diesem Paket schreibt für genau ein Studio,
und dieses Studio wird hier beschrieben. Zehn Minuten hier entscheiden, ob die
Skripte später nach der Inhaberin klingen oder nach einer Werbeagentur.

Alle Texte dieses Pakets sind auf Deutsch. Die Nutzerin ist meistens die
Inhaberin eines Kosmetikstudios und arbeitet zum ersten Mal mit Claude. Kurz
und freundlich sprechen, keine Fachbegriffe aus der Technik, keine englischen
Begriffe, wo es deutsche gibt.

## Wo alles liegt

Der Arbeitsordner ist der Ordner, der gerade in Claude geöffnet ist. Dort
entsteht:

```
studio-profil.md    wer du bist, was du anbietest, wie du sprichst
recherche.md        was Frauen im Netz zu deinen Behandlungen fragen und befürchten
ideen.md            deine Ideen-Liste für Reels (/ig-ideen, /ig-viral)
wochenplan.md       was diese Woche gepostet wird (/ig-plan)
lernen.md           was Claude über deinen Geschmack gelernt hat
log.md              was schon gepostet wurde, mit Hook-Formel
reels/              ein Skript je Datei, mit Caption
stories/            Story-Abläufe
```

Keine versteckten Ordner. Alles liegt sichtbar im Finder oder Explorer.

## Ablauf

**1. Prüfen, was schon da ist.** Liegt `studio-profil.md` im Arbeitsordner,
den Inhalt in fünf Zeilen zusammenfassen und fragen, ob er noch stimmt. Dann
nur die Lücken abfragen, nicht alles von vorn.

**2. Ordner und Dateien anlegen**, falls sie fehlen: `reels/`, `stories/`,
`log.md` (Zeile `# Log`) und `lernen.md` (siehe unten).

**3. Das Gespräch führen.** Die Vorlage liegt in diesem Ordner als
`profil-vorlage.md`. Nicht die Vorlage zum Ausfüllen schicken, sondern in
Runden fragen, je Runde drei bis vier Fragen. **Zu jeder Frage ein Satz, warum
sie wichtig ist, und ein Beispiel**, damit die Nutzerin weiß, was gemeint ist.
Wer zum ersten Mal so ein Profil anlegt, weiß sonst nicht, wie ausführlich die
Antwort sein soll. Zwischen den Runden kurz zeigen, was schon steht.

So sehen die Runden aus (Beispiele immer dazuschreiben):

- **Runde 1, das Studio.**
  Name, Vorname, Handle, Stadt und Stadtteil, seit wann, wie gebucht wird.
  Beispiel: „Studio Lena, Lena, @studio.lena.berlin, Berlin-Prenzlauer Berg,
  seit 2015, Buchung über Treatwell oder WhatsApp.“
- **Runde 2, die Hauptbehandlung.**
  Warum: Davon handeln die meisten Reels.
  Fragen: Welche Behandlung bringt das meiste Geld? Was kostet sie einzeln und
  als Paket? Wie viele Sitzungen, in welchem Abstand? Welche anderen
  Behandlungen gibt es?
  Beispiel: „Dauerhafte Haarentfernung mit Diodenlaser. Achseln 59 Euro, Paket
  6 Sitzungen 299 Euro. 6 bis 8 Sitzungen alle 4 bis 6 Wochen. Daneben
  Aquafacial und Wimpernlifting.“
  Geht eine Behandlung unter die Haut (Unterspritzung, Fadenlifting), fragen,
  wer behandelt, und ohne Antwort keine Texte dazu. Siehe `nicht-versprechen.md`.
- **Runde 3, die Kundin.**
  Warum: Ihre Fragen und Ängste sind die besten Hooks, und zwar wörtlich.
  Fragen: Wer kommt zu dir? Welche drei Fragen hörst du vor dem ersten Termin
  am häufigsten, so wie die Kundin sie sagt? Wovor hat sie Angst? Warum bucht
  sie am Ende bei dir?
  Beispiel: „Frauen 25 bis 45, die jahrelang gewachst haben. ‚Tut das weh?‘,
  ‚Wie oft muss ich wirklich kommen?‘, ‚Geht das bei dunkler Haut?‘ Angst vor
  Schmerz und davor, dass es nicht wirkt. Sie bucht, weil ich ehrlich sage,
  was geht.“
  Wenn die Nutzerin sagt „weiß ich nicht“: nach dem letzten Erstgespräch
  fragen, was die Kundin da gesagt hat. Oder sagen, dass die Recherche in
  Schritt 5 genau das nachliefert.
- **Runde 4, die Stimme.**
  Warum: Sie muss die Sätze später laut sagen. Klingt ein Satz nicht nach ihr,
  dreht sie ihn nicht.
  Fragen: Du oder Sie? Wie bist du vor der Kamera (ruhig, schnell, lustig,
  direkt)? Welche Wörter benutzt du oft? Welche würdest du nie sagen? Emoji ja
  oder nein? Zeigst du dein Gesicht?
  Beispiel: „Du. Ruhig und direkt. Ich sage oft ‚ehrlich gesagt‘. Nie
  ‚Wohlfühloase‘ oder ‚Girls‘. Selten ein Emoji. Lieber Hände als Gesicht.“
  Am besten: drei eigene Captions oder Reels einfügen lassen. Daraus lässt sich
  die Stimme besser ablesen als aus jeder Selbstbeschreibung.
- **Runde 5, die Haltung.**
  Warum: Eine Meinung, die nicht alle teilen, ist der Stoff für Reels, die
  geteilt werden.
  Frage: Welche drei Dinge glaubst du, die manche Kundinnen nicht glauben?
  Beispiele anbieten, wenn nichts kommt: „Wer vor dem Termin zupft,
  verschenkt eine Sitzung.“ „Nach der ersten Sitzung sieht es schlimmer aus,
  und das ist normal.“ „Eine einzelne Gesichtsbehandlung ist ein Event, keine
  Kur.“
- **Runde 6, Belege und Tabus.**
  Warum: Zahlen machen Reels glaubwürdig. Ohne sie erfindet Claude keine,
  sondern lässt eine Lücke.
  Fragen: Wie viele Jahre machst du das? Ungefähr wie viele Kundinnen? Welche
  Google-Note bei wie vielen Bewertungen? Ein Ergebnis einer Kundin, das du
  erzählen darfst, ohne Namen? Hast du Vorher-Nachher-Bilder mit
  Einverständnis? Was darf nie öffentlich werden?
  Beispiel: „11 Jahre, etwa 3.000 Kundinnen, Google 4,9 bei 212. Eine Kundin
  kam nach 15 Jahren Wachs und brauchte nach vier Sitzungen keinen Rasierer
  mehr. Vorher-Nachher von drei Kundinnen. Keine Umsatzzahlen.“

Jede Antwort so übernehmen, wie sie gesagt wurde. Nicht glätten, nicht
aufwerten, nichts dazuerfinden. Wenn eine Zahl fehlt, bleibt das Feld leer.

**Keine Aufforderung im Profil.** Stichwort, „Termin sichern“, „speicher dir
das“: Das hängt vom einzelnen Reel ab und wird dort entschieden, nicht hier.

**4. Die Datei schreiben.** `studio-profil.md` nach der Vorlage, alle
Abschnitte, leere Felder bleiben leer. Der Nutzerin zeigen und fragen, ob etwas
falsch ist.

**5. Recherche anbieten.** Fragen:

> „Soll ich jetzt im Netz nachsehen, was Frauen zu deinen Behandlungen fragen,
> befürchten und falsch glauben? Das dauert ein paar Minuten und gibt dir
> Stoff für viele Reels.“

Bei ja: Zur Hauptbehandlung (und kurz zu den weiteren) mit der Websuche dieser
Sitzung recherchieren: Foren und Fragen-Seiten (gutefrage, reddit,
Erdbeerlounge, urbia), Bewertungen von Studios, dazu ein bis zwei seriöse
Fachquellen (Fachgesellschaft, Verbraucherzentrale, Bundesamt). Ergebnis in
`recherche.md`:

1. die 10 häufigsten Fragen, wörtlich, mit Quelle
2. Ängste und Einwände, mit O-Ton
3. Mythen und was stimmt, mit Quelle
4. Gefühle und Alltagsszenen (Freibad, Partner, Rasurpickel), wörtlich
5. die Wörter der Kundinnen gegenüber den Fachwörtern

Nur Belegtes, mit Link. Keine Zahlen aus der Recherche als Zahlen des Studios
ausgeben. Fragen und Ängste nach Themen bündeln und je Thema angeben, in wie
vielen unabhängigen Quellen es vorkommt, sortiert nach Häufigkeit. Was nur
einmal vorkommt, ist ein Einzelfall und steht am Ende. Danach im Abschnitt „Aus der Recherche“ von `studio-profil.md` je
drei Stichpunkte eintragen. Die eigenen Angaben der Nutzerin bleiben, wie sie
sind; die Recherche steht getrennt daneben.

Gibt es keine Websuche in dieser Sitzung, das sagen und den Schritt
überspringen. Die Nutzerin kann ihn später mit `/ig-ideen` nachholen.

**6. Den nächsten Schritt nennen.** Genau einen:

```
PROFIL ANGELEGT  studio-profil.md  ·  recherche.md

Studio:        Lena, Studio Lena in Berlin-Prenzlauer Berg, seit 2015
Hauptleistung: dauerhafte Haarentfernung, 6 bis 8 Sitzungen
Stimme:        Du, ruhig, direkt, selten Emoji
Belege:        11 Jahre, Google 4,9 bei 212 Bewertungen
Recherche:     12 Fragen, 8 Ängste, 5 Mythen aus 14 Quellen
Fehlt noch:    Vorher-Nachher-Bilder

Nächster Schritt: /ig-ideen, dann bekommst du eine Liste mit Reel-Ideen.
```

## lernen.md

Die Datei, in der Claude festhält, was die Nutzerin mag und was nicht. Jeder
ig-Skill liest sie vor dem Schreiben. Anlegen mit:

```
# Was ich über dich gelernt habe

Hier trägt Claude ein, was du korrigiert, gelobt oder abgelehnt hast.
Du kannst Zeilen löschen oder selbst welche schreiben.

## Mag ich

## Mag ich nicht

## Regeln
```

Regel für alle Skills: Sagt die Nutzerin etwas wie „das würde ich nie sagen“,
„zu werblich“, „genau so“, „das Thema mag ich nicht“, dann nach der Antwort
eine Zeile in `lernen.md` eintragen, mit Datum, und kurz sagen: „Hab ich mir
gemerkt.“ Nur eintragen, was sie wirklich gesagt hat.

## Regeln

- **Nichts erfinden.** Weder Zahlen noch Kundinnen noch Zitate.
- **Nicht-versprechen.md lesen** und bei jeder Behandlung prüfen, ob die
  Nutzerin Begriffe daraus verwendet. Dann freundlich die bessere
  Formulierung vorschlagen, ohne Rechtsbelehrung.
- **Keine Anmeldung bei Instagram**, keine Passwörter, keine Zugangsdaten.
- **Kurz halten.** Wird die Nutzerin ungeduldig, Runden 5 und 6 auf später
  verschieben und mit dem speichern, was da ist. Die anderen Skills fragen
  nach, was ihnen fehlt.
