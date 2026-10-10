---
name: ig-start
description: >-
  Richtet das Instagram-System für ein Kosmetikstudio ein: legt im Gespräch das
  Studio-Profil an (studio-profil.md), aus dem alle anderen ig-Skills lesen,
  und erstellt die Ordner-Struktur. Nutzen, wenn die Nutzerin "/ig-start",
  "einrichten", "mein Studio anlegen", "Profil anlegen", "los geht's" sagt, oder
  wenn ein anderer ig-Skill feststellt, dass noch keine studio-profil.md im
  Arbeitsordner liegt.
---

# ig-start

Der erste Befehl. Alles andere in diesem Paket schreibt für genau ein Studio,
und dieses Studio wird hier beschrieben. Zehn Minuten hier entscheiden, ob die
Skripte später gedreht oder umgeschrieben werden.

Alle Texte dieses Pakets sind auf Deutsch. Die Nutzerin ist meistens die
Inhaberin eines Kosmetikstudios und arbeitet zum ersten Mal mit Claude. Kurz
und freundlich sprechen, keine Fachbegriffe aus der Technik, keine englischen
Begriffe, wo es deutsche gibt.

## Wo alles liegt

Der Arbeitsordner ist der Ordner, der gerade in Claude geöffnet ist. Dort
entsteht:

```
studio-profil.md    wer du bist, was du anbietest, wie du sprichst
ideen.md            was in deiner Nische gerade funktioniert (/ig-viral)
wochenplan.md       was diese Woche gepostet wird (/ig-plan)
log.md              was schon gepostet wurde, mit Hook-Formel (/ig-reel, /ig-audit)
reels/              ein Skript je Datei, mit Caption
beitraege/          Karussells
stories/            Story-Abläufe
```

Keine versteckten Ordner. Alles liegt sichtbar im Finder oder Explorer und
lässt sich sichern.

## Ablauf

**1. Prüfen, was schon da ist.** Liegt `studio-profil.md` im Arbeitsordner,
den Inhalt zusammenfassen und fragen, ob er noch stimmt oder etwas ergänzt
werden soll. Dann nur die Lücken abfragen, nicht alles von vorn.

**2. Ordner anlegen**, falls sie fehlen: `reels/`, `beitraege/`, `stories/`.
Außerdem leere `log.md` mit der Zeile `# Log` anlegen, wenn sie fehlt.

**3. Das Gespräch führen.** Die Vorlage liegt in diesem Ordner als
`profil-vorlage.md`. Nicht die Vorlage zum Ausfüllen schicken, sondern
fragen, in Runden von drei bis vier Fragen, und zwischendurch zeigen, was
schon steht. Reihenfolge:

- Runde 1, das Studio: Name, Vorname der Inhaberin, Handle, Stadt und
  Stadtteil, seit wann.
- Runde 2, die Hauptbehandlung: welche, Preis einzeln und als Paket, wie viele
  Sitzungen in welchem Abstand, welche weiteren Behandlungen. Wenn die
  Nutzerin eine Behandlung nennt, die unter die Haut geht (Unterspritzung,
  Fadenlifting), fragen, wer behandelt, und ohne Antwort keine Texte dazu
  schreiben. Siehe `nicht-versprechen.md`.
- Runde 3, die Kundin: wer kommt, die drei häufigsten Fragen vor dem ersten
  Termin wörtlich, was sie befürchtet. Hier entstehen die Hooks. Wenn die
  Nutzerin sagt „das weiß ich nicht“, nach dem letzten Erstgespräch fragen.
- Runde 4, die Stimme: Du oder Sie, ruhig oder schnell, Wörter, die sie
  wirklich benutzt, Wörter, die sie nie sagen würde, Gesicht vor der Kamera.
  Am besten: drei eigene Beiträge oder Reels einfügen lassen. Daraus lässt
  sich die Stimme ablesen, besser als aus jeder Selbstbeschreibung.
- Runde 5, die Haltung: drei Dinge, die sie glaubt und manche Kundinnen
  nicht. Beispiele anbieten, wenn nichts kommt: „Wer vor dem Termin zupft,
  verschenkt eine Sitzung“, „Pakete sind nicht billiger, sie sind
  konsequenter“.
- Runde 6, Belege und Tabus: Jahre, Anzahl Kundinnen, Google-Note, ein
  Ergebnis, das erzählt werden darf, Vorher-Nachher-Bilder vorhanden. Was
  nicht öffentlich werden darf.
- Runde 7, die Aufforderung: ein Stichwort für Kommentare, was man dafür
  bekommt, wohin der Link führt, wie man bucht.

Jede Antwort so übernehmen, wie sie gesagt wurde. Nicht glätten, nicht
aufwerten, nichts dazuerfinden. Wenn eine Zahl fehlt, bleibt das Feld leer.

**4. Die Datei schreiben.** `studio-profil.md` nach der Vorlage, alle
Abschnitte, leere Felder bleiben leer. Dann der Nutzerin die Datei zeigen und
fragen, ob etwas falsch ist.

**5. Den nächsten Schritt nennen.** Genau einen:

```
PROFIL ANGELEGT  studio-profil.md

Studio:        Lena, Kosmetikstudio in Berlin-Prenzlauer Berg
Hauptleistung: dauerhafte Haarentfernung, 6 bis 8 Sitzungen
Stimme:        Du, ruhig, direkt, selten Emoji
Belege:        11 Jahre, Google 4,9 bei 212 Bewertungen
Fehlt noch:    Anzahl Kundinnen, Vorher-Nachher-Bilder

Nächster Schritt: /ig-reel mit einer Frage, die dir eine Kundin diese Woche
gestellt hat. Oder /ig-viral, wenn du erst sehen willst, was bei anderen läuft.
```

## Regeln

- **Nichts erfinden.** Weder Zahlen noch Kundinnen noch Zitate. Lieber ein
  leeres Feld.
- **Nicht-versprechen.md lesen** und bei jeder Behandlung prüfen, ob die
  Nutzerin Begriffe daraus verwendet. Dann freundlich die bessere Formulierung
  vorschlagen, ohne Rechtsbelehrung.
- **Keine Anmeldung bei Instagram**, keine Passwörter, keine Zugangsdaten.
  Alles, was dieser Skill braucht, erzählt die Nutzerin.
- **Kurz halten.** Sieben Runden klingen nach viel, jede dauert eine Minute.
  Wenn die Nutzerin ungeduldig wird, Runden 5 bis 7 auf später verschieben
  und das Profil mit dem speichern, was da ist. Die anderen Skills fragen
  nach, was ihnen fehlt.
