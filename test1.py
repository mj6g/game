import time
import threading

# Képernyő mérete
SZELESSEG = 24
MAGASSAG = 10

# Karakter pozíciója és animációs képkockái (3 sor magas ASCII figura)
jatekos_x = 5
jatekos_y = 3
karakter_animacio = [
    [
        " O ",
        "/|\\",
        "/ \\"
    ],
    [
        " O/",
        "/| ",
        "/ \\"
    ]
]

aktualis_frame = 0
fut_a_jatek = True

def kepernyo_rajzolasa():
    """Háttérszál, ami folyamatosan írja az animált képkockákat a fájlba."""
    global aktualis_frame
    while fut_a_jatek:
        # Üres pálya létrehozása szóközökkel
        palya = [[" " for _ in range(SZELESSEG)] for _ in range(MAGASSAG)]

        # Karakter rámásolása a pályára az aktuális fázisban
        figura = karakter_animacio[aktualis_frame]
        for sor_idx, sor in enumerate(figura):
            for oszlop_idx, karakter in enumerate(sor):
                px = jatekos_x + oszlop_idx
                py = jatekos_y + sor_idx
                if 0 <= px < SZELESSEG and 0 <= py < MAGASSAG:
                    palya[py][px] = karakter

        # Keret és szöveg összeállítása
        keret_felso = "+" + "-" * SZELESSEG + "+"
        sorok = [keret_felso]
        for sor in palya:
            sorok.append("|" + "".join(sor) + "|")
        sorok.append(keret_felso)
        sorok.append(f"Pozicio: X={jatekos_x}, Y={jatekos_y}")

        # Írás a fájlba (Windows fájlzárolás elleni védelemmel)
        try:
            with open("kepernyo.txt", "w", encoding="utf-8") as f:
                f.write("\n".join(sorok))
        except PermissionError:
            # Ha a szövegszerkesztő pont ebben az ezredmásodpercben olvassa a fájlt,
            # egyszerűen kihagyjuk ezt a képkockát, hogy ne omoljon össze a program.
            pass

        # Következő animációs fázisra váltás
        aktualis_frame = (aktualis_frame + 1) % len(karakter_animacio)
        time.sleep(0.35)  # Animáció sebessége (másodpercben)

# Háttérszál elindítása
rajzolo_szal = threading.Thread(target=kepernyo_rajzolasa, daemon=True)
rajzolo_szal.start()

print("A jatek elindult! Nyisd meg a 'kepernyo.txt' fajlt.")
print("Iranyitas: w (fel), s (le), a (balra), d (jobbra), q (kilepes)")

# Fő ciklus: parancsok fogadása a Thonny parancssorából
while fut_a_jatek:
    parancs = input("Parancs > ").strip().lower()

    if parancs == "w" and jatekos_y > 0:
        jatekos_y -= 1
    elif parancs == "s" and jatekos_y < MAGASSAG - 3:
        jatekos_y += 1
    elif parancs == "a" and jatekos_x > 0:
        jatekos_x -= 1
    elif parancs == "d" and jatekos_x < SZELESSEG - 3:
        jatekos_x += 1
    elif parancs == "q":
        fut_a_jatek = False
        print("Kilepes...")