import random

# Velkommen til Romstasjon Mysteriet!
# En alien har stjålet nøkkelkortet. Klarer dere å finne den skyldige?
#
# ELEVOPPDRAG:
# 1. Endre robotnavnet og teksten under. Hva skjer når dere kjører programmet?
# 2. Endre antall mistenkte fra 10 til et annet tall. Hva skjer med hintene?
# 3. Bonus: Endre poengsummen eller finn på en morsom premie.

robot = "BIP"
antall_mistenkte = 10
maks_forsok = 4

print("=" * 38)
print("     ROMSTASJON MYSTERIET")
print("=" * 38)
print(f"{robot}: Alarm! Nøkkelkortet er borte!")
print(f"Det er {antall_mistenkte} aliens i kontrollrommet.")
print(f"Finn den skyldige på maks {maks_forsok} forsøk.")
print()

skyldig = random.randint(1, antall_mistenkte)

for forsok in range(1, maks_forsok + 1):
    valg_tekst = input(
        f"Forsøk {forsok}/{maks_forsok} – velg en alien fra 1 til {antall_mistenkte}: "
    )

    if not valg_tekst.isdigit():
        print("Skriv et helt tall, for eksempel 4.")
        continue

    valg = int(valg_tekst)

    if valg < 1 or valg > antall_mistenkte:
        print(f"Velg et nummer fra 1 til {antall_mistenkte}.")
        continue

    if valg == skyldig:
        print()
        print(f"Riktig! Alien nummer {skyldig} hadde nøkkelkortet!")
        print("Dere reddet romstasjonen!")
        print("Belønning: 100 rompoeng og en pose månekjeks.")
        break

    if valg < skyldig:
        print("Ikke helt! Gjett litt lenger ut i rekka (et høyere nummer).")
    else:
        print("Ikke helt! Gjett litt tidligere i rekka (et lavere nummer).")
else:
    print()
    print("Dere brukte opp forsøkene!")
    print(f"Det var alien nummer {skyldig} som tok nøkkelkortet!")

print()
print(f"{robot}: Takk for hjelpen, romdetektiver!")
