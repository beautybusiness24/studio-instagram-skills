---
name: ig-profile
description: >-
  Bewertet das Instagram-Profil eines Kosmetikstudios mit 100 Punkten nach 12
  Kriterien und schreibt die Teile neu, die Punkte verlieren: Namensfeld,
  Bio, Link, Highlights, die drei angepinnten Beiträge, das Raster. Nutzen,
  wenn die Nutzerin sagt "optimiere mein Profil", "verbessere meine Bio",
  "bewerte mein Instagram", "warum folgt mir keiner", oder ihr Profil
  einfügt und fragt, wie es wirkt.
---

# ig-profile

Fast alle optimieren hier das Falsche. Das Profil ist kein Schaufenster, in
dem jemand bummelt. Es ist ein **Entscheidungsbildschirm**, erreicht von
einem Reel aus, und er hat etwa drei Sekunden, um eine Frage zu beantworten:
Gibt es hier mehr davon, und ist das für mich? Bei einem Studio kommt eine
zweite Frage dazu: Ist das in meiner Nähe?

## Eingabe

Die Nutzerin bitten, einzufügen oder als Screenshot zu schicken: das
Namensfeld, den Handle, die Bio, wohin der Link führt, die Namen der
Highlights, was angepinnt ist, und die ersten neun Raster-Cover. Ein
Screenshot vom oberen Teil des Profils plus die ersten zwei Raster-Reihen
reicht für den ersten Durchgang.

Sich nicht bei Instagram für sie anmelden.

`studio-profil.md` im Arbeitsordner lesen, falls vorhanden. Dort stehen
Behandlung, Stadt, Belege und Stichwort, die in die neue Bio gehören.

## Bewerten

`rubric.json` in diesem Ordner lesen. Zwölf Punkte, 100 Zähler, jeder mit
dem, was volle Punktzahl ist und wie es meistens scheitert. Jeden Punkt
bewerten, die Tabelle zeigen, die Summe nennen. Ehrlich sein. Die meisten
Studio-Profile landen beim ersten Durchgang zwischen 30 und 45, und eine
großzügige Note ist nutzlos.

```
PROFIL-WERTUNG  38/100

  Namensfeld        2/12   nur „Lena's Beauty Lounge“, kein Wort, nach dem jemand sucht
  Bio Zeile 1       3/12   drei Substantive und ein Funkel-Emoji
  angepinnte Drei   0/10   nichts angepinnt
  Highlights        2/8    „Random“, „Life“, „2023“
  Raster            4/8    sechs von neun Covern sind ein Gesicht mitten im Wort
  ...
```

## Dann neu schreiben, in dieser Reihenfolge

In absteigender Reihenfolge der verlorenen Punkte beheben. Nicht alles auf
einmal umschreiben, die Nutzerin muss jedes davon wirklich ändern gehen.

**1. Das Namensfeld (30 Zeichen).** Die fette Zeile unter dem Foto, nicht der
Handle. Dieses Feld durchsucht Instagram, und die meisten Studios schreiben
einen Namen hinein und sonst nichts. Form, die funktioniert:
`{Vorname} | {Behandlung} {Stadt}`. Beispiel: „Lena | Haarentfernung Berlin“ (28 Zeichen; „Dauerhafte
Haarentfernung“ passt nicht mehr hinein). Drei Varianten geben, jede nachzählen.

**2. Bio Zeile eins.** Für wen das Studio da ist und was sich ändert, mit Ort.
Kein Berufstitel, keine Adjektive, keine Liste mit Strichen. Der Rest der 150
Zeichen trägt einen Beleg (Jahre, Bewertungen, Anzahl Behandlungen aus dem
Studio-Profil) oder ein schlichtes Angebot. `../ig-start/nicht-versprechen.md`
gilt auch in der Bio: kein „schmerzfrei“, kein „für immer“.

**3. Die angepinnten Drei.** Drei Plätze, drei verschiedene Aufgaben: das beste
Ergebnis (Vorher/Nachher mit Einverständnis), der klarste Ablauf einer
Behandlung, die beste Vorstellung der Person hinter dem Studio. Das ist der
wirksamste Handgriff auf dem ganzen Profil, und er braucht vier Tipps. Ein
Raster ohne angepinnte Beiträge zeigt, was zuletzt gepostet wurde, und das
ist ein Münzwurf.

**4. Highlights.** Vier bis sechs, benannt nach den Fragen, die eine Kundin vor
dem ersten Termin stellt: Preise, Ablauf, Ergebnisse, Über mich, Termine.
Nicht „Random“. Den Rest löschen.

**5. Der Link.** Ein Ziel, das zu dem passt, was die Bio gerade versprochen
hat, meistens die Terminbuchung. Fünf sind erlaubt; zwei sind schon eine
Speisekarte, und eine Speisekarte bringt weniger Buchungen als eine Tür.

**6. Raster-Cover.** Die ersten neun in Daumennagel-Größe. Reel-Cover werden
ausgewählt, nicht als zufälliges erstes Bild gelassen. Vier Wörter Text auf
einem Cover machen ein Raster in einem Blick lesbar.

**7. Unternehmenskonto, Kategorie, Adresse.** Bei einem Studio nicht
verhandelbar: Ohne Unternehmenskonto gibt es keine Insights, keinen
Kontakt-Knopf und keine Adresse, und ohne Adresse weiß die Zuschauerin nicht,
ob sie überhaupt hinkommen kann.

## Ausgabe

Wertungstabelle, dann die Neufassungen als kopierfertige Blöcke in der
Reihenfolge der Wirkung, jeder durch `/ig-human` gelaufen. Am Ende neu
bewerten und den Unterschied ehrlich zeigen. Erreicht die Neufassung 84 und
nicht 98, dann 84 sagen, und sagen, was der Rest braucht: meistens ein
Raster, eine Story-Gewohnheit und ein angepinnter Beitrag, der noch nicht
existiert. Nichts davon ist eine Neufassung.

Nichts wird bei Instagram gespeichert. Die Nutzerin ändert jedes Feld selbst.
