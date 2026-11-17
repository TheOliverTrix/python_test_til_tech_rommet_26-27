import matplotlib.pyplot as plt


START_HUNNER = 20
START_HANNER = 20
# Startrevene er voksne i modellen og jakter fra første simuleringsår.
START_REV = 5

MAKS_BESTAND_HARER = 500
MAKS_ALDER = 10
# Dette er justerbare eksempelverdier, ikke målinger fra en bestemt øy.
HARER_PER_HUNN_PER_AR = 2
REV_UNGER_PER_VOKS_PER_AR = 0.1
# Endre tallet for å velge hvor mange harer hver voksen rev spiser per år.
HARER_SPIST_PER_REV_PER_AR = 3
ANTALL_AR = 30


def aldre_ett_ar(populasjon):
    """Flytt dyrene ett alderstrinn opp; de eldste faller ut av modellen."""
    return [0.0] + populasjon[:-1]


def simuler_okosystem(start_hunner, start_hanner, start_rever, maks_harer, antall_ar):
    """Simuler bestander som aldersgrupper; tallene er gjennomsnitt og kan bli desimaltall."""
    if antall_ar < 1:
        raise ValueError("Simuleringen må vare minst ett år.")
    if maks_harer <= 0:
        raise ValueError("Maksbestanden må være større enn null.")
    if min(start_hunner, start_hanner, start_rever) < 0:
        raise ValueError("Startbestandene kan ikke være negative.")

    # Indeks 0 er nyfødte, indeks 10 er ti år gamle dyr.
    # Startdyrene settes til ett år fordi alder ikke er kjent.
    hunner = [0.0] * (MAKS_ALDER + 1)
    hanner = [0.0] * (MAKS_ALDER + 1)
    rever = [0.0] * (MAKS_ALDER + 1)
    hunner[1] = float(start_hunner)
    hanner[1] = float(start_hanner)
    rever[1] = float(start_rever)

    harebestander = [sum(hunner) + sum(hanner)]
    revebestander = [sum(rever)]

    for _ in range(1, antall_ar):
        antall_harer = sum(hunner) + sum(hanner)
        voksne_rever = sum(rever[1:])

        # Reven tar et gjennomsnittlig antall harer; jakten fordeles på bestanden.
        harer_spist = min(
            antall_harer,
            voksne_rever * HARER_SPIST_PER_REV_PER_AR,
        )
        if antall_harer > 0:
            overlevelsesandel = (antall_harer - harer_spist) / antall_harer
            hunner = [antall * overlevelsesandel for antall in hunner]
            hanner = [antall * overlevelsesandel for antall in hanner]

        voksne_hunner = sum(hunner[1:])
        reveunger = voksne_rever * REV_UNGER_PER_VOKS_PER_AR
        if voksne_rever > 0:
            matfaktor = min(
                1.0,
                antall_harer / (voksne_rever * HARER_SPIST_PER_REV_PER_AR),
            )
            reveunger *= matfaktor

        hareunger = voksne_hunner * HARER_PER_HUNN_PER_AR

        hunner = aldre_ett_ar(hunner)
        hanner = aldre_ett_ar(hanner)
        rever = aldre_ett_ar(rever)

        ledig_plass = max(0, maks_harer - sum(hunner) - sum(hanner))
        hareunger = min(hareunger, ledig_plass)
        hunner[0] = hareunger / 2
        hanner[0] = hareunger / 2
        rever[0] = reveunger

        harebestand = sum(hunner) + sum(hanner)
        if harebestand > maks_harer:
            faktor = maks_harer / harebestand
            hunner = [antall * faktor for antall in hunner]
            hanner = [antall * faktor for antall in hanner]

        harebestander.append(sum(hunner) + sum(hanner))
        revebestander.append(sum(rever))

    return harebestander, revebestander


def vis_simulering():
    harebestander, revebestander = simuler_okosystem(
        START_HUNNER,
        START_HANNER,
        START_REV,
        MAKS_BESTAND_HARER,
        ANTALL_AR,
    )
    ar = range(1, ANTALL_AR + 1)

    print(f"År 1: {START_HUNNER} hunner, {START_HANNER} hanner og {START_REV} rever.")
    print(
        f"Etter {ANTALL_AR} år: omtrent {harebestander[-1]:.0f} harer "
        f"og {revebestander[-1]:.0f} rever."
    )

    figur, (hareakse, reveakse) = plt.subplots(2, 1, sharex=True)
    hareakse.plot(ar, harebestander, marker="o", color="forestgreen")
    hareakse.set_title("Harer")
    hareakse.set_ylabel("Antall harer")
    hareakse.grid(True)

    reveakse.plot(ar, revebestander, marker="o", color="darkorange")
    reveakse.set_title("Rever")
    reveakse.set_xlabel("År")
    reveakse.set_ylabel("Antall rever")
    reveakse.grid(True)

    figur.suptitle("Simulering av harer og rever på en norsk øy")
    figur.tight_layout()
    plt.show()


if __name__ == "__main__":
    vis_simulering()
