---
name: ig-plan
description: >-
  Plant die Instagram-Woche eines Kosmetikstudios: welche Reels an welchem Tag,
  welche Stories, mit fertigen Hooks. Claude bringt selbst Ideen mit (aus
  Studio-Profil, Recherche, Ideen-Liste und dem, was gelernt wurde), fragt nach
  Neuem aus dem Studio, und die Nutzerin bestätigt oder ändert jeden Platz.
  Nutzen, wenn die Nutzerin sagt "plane meine Woche", "was soll ich posten",
  "Content-Plan", "Wochenplan", "ich habe keine Ideen".
---

# ig-plan

Die Schaltzentrale. Einmal pro Woche, am selben Tag, zum Beispiel Sonntagabend
oder Montag früh vor der ersten Kundin. Die Nutzerin muss nicht kreativ sein:
Claude bringt die Ideen mit, sie entscheidet.

## Eingabe

Lesen, falls vorhanden: `studio-profil.md`, `recherche.md`, `ideen.md`,
`viral.md`, `lernen.md`, `log.md`, den letzten `wochenplan.md`. Fehlt
`studio-profil.md`, `/ig-start` vorschlagen.

Dann zwei kurze Fragen, mit Beispielen, damit sie weiß, was gemeint ist:

> **1. Gab es diese Woche etwas im Studio, das du erzählen möchtest?**
> Zum Beispiel: eine Frage, die mehrmals kam, eine Kundin mit einem schönen
> Ergebnis, ein Missverständnis, etwas Neues im Studio. Du kannst es einfach
> reinsprechen oder tippen. Wenn nichts war, sag „nichts“, ich habe Ideen.
>
> **2. Gibt es ein Ziel für die Woche?**
> Zum Beispiel: freie Termine füllen, eine Behandlung bekannter machen, mehr
> Follower aus deinem Stadtteil. Oder einfach: „regelmäßig posten“.

Aus dem, was sie erzählt, werden Plätze. Den Rest füllt Claude selbst, in
dieser Reihenfolge:
1. offene Ideen aus `ideen.md` (Status `offen`)
2. Kundinnen-Fragen, Haltungen und Befürchtungen aus `studio-profil.md`
3. Fragen, Ängste und Mythen aus `recherche.md`
4. höchstens eine Idee aus `ideen-vorrat.md` in diesem Ordner

Ist `ideen.md` fast leer und es gibt keine Recherche, vorher kurz `/ig-ideen`
laufen lassen oder anbieten.

Was in `lernen.md` unter „Mag ich nicht“ steht, kommt nicht in den Plan.
Was im `log.md` der letzten zwei Wochen steht, auch nicht noch einmal.

## Was in die Woche kommt

**Drei Reels und jeden Tag Stories.** Das ist für ein Studio mit vollem
Terminkalender ein Takt, der sich halten lässt. Reels sind das Format, das
Leute erreicht, die dem Studio noch nicht folgen. Stories halten die, die
schon folgen, und bringen Termine. Karussells nur, wenn die Nutzerin danach
fragt.

Die drei Reels mischen, nie zweimal derselbe Typ:

| Typ | Aufgabe | Beispiel (dauerhafte Haarentfernung) |
| --- | --- | --- |
| **Frage** | eine echte Frage der Kundinnen beantworten | „‚Tut Laser mehr weh als Wachs?‘ Die Frage kriege ich jede Woche.“ |
| **Mythos** | einen Irrtum richtigstellen | „Hör auf, vor dem Termin zu zupfen. Damit verschenkst du die Sitzung.“ |
| **Ergebnis** | zeigen, was passiert, mit Einverständnis und ehrlich | „Nach Sitzung 4, nicht nach der ersten. So sieht der echte Weg aus.“ |
| **Gefühl** | eine Alltagsszene, in der sich die Zuschauerin erkennt | „Du sagst das Treffen ab, weil du dich nicht rasiert hast?“ |
| **Haltung** | eine ehrliche Meinung, die nicht alle teilen | „Nach Sitzung 1 sieht es schlimmer aus. Und das ist gut so.“ |

Jedes Thema muss eine Frage beantworten, die eine Kundin wirklich hat. Was nur
das Studio interessiert (Gerät kaputt, Urlaub, neue Tapete), gehört höchstens
in die Story.

**Stories:** Will die Nutzerin Termine füllen, die Story-Treppe aus
`../ig-story/story-treppe.md` über die Woche legen. Sonst je Tag ein Satz,
was gezeigt wird.

## Ausgabe

Für jeden Reel-Platz: Tag, Uhrzeit, Typ, **vollständiger gesprochener Hook**,
Hook-Karte (höchstens sechs Wörter), ein Satz, worum es geht, und woher die
Idee kommt (aus deiner Woche / aus deinem Profil / aus der Recherche).

```
WOCHE VOM 12. OKTOBER

DI  18:30  REEL  FRAGE
    Hook:  „‚Tut Laser mehr weh als Wachs?‘ Die Frage kriege ich jede Woche.“
    Karte: TUT LASER MEHR WEH?
    Worum: ehrliche Antwort, Wärme und kurzes Zwicken, Vergleich mit Wachs.
    Woher: Frage 1 aus deinem Profil, auch in 6 von 10 Foren-Threads.

DO  18:30  REEL  MYTHOS
    ...

SO  19:00  REEL  GEFÜHL
    ...

STORIES  Mo bis Fr Story-Treppe zum Ziel „Termine füllen“ (Details unten).
```

Uhrzeit: früher Abend ist für Kundinnen von Studios meist gut. Ist Zernio
verbunden (`/ig-verbinden`), die beste Zeit aus den eigenen Statistiken holen
(Achtung, Zernio rechnet in UTC). Die Uhrzeit zählt viel weniger als die
ersten zwei Sekunden.

## Bestätigen lassen

Danach fragen, als Auswahl, wenn die Sitzung das kann:

> **Passt der Plan so?**
> 1. **Ja, passt.** Ich speichere ihn.
> 2. **Einzelne Plätze ändern.** Sag mir welche, ich mache neue Vorschläge.
> 3. **Ganz andere Richtung.** Sag mir, was dir fehlt.

Erst nach „ja“ in `wochenplan.md` speichern. Jede Änderung, die etwas über
ihren Geschmack sagt („keine Preis-Themen“, „mehr Gefühl“), in `lernen.md`.

Danach: „Sag ‚schreib Dienstag‘, dann mache ich mit /ig-reel das Skript.“

## Austausch mit anderen Accounts

Optional, nicht Pflicht: Wer will, kommentiert ein paar Minuten am Tag bei
Accounts aus der Nachbarschaft (Friseurin, Café, Stadtteil-Seite) oder bei
Kolleginnen aus anderen Städten. Das macht das Studio sichtbar bei Leuten, die
es noch nicht kennen. Dass es die eigene Reichweite direkt erhöht, ist nicht
belegt; es ist Kontaktpflege. Vorschläge schreibt `/ig-comment`.

Nichts wird geplant oder gepostet. Das ist ein Plan, und die Nutzerin führt
ihn aus, oder plant ihn mit `/ig-posten` in Zernio ein.
