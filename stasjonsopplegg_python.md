# Pythonstasjon: Romstasjon Mysteriet

Et kort, interaktivt oppdrag for 10. trinn. Elevene leter etter en alien som har stjålet nøkkelkortet, og endrer deretter programmet selv.

## Før elevene kommer

- Ha [romstasjon_mysteriet.py](./romstasjon_mysteriet.py) klart i VS Code.
- Sjekk at Python er installert, og at fila kan kjøres med **Run Python File**.
- La elevene jobbe to og to hvis det er mange ved stasjonen.

## 13-minutters plan

| Tid | Aktivitet |
|---|---|
| 0–1 min | **Hook:** «Nøkkelkortet til romstasjonen er stjålet. Koden kan avsløre hvem som tok det. Kan dere hjelpe roboten BIP?» |
| 1–3 min | Kjør programmet. Elevene har fire forsøk på å finne den skyldige blant 10 aliens. Spør: «Hva forteller hintene dere?» |
| 3–6 min | Elevene velger en startoppgave nedenfor, for eksempel å endre robotnavnet eller antall forsøk. Kjør programmet på nytt. |
| 6–10 min | Velg en utforskeroppgave: endre antall mistenkte, teste ulike svar eller spille flere ganger for å undersøke trekningen. |
| 10–12 min | Velg en bonusoppgave hvis dere vil kode mer. La parene vise hverandre hva de endret. |
| 12–13 min | Avslutt med: «Hva var det dere endret? Hva gjorde Python automatisk?» |

## Oppgaver for elevene

Oppgavene kan gjøres i rekkefølge eller velges etter hvor mye tid dere har.

### Startoppgaver

1. Gi roboten et nytt navn, og skriv om alarmmeldingen.
2. Endre `maks_forsok`. Prøv å gjøre spillet lettere eller vanskeligere.
3. Endre `rompoeng` og finn på en ny premie.

### Utforsk

4. Endre `antall_mistenkte`. Sjekk at programmet fortsatt ber om et tall innenfor riktig område, og at hintene fungerer.
5. Skriv inn bokstaver, `0` eller et tall som er større enn antall mistenkte. Hvordan svarer programmet? Merk at et ugyldig svar bruker et forsøk i den nåværende versjonen.
6. Spill flere ganger. Blir den skyldige trukket på nytt hver gang?

### Bonus

7. Endre programmet slik at bokstaver og tall utenfor området ikke bruker et forsøk.
8. Legg til et hint som forteller om den skyldiges nummer er partall eller oddetall.

## For den som leder stasjonen

- Ikke vis fasiten med en gang: la elevene gjette hva som er tilfeldig og kjøre programmet flere ganger.
- Hvis de står fast, pek på oppdragskommentarene øverst i Python-fila. Be elevene velge én oppgave om gangen og kjøre programmet etter hver endring.
- Kjerneideen er at `antall_mistenkte` styrer trekningen og valgene elevene får. Hintet sier om det hemmelige nummeret er høyere eller lavere enn gjetningen.
- `rompoeng` er en variabel som brukes i meldingen om belønningen.
- Det er ikke meningen at alle skal rekke alle oppgavene. Det viktigste er å kjøre, endre og teste.

## Slik kjører dere

1. Åpne `romstasjon_mysteriet.py` i VS Code.
2. Trykk på trekanten **Run Python File** oppe til høyre.
3. Skriv svaret i terminalen nederst og trykk Enter.
