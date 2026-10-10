---
name: ig-posten
description: >-
  Plant ein fertig geschnittenes Reel über Zernio auf Instagram ein: Video
  hochladen, Caption und Cover aus der Reel-Datei übernehmen, Zeitpunkt wählen,
  nach ausdrücklichem Ja einplanen. Nutzen, wenn die Nutzerin sagt "poste
  das", "plane das Reel ein", "veröffentlichen", "/ig-posten", oder ein
  geschnittenes Video hat. Braucht eine Zernio-Verbindung (/ig-verbinden).
---

# ig-posten

Vom fertigen Video zum eingeplanten Reel, ohne Instagram-App. Die Caption und
die Hook-Karte stehen schon in der Reel-Datei aus `/ig-reel`.

## Voraussetzungen

1. Zernio ist verbunden. Gibt es keine Zernio-Werkzeuge oder kein
   Instagram-Konto in `accounts_list`: `/ig-verbinden` vorschlagen und stoppen.
2. **Das Video liegt auf dem Laptop.** Geschnitten wird meist am Handy
   (CapCut). Das fertige Video per AirDrop, E-Mail an sich selbst oder
   Google Drive auf den Laptop holen und in den Ordner `reels/` legen.
   Hochkant, 9:16, MP4, unter 300 MB, 3 bis 90 Sekunden.
3. Optional ein Cover-Bild (JPG oder PNG, 1080 x 1920) mit der Hook-Karte. Sonst
   wird ein Zeitpunkt im Video als Cover gewählt.

## Ablauf

**1. Zuordnen.** Fragen, zu welchem Skript in `reels/` das Video gehört, oder
die neueste Reel-Datei vorschlagen. Caption, Hook-Karte und Cover-Vorschlag
daraus lesen. Fehlt die Caption: mit den Regeln aus `../ig-caption/SKILL.md`
schreiben und zeigen.

**2. Zeitpunkt.** Aus `wochenplan.md` nehmen, falls dort ein Platz steht.
Sonst fragen, mit Vorschlag: früher Abend, oder die beste Zeit aus den eigenen
Zernio-Statistiken (`analytics_get_best_time_to_post`, Ergebnis ist UTC, in
deutsche Zeit umrechnen). „Jetzt sofort“ geht auch.

**3. Hochladen.** Mit Zernio einen Upload-Link holen
(`media_generate_upload_link`), das Video hochladen, Status prüfen
(`media_check_upload_status`). Bei einem Fehler genau sagen, was nicht
stimmt (Format, Größe, Länge).

**4. Vorschau zeigen, nichts senden.** So:

```
BEREIT ZUM EINPLANEN
Konto:      @studio.lena.berlin
Video:      reels/2026-10-11-mehr-haare.mp4 (31 s)
Cover:      Bild bei Sekunde 1, mit Hook-Karte „MEHR HAARE NACH SITZUNG 1?“
Zeitpunkt:  Dienstag, 13.10., 18:30 Uhr (16:30 UTC)
Caption:    [vollständig]
Auch im Feed zeigen: ja
```

Dann fragen: **„Soll ich das genau so einplanen?“** Nur bei einem klaren Ja
weiter. Bei Änderungswünschen ändern und neu zeigen.

**5. Einplanen.** Mit `posts_create` (oder `validate_post` vorher), Plattform
Instagram, Konto aus Schritt 1, Video, Caption, Cover (`instagramThumbnail`
oder `thumbOffset` in Millisekunden), Zeitpunkt. Bei „jetzt“ statt dessen
`posts_publish_now`.

**6. Bestätigen und festhalten.**

```
EINGEPLANT
Dienstag, 13.10., 18:30 Uhr auf @studio.lena.berlin
Ändern oder löschen: sag es mir, oder im Zernio-Dashboard.
```

In der Reel-Datei den Status auf `eingeplant` mit Datum setzen und in
`log.md` die Zeile ergänzen.

## Nach dem Posten

In der ersten Stunde auf Kommentare antworten: `/ig-reply` holt sie direkt
über Zernio. Nach 24 Stunden sind die Zahlen da: `/ig-audit`.

## Regeln

- **Nie ohne ausdrückliches Ja einplanen oder veröffentlichen.** Auch nicht,
  wenn ein Wochenplan „Dienstag 18:30“ sagt.
- Keine Musik aus dem Instagram-Katalog über Zernio; Musik wird in CapCut
  ins Video geschnitten.
- Stories mit Umfrage, Fragen-Box oder Link postet die Nutzerin in der App;
  Sticker gehen über Zernio nicht.
- Höchstens ein Konto auswählen. Hat Zernio mehrere Instagram-Konten, fragen,
  welches.

## Lernen

`lernen.md` im Arbeitsordner vor dem Schreiben lesen und beachten. Korrigiert
die Nutzerin etwas, das über ihren Geschmack sagt („würde ich nie sagen“, „zu
werblich“, „genau so“), danach eine Zeile mit Datum in `lernen.md` eintragen
und kurz sagen: „Hab ich mir gemerkt.“
