import requests
import os
from datetime import datetime

# 📡 Stáhni aktuální radarový snímek z ČHMÚ
radar_url = "https://portal.chmi.cz/files/portal/docs/meteo/rad/data/latest.png"
radar_cil = "/data/data/com.termux/files/home/MEAI/rosnicka/media/radar.png"

try:
    radar_data = requests.get(radar_url)
    with open(radar_cil, "wb") as f:
        f.write(radar_data.content)
except Exception as e:
    print(f"⚠️ Chyba při stahování radaru: {e}")

# 🌍 Souřadnice pro Drozdov
latitude = 50.003
longitude = 13.833

# 🌐 Open-Meteo API
url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m,weathercode,wind_speed_10m"
response = requests.get(url)
data = response.json()

# 📊 Získání dat
teplota = data["current"]["temperature_2m"]
vitr = data["current"]["wind_speed_10m"]
kod = data["current"]["weathercode"]

# 🧠 Převod kódu na ikonu
def kod_na_ikonu(kod):
    if kod == 0:
        return "clear.png"
    elif kod in [1, 2, 3]:
        return "cloudy.png"
    elif kod in [45, 48]:
        return "fog.png"
    elif 51 <= kod <= 67 or 80 <= kod <= 82:
        return "rain.png"
    elif 71 <= kod <= 77 or 85 <= kod <= 86:
        return "snow.png"
    elif kod in [95, 96, 97, 98, 99]:
        return "thunderstorm.png"
    else:
        return "unknown.png"

ikona = kod_na_ikonu(kod)

# 🌙 Noční režim
hodina = datetime.now().hour
if hodina >= 20 or hodina < 6:
    ikona = "naithcolor.png"

# 📂 Cesty
archiv_slozka = "/data/data/com.termux/files/home/MEAI/rosnicka/archiv"
media_slozka = "/data/data/com.termux/files/home/MEAI/rosnicka/media"
cas = datetime.now().strftime("%Y-%m-%d_%H-%M")
cas_svg = datetime.now().strftime("%Y%m%dT%H%M")

# 📝 Výdech
soubor_vydech = f"{archiv_slozka}/vydech_{cas}.txt"
obsah = f"""
🌡️ Teplota: {teplota}°C
🌬️ Vítr: {vitr} m/s
⛅ Kód počasí: {kod}
🖼️ Ikona: {ikona}
📅 Čas: {cas}
"""
with open(soubor_vydech, "w") as f:
    f.write(obsah.strip())

# 🎨 Orbitální SVG erb s radarovým pozadím
soubor_orbit_svg = f"{archiv_slozka}/erb_orbit_rosnicka_meai_{cas_svg}.svg"
svg_orbit = f"""<?xml version="1.0" encoding="UTF-8"?>
<svg width="400" height="300" xmlns="http://www.w3.org/2000/svg">
  <image href="{media_slozka}/radar.png" x="0" y="0" width="400" height="300"/>
  <circle cx="200" cy="150" r="140" fill="none" stroke="#00796b" stroke-width="4"/>
  <text x="200" y="50" font-size="20" text-anchor="middle" fill="#ffffff">🪐 Orbit Rosnička MEAI</text>
  <text x="200" y="90" font-size="16" text-anchor="middle" fill="#ffffff">Kód {kod}</text>
  <text x="200" y="120" font-size="14" text-anchor="middle" fill="#ffffff">🌡️ {teplota} °C</text>
  <text x="200" y="140" font-size="14" text-anchor="middle" fill="#ffffff">💨 {vitr} m/s</text>
  <text x="200" y="160" font-size="14" text-anchor="middle" fill="#ffffff">🕒 {cas}</text>
  <text x="200" y="200" font-size="12" text-anchor="middle" fill="#ffffff">„Orbit MEAI nevydává hluk. On vydechuje paměť.“</text>
</svg>
"""
with open(soubor_orbit_svg, "w") as f:
    f.write(svg_orbit)

# 📲 Otevři orbitální erb v Androidu
os.system(f"termux-open {soubor_orbit_svg}")

# 📋 Logování
with open(f"{archiv_slozka}/log_rosnicka.txt", "a") as log:
    log.write(f"\n🕒 Orbitální výdech v {cas} → {soubor_orbit_svg}")
