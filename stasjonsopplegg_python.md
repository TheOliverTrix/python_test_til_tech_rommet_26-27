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
| 3–6 min | Elevene endrer `robot = "BIP"` til et eget robotnavn og endrer en av tekstene. Kjør programmet igjen. |
| 6–10 min | **Hardere oppdrag:** Endre `antall_mistenkte = 10` til et annet tall. Kjør programmet på nytt og sjekk at både valgene og hintene fortsatt gir mening. |
| 10–12 min | **Bonus:** Endre rompoengene fra 100 til 500, eller finn på en ny premie. La parene vise hverandre endringen. |
| 12–13 min | Avslutt med: «Hva var det dere endret? Hva gjorde Python automatisk?» |

## For den som leder stasjonen

- Ikke vis fasiten med en gang: la elevene gjette hva som er tilfeldig og kjøre programmet flere ganger.
- Hvis de står fast, pek på oppdragskommentarene øverst i Python-fila.
- Kjerneideen er at `antall_mistenkte` styrer trekningen og valgene elevene får. Hintet sier om det hemmelige nummeret er høyere eller lavere enn gjetningen.
- Det er helt greit om de ikke rekker bonusoppdraget; det viktigste er å kjøre, endre og teste.

## Slik kjører dere

1. Åpne `romstasjon_mysteriet.py` i VS Code.
2. Trykk på trekanten **Run Python File** oppe til høyre.
3. Skriv svaret i terminalen nederst og trykk Enter.
