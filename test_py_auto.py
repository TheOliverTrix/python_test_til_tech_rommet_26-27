import pyautogui
import tkinter as tk


OPPDATERING_MS = 100

FARGER = {
    "svart": (0, 0, 0),
    "hvit": (255, 255, 255),
    "rød": (255, 0, 0),
    "grønn": (0, 128, 0),
    "blå": (0, 0, 255),
    "gul": (255, 255, 0),
    "oransje": (255, 165, 0),
    "lilla": (128, 0, 128),
    "rosa": (255, 192, 203),
    "brun": (165, 42, 42),
    "turkis": (0, 128, 128),
    "grå": (128, 128, 128),
}


def rgb_til_hex(rgb):
    return "#{:02X}{:02X}{:02X}".format(*rgb)


def finn_fargenavn(rgb):
    return min(
        FARGER,
        key=lambda navn: sum(
            (rgb[i] - FARGER[navn][i]) ** 2
            for i in range(3)
        ),
    )


def main():
    vindu = tk.Tk()
    vindu.title("Pikselfinner")
    vindu.geometry("380x340")
    vindu.resizable(False, False)
    vindu.attributes("-topmost", True)

    tk.Label(
        vindu,
        text="Hold pekeren over en piksel",
        font=("Segoe UI", 14, "bold"),
    ).pack(pady=(16, 8))
    tk.Label(
        vindu,
        text="Flytt vinduet til siden for å lese farger bak det.",
    ).pack()

    fargeprove = tk.Frame(vindu, bg="#000000", height=90, relief="sunken", bd=2)
    fargeprove.pack(fill="x", padx=24, pady=8)
    fargeprove.pack_propagate(False)

    navn_tekst = tk.Label(vindu, font=("Segoe UI", 13, "bold"))
    navn_tekst.pack(pady=(8, 2))
    hex_tekst = tk.Label(vindu, font=("Consolas", 14))
    hex_tekst.pack(pady=2)
    rgb_tekst = tk.Label(vindu, font=("Consolas", 11))
    rgb_tekst.pack(pady=2)
    posisjon_tekst = tk.Label(vindu, font=("Segoe UI", 10))
    posisjon_tekst.pack(pady=2)
    status_tekst = tk.Label(vindu, text="Måler musepekeren …", font=("Segoe UI", 9))
    status_tekst.pack(pady=2)

    def oppdater_farge():
        try:
            x, y = pyautogui.position()
            rgb = tuple(pyautogui.pixel(x, y))
        except pyautogui.FailSafeException:
            status_tekst.configure(
                text="Sikkerhetsstopp: flytt pekeren bort fra hjørnet øverst til venstre."
            )
            vindu.after(OPPDATERING_MS, oppdater_farge)
            return

        hex_farge = rgb_til_hex(rgb)
        navn = finn_fargenavn(rgb)
        fargeprove.configure(bg=hex_farge)
        navn_tekst.configure(text=f"Nærmeste fargenavn: {navn}")
        hex_tekst.configure(text=f"HEX: {hex_farge}")
        rgb_tekst.configure(text=f"RGB: {rgb}")
        posisjon_tekst.configure(text=f"Posisjon: x={x}, y={y}")
        status_tekst.configure(text="Måler musepekeren …")
        vindu.after(OPPDATERING_MS, oppdater_farge)

    vindu.after(0, oppdater_farge)
    vindu.mainloop()


if __name__ == "__main__":
    main()