import os
import re

archiv_slozka = "/data/data/com.termux/files/home/MEAI/rosnicka/archiv"

# Výchozí hodnoty
default_hodnoty = {
    "Teplota": "20.0",
    "Vlhkost": "50",
    "Vítr": "2.0",
    "Tlak": "1010"
}

# Najdi poslední výdech
soubory = sorted([f for f in os.listdir(archiv_slozka) if f.startswith("vydech_")])
if not soubory:
    print("❌ Žádné výdechy nenalezeny.")
    exit()

posledni = os.path.join(archiv_slozka, soubory[-1])
with open(posledni, "r") as f:
    obsah = f.read()

print(f"\n🔧 Oprava výdechu: {soubory[-1]}\n")

# Oprava chybějících hodnot
for label, default in default_hodnoty.items():
    if re.search(fr"{label}: ([\d\.]+)", obsah):
        print(f"✅ {label} nalezena")
    else:
        print(f"➕ Doplněno: {label}: {default}")
        obsah += f"\n{label}: {default}"

# Ulož zpět
with open(posledni, "w") as f:
    f.write(obsah.strip() + "\n")

print("\n✅ Výdech opraven a uložen.")
