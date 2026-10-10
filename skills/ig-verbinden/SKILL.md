---
name: ig-verbinden
description: >-
  Führt Schritt für Schritt durch die Verbindung von Instagram mit Claude über
  Zernio (kostenlos für zwei Konten): Instagram auf Business oder Creator
  umstellen, Zernio-Konto anlegen, Instagram verbinden, Zernio als Connector in
  Claude hinzufügen, Verbindung testen. Danach können /ig-posten, /ig-audit,
  /ig-reply, /ig-dm und /ig-profile mit echten Instagram-Daten arbeiten.
  Nutzen, wenn die Nutzerin sagt "Instagram verbinden", "Zernio einrichten",
  "/ig-verbinden", oder ein anderer ig-Skill echte Daten braucht.
---

# ig-verbinden

Ohne Verbindung sieht Claude Instagram nicht: keine Aufrufe, keine Kommentare,
keine DMs, und posten kann er auch nicht. Zernio ist die Brücke. Zernio ist
ein Planungsdienst mit offizieller Instagram-Anbindung, und Claude kann ihn
direkt bedienen.

**Kosten:** Die ersten zwei verbundenen Konten sind kostenlos, ohne Kreditkarte,
mit allen Funktionen (Posten, Statistiken, Kommentare, DMs). Jedes Konto zählt
einzeln: Instagram ist eins, eine Facebook-Seite wäre das zweite. Ab dem
dritten Konto kostet es etwa 6 Dollar im Monat je Konto. (Stand Oktober 2026,
Quelle zernio.com/pricing und docs.zernio.com.)

## Zuerst prüfen, ob es schon läuft

Gibt es in dieser Sitzung Werkzeuge von Zernio (zum Beispiel `accounts_list`
oder `zernio_overview`), `accounts_list` aufrufen. Steht dort ein
Instagram-Konto: „Du bist schon verbunden mit @…“, fertig. Sonst die Schritte
unten, einen nach dem anderen. Nach jedem Schritt fragen, ob er geklappt hat.
Nie mehrere Schritte auf einmal schicken.

## Schritt 1: Instagram auf Unternehmens- oder Creator-Konto

Warum: Über private Konten darf kein Programm posten oder Zahlen lesen.

In der Instagram-App: Profil → Menü (drei Striche) → **Kontotyp und Tools** →
**Zu professionellem Konto wechseln** → Kategorie „Kosmetikstudio“ oder
„Schönheitssalon“ → **Unternehmen** wählen. Eine Facebook-Seite ist dafür
nicht nötig. Bei den meisten Studios ist das schon so eingestellt; dann steht
im Profil ein Knopf „Insights“ oder „Professionelles Dashboard“.

## Schritt 2: Zernio-Konto anlegen

Auf **zernio.com** registrieren, mit E-Mail oder Google. Keine Kreditkarte.
Claude gibt keine Passwörter ein und legt kein Konto an; das macht die
Nutzerin selbst.

## Schritt 3: Instagram in Zernio verbinden

Im Zernio-Dashboard Instagram hinzufügen und den Weg **„Instagram Login“**
wählen (nicht „Facebook Login“). Dann bei Instagram anmelden und den Zugriff
erlauben. Der Facebook-Weg ist nur nötig für Werbung, Musik aus dem
Instagram-Katalog oder das Auslesen fremder Konten.

Tauchen später keine DMs auf: in der Instagram-App unter Einstellungen →
**Nachrichten und Story-Antworten** → **Zugriff auf Nachrichten** bzw.
**Verbundene Tools** den Zugriff erlauben und in Zernio neu verbinden.

## Schritt 4: Zernio in Claude hinzufügen

In der Claude-App: **Einstellungen → Connectors → Benutzerdefinierten
Connector hinzufügen** (englisch „Add custom connector“).
- Name: `Zernio`
- URL: `https://mcp.zernio.com/mcp`
- Hinzufügen, dann mit dem Zernio-Konto anmelden. Ein Schlüssel ist nicht nötig.

Danach Claude einmal neu starten und den Ordner Instagram-Studio wieder
öffnen. Erscheint „Couldn't reach the MCP server“: Connector entfernen und neu
hinzufügen.

Im Terminal (Claude Code) geht es auch mit:
```
claude mcp add --transport http zernio https://mcp.zernio.com/mcp
```
und danach `/mcp` zum Anmelden.

## Schritt 5: Testen

`accounts_list` aufrufen und zeigen:

```
VERBUNDEN
Instagram:   @studio.lena.berlin
Profil:      Studio Lena
Kosten:      kostenlos (1 von 2 freien Konten)

Was jetzt geht:
  /ig-posten    Reels mit Caption und Cover einplanen
  /ig-audit     deine echten Zahlen: Aufrufe, Reichweite, Wiedergabezeit
  /ig-reply     Kommentare unter deinen Beiträgen lesen und beantworten
  /ig-dm        Nachrichten lesen und beantworten
  /ig-profile   Profil-Bewertung mit echten Daten
```

Dann ins Studio-Profil unter „Das Studio“ eintragen: `Zernio verbunden: ja,
Konto @…`.

## Regeln für alle Skills, die Zernio nutzen

- **Nie etwas senden, posten, löschen oder ausblenden ohne ausdrückliches Ja
  der Nutzerin zu genau diesem Text.** Vorher immer zeigen, was rausgeht.
- **Lesen ist frei.** Statistiken, Kommentare und Nachrichten abrufen geht ohne
  Nachfrage, wenn die Nutzerin den Skill aufgerufen hat.
- **Keine Massenaktionen.** Keine automatischen Antworten an alle, keine
  Nachrichten an Leute, die nicht zuerst geschrieben haben.
- **Instagram-Grenzen:** Auf DMs darf nur innerhalb von 24 Stunden nach der
  letzten Nachricht der Kundin geantwortet werden. Story-Sticker (Umfrage,
  Fragen-Box, Link) lassen sich nicht über Zernio setzen; Stories mit Stickern
  postet die Nutzerin in der App.
- **Zahlen kommen verzögert.** Reichweite und Aufrufe sind erst etwa 24 Stunden
  nach dem Posten aussagekräftig.
- **Zeiten in UTC.** Zernio rechnet in UTC. Deutsche Zeit ist im Winter eine,
  im Sommer zwei Stunden später.
