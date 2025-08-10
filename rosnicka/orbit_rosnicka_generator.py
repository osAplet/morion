import os
import re

archiv_slozka = "/data/data/com.termux/files/home/MEAI/rosnicka/archiv"
svg_cesta = "/data/data/com.termux/files/home/MEAI/rosnicka/assets/svg/orbit_rosnicka_meai.svg"

# Najdi poslední výdech
soubory = sorted([f for f in os.listdir(archiv_slozka) if f.startswith("vydech_")])
if not soubory:
    print("❌ Žádné výdechy nenalezeny.")
    exit()

posledni = os.path.join(archiv_slozka, soubory[-1])
with open(posledni, "r") as f:
    obsah = f.read()

# Získání hodnot
def najdi(label, default="?"):
    match = re.search(fr"{label}: ([\d\.]+)", obsah)
    return match.group(1) if match else default

teplota = najdi("Teplota")
vlhkost = najdi("Vlhkost")
vitr = najdi("Vítr")
tlak = najdi("Tlak")

# SVG obsah
svg = f"""<svg width="300" height="300"
     xmlns="http://www.w3.org/2000/svg"
     xmlns:xlink="http://www.w3.org/1999/xlink">

  <style>
    .orbit {{
      fill: none;
      stroke-width: 2;
      stroke-dasharray: 4 2;
    }}
    .text {{
      font-family: sans-serif;
      font-size: 18px;
      fill: #ffffff;
      text-anchor: middle;
    }}
    .hidden {{ visibility: hidden; }}
    .visible {{ visibility: visible; }}
    .background {{ fill: #0a0f1c; }}
  </style>

  <rect width="300" height="300" class="background"/>

  <!-- Orbitální kruhy -->
  <circle cx="150" cy="150" r="100" class="orbit" stroke="#00ffe0"/>
  <circle cx="150" cy="150" r="80" class="orbit" stroke="#ff4081"/>
  <circle cx="150" cy="150" r="60" class="orbit" stroke="#40c4ff"/>
  <circle cx="150" cy="150" r="40" class="orbit" stroke="#cddc39"/>

  <!-- Vrstvy -->
  <text id="vrstva1" x="150" y="140" class="text visible">🌡️ Teplota: {teplota} °C</text>
  <text id="vrstva2" x="150" y="140" class="text hidden">💧 Vlhkost: {vlhkost} %</text>
  <text id="vrstva3" x="150" y="140" class="text hidden">🌪️ Vítr: {vitr} m/s</text>
  <text id="vrstva4" x="150" y="140" class="text hidden">📉 Tlak: {tlak} hPa</text>

  <!-- Cyklické přepínání vrstev -->
  <!-- Vrstva 1: Teplota -->
  <set xlink:href="#vrstva1" attributeName="visibility" to="visible" begin="0s;32s" dur="8s" repeatCount="indefinite"/>
  <set xlink:href="#vrstva1" attributeName="visibility" to="hidden" begin="8s;40s" dur="0.1s" repeatCount="indefinite"/>

  <!-- Vrstva 2: Vlhkost -->
  <set xlink:href="#vrstva2" attributeName="visibility" to="visible" begin="8s;40s" dur="8s" repeatCount="indefinite"/>
  <set xlink:href="#vrstva2" attributeName="visibility" to="hidden" begin="16s;48s" dur="0.1s" repeatCount="indefinite"/>

  <!-- Vrstva 3: Vítr -->
  <set xlink:href="#vrstva3" attributeName="visibility" to="visible" begin="16s;48s" dur="8s" repeatCount="indefinite"/>
  <set xlink:href="#vrstva3" attributeName="visibility" to="hidden" begin="24s;56s" dur="0.1s" repeatCount="indefinite"/>

  <!-- Vrstva 4: Tlak -->
  <set xlink:href="#vrstva4" attributeName="visibility" to="visible" begin="24s;56s" dur="8s" repeatCount="indefinite"/>
  <set xlink:href="#vrstva4" attributeName="visibility" to="hidden" begin="32s;64s" dur="0.1s" repeatCount="indefinite"/>
</svg>
"""

# Ulož SVG
with open(svg_cesta, "w", encoding="utf-8") as f:
    f.write(svg)

print(f"✅ Orbitální SVG vytvořeno z výdechu: {soubory[-1]}")
