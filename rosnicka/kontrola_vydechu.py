import os
import re

archiv_slozka = "/data/data/com.termux/files/home/MEAI/rosnicka/archiv"

# Najdi poslední výdech
soubory = sorted([f for f in os.listdir(archiv_slozka) if f.startswith("vydech_")])
if not soubory:
    print("❌ Žádné výdechy nenalezeny.")
    exit()

posledni = os.path.join(archiv_slozka, soubory[-1])
with open(posledni, "r") as f:
    obsah = f.read()

# Kontrola hodnot
def zkontroluj(label):
    match = re.search(fr"{label}: ([\d\.]+)", obsah)
    if match:
        print(f"✅ {label}: {match.group(1)}")
        return True
    else:
        print(f"❌ Chybí: {label}")
        return False

print(f"\n🔍 Kontrola výdechu: {soubory[-1]}\n")
zkontroluj("Teplota")
zkontroluj("Vlhkost")
zkontroluj("Vítr")
zkontroluj("Tlak")
