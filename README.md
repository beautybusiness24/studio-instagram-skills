# Instagram-Skills für Kosmetikstudios

14 Claude-Skills, die den Instagram-Account eines Kosmetikstudios führen. Auf
Deutsch, mit Beispielen aus dem Studioalltag. Kostenlos, MIT-Lizenz, keine
Anmeldung, kein Schlüssel, nichts zu verbinden.

Einer legt im Gespräch dein Studio-Profil an, aus dem alle anderen lesen.
Einer schreibt deine Reels aus 26 Hook-Formeln und bewertet den Hook, bevor
du einen Take darauf verschwendest. Einer sieht nach, welche Reels in deiner
Nische gerade wirklich laufen. Einer schreibt die Caption und zeigt dir genau,
was der Feed vor dem „... mehr“ anzeigt. Einer bewertet dein Profil mit 100
Punkten. Einer plant die Woche.

Und einer ist der Humanizer, der Grund, warum der Rest brauchbar ist. Er
entfernt Gedankenstriche, Floskeln wie „Wohlfühloase“ und unsichtbare
Zeichen aus jedem Entwurf und misst, was übrig bleibt, mit fünf Prüfungen,
bevor du es siehst.

**Nichts wird gepostet, bis du ja sagst.** Diese Skills schreiben. Du postest.

## Installieren

In der Claude-Desktop-App, im Bereich **Code**:

1. Auf **+** neben dem Eingabefeld klicken, dann **Plugins**, dann
   **Marketplace hinzufügen**.
2. Diese Adresse eintragen: `https://github.com/beautybusiness24/studio-instagram-skills.git`
3. Das Plugin **bb24-instagram** auswählen und **Installieren**.
4. Claude einmal neu starten.

Oder im Terminal von Claude Code:

```
/plugin marketplace add beautybusiness24/studio-instagram-skills
/plugin install bb24-instagram
```

Oder du gibst Claude einfach diesen Link und schreibst dazu: „Bitte
installiere dieses Plugin für mich.“

Dann einen Ordner **Instagram-Studio** auf dem Schreibtisch anlegen, in Claude
öffnen, und `/ig-start` eingeben. Das Gespräch dauert zehn Minuten und legt
`studio-profil.md` an. Jeder Skill liest diese Datei.

## Die vierzehn

| Befehl | was er macht |
| --- | --- |
| `/ig-start` | Legt im Gespräch dein Studio-Profil an und die Ordner, in denen alles gespeichert wird. Der erste Befehl. |
| `/ig-reel` | Eine Idee wird ein Reel. Drei Hooks aus [26 Formeln](skills/ig-reel/hooks.json), bewertet, dann das Skript, der Text im Bild und ein Zeitplan pro Satz. |
| `/ig-viral` | Sieht nach, was in deiner Nische läuft, ordnet nach dem Vielfachen über dem Normalwert jedes Accounts, benennt die Formel, schreibt die Ideen-Datei. |
| `/ig-caption` | Die Caption: die Zeile vor dem „... mehr“, die eine Aufforderung, die Suchbegriffe, bis zu fünf Hashtags. Geprüft. |
| `/ig-plan` | Die Woche: was, welches Format, wann, mit wem du dich austauschst. |
| `/ig-profile` | Bewertet dein Profil mit 100 Punkten nach 12 Kriterien und schreibt neu, was Punkte verliert. |
| `/ig-audit` | Rückblick auf das, was du gepostet hast: was lief, warum, womit du aufhören solltest. |
| `/ig-carousel` | Karussell: Cover, Text Folie für Folie, Dateien zum Hochladen. |
| `/ig-story` | Die Stories des Tages, Bild für Bild, mit den Stickern und dem Bild, das Termine bringt. |
| `/ig-comment` | Kommentare unter die Beiträge anderer, die wie eine Person klingen. |
| `/ig-reply` | Deine eigenen Kommentare sortiert nach Wert, mit Antworten. Fragen werden Reels. |
| `/ig-dm` | DMs: die Stichwort-Lieferung, die Terminanfrage, die Kooperationsanfrage, zwei Nachfass-Nachrichten. |
| `/ig-repurpose` | Aus einem Beratungsgespräch, einer Schulung oder einem Live wird eine Woche Beiträge. |
| `/ig-human` | Entfernt den Maschinen-Fingerabdruck und misst mit fünf Prüfungen. Läuft vor allem anderen. |

## Wo deine Daten liegen

Im Ordner, den du in Claude geöffnet hast. Keine versteckten Ordner.

```
studio-profil.md    wer du bist, was du anbietest, wie du sprichst
ideen.md            was in deiner Nische gerade funktioniert
wochenplan.md       was diese Woche gepostet wird
log.md              was schon gepostet wurde, mit Hook-Formel
reels/              ein Skript je Datei, mit Caption
beitraege/          Karussells
stories/            Story-Abläufe
```

## Die Werkzeuge

Fünf Skills bringen kleine Python-Programme mit, die auf deinem Rechner
laufen: Hook-Wertung, Zeitplan, Caption-Prüfung, Ideen-Auswertung, Humanizer.
Sie brauchen nur Python 3, nichts weiter. Auf dem Mac ist es da. Unter
Windows einmal von [python.org](https://www.python.org/downloads/) installieren
und beim Installieren „Add python.exe to PATH“ anhaken. Ohne Python arbeiten
die Skills trotzdem, dann bewertet Claude von Hand und sagt das dazu.

## Was ein Studio nicht verspricht

Alle Skills lesen [nicht-versprechen.md](skills/ig-start/nicht-versprechen.md),
bevor sie einen Text ausgeben: kein „für immer“, kein „garantiert“, kein
„schmerzfrei“, keine Heilung, keine fremden Vorher-Nachher-Bilder, keine
erfundenen Zahlen. Die Liste ist kein Rechtstext und steht in keinem
Beitrag. Sie sorgt dafür, dass du nichts behauptest, was du nicht halten
kannst.

## Herkunft

Dieses Paket ist eine deutsche, auf Kosmetikstudios zugeschnittene Fassung
des [instagram-agent-skill](https://github.com/Jakeschincariol/instagram-agent-skill)
von Jake Schincariol (MIT-Lizenz, siehe [LICENSE-original](LICENSE-original)).
Die Hook-Formeln, die Werkzeuge und der Aufbau der Skills stammen von dort.
Übersetzung, Studio-Beispiele, der Skill `/ig-start`, die deutsche
Floskel-Liste und die Liste der Versprechen sind von
[Beauty Business 24](https://beautybusiness24.com).

## Lizenz

MIT. Siehe [LICENSE](LICENSE).
