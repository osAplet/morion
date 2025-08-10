import os
from datetime import datetime

# 📁 Cesta k archivu
archiv_slozka = "/data/data/com.termux/files/home/MEAI/rosnicka/archiv"

# 🔍 Najdi nejnovější výdech
soubory = sorted([f for f in os.listdir(archiv_slozka) if f.startswith("vydech_")], reverse=True)
if not soubory:
    print("❌ Nenalezen žádný výdechový soubor.")
    exit(1)

posledni_vydech = os.path.join(archiv_slozka, soubory[0])

# 📖 Načti obsah
with open(posledni_vydech, "r") as f:
    obsah = f.read()

# 🧠 Získání dat z textu
lines = obsah.splitlines()
teplota = lines[0].split(":")[1].strip()
vitr = lines[1].split(":")[1].strip()
popis = lines[2].split(":")[1].strip()
ikona = lines[3].split(":")[1].strip()
cas = lines[4].split(":")[1].strip()

# 🖼️ SVG šablona
svg = f"""<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<svg width="300" height="200" xmlns="http://www.w3.org/2000/svg">
  <rect width="100%" height="100%" fill="#e0f7fa"/>
  <text x="150" y="40" font-size="20" text-anchor="middle" fill="#00796b">Rosnička MEAI</text>
  <text x="150" y="70" font-size="16" text-anchor="middle" fill="#004d40">{popis}</text>
  <text x="150" y="100" font-size="14" text-anchor="middle" fill="#00695c">🌡️ {teplota} °C</text>
  <text x="150" y="120" font-size="14" text-anchor="middle" fill="#00695c">💨 {vitr}</text>
  <text x="150" y="140" font-size="14" text-anchor="middle" fill="#00695c">🕒 {cas}</text>
  <text x="150" y="170" font-size="24" text-anchor="middle">{ikona}</text>
</svg>
"""

# 📁 Uložení SVG
soubor_svg = os.path.join(archiv_slozka, f"erb_rosnicka_meai_{datetime.now().strftime('%Y%m%dT%H%M')}.svg")
with open(soubor_svg, "w") as f:
    f.write(svg)

print(f"✅ SVG erb vytvořen: {soubor_svg}")

os.system("python ~/MEAI/rosnicka/vytvor_erb.py")
