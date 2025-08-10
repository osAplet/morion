import requests
from PIL import Image
import datetime

# 🌍 Souřadnice pro Drozdov
latitude = 50.003
longitude = 13.833

# 🌐 Open-Meteo API
url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m,weathercode,wind_speed_10m"

response = requests.get(url)
data = response.json()

# 📊 Data
teplota = data["current"]["temperature_2m"]
vitr = data["current"]["wind_speed_10m"]
kod = data["current"]["weathercode"]

# 🧠 Převod kódu na název ikony
def kod_na_ikonu(kod):
    if kod == 0:
        return "clear.png"
    elif kod in [1, 2, 3]:
        return "cloudy.png"
    elif kod in [45, 48]:
        return "unknown.png"
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
hodina = datetime.datetime.now().hour
if hodina >= 20 or hodina < 6:
    ikona = "naithcolor.png"

# 📂 Cesta k ikoně
ikona_path = f"/data/data/com.termux/files/home/MEAI/rosnicka/ikony/{ikona}"

# 🖼️ Zobraz
try:
    img = Image.open(ikona_path)
    img.show()
    print(f"🌡️ Teplota: {teplota}°C")
    print(f"🌬️ Vítr: {vitr} m/s")
    print(f"⛅ Kód počasí: {kod} → Ikona: {ikona}")
except Exception as e:
    print(f"❌ Chyba: {e}")

import os
from datetime import datetime

# 📅 Získání aktuálního času
cas = datetime.now().strftime("%Y-%m-%d_%H-%M")

# 📄 Název souboru
soubor = f"/data/data/com.termux/files/home/MEAI/rosnicka/archiv/vydech_{cas}.txt"

# 📝 Obsah výdechu
obsah = f"""
🌡️ Teplota: {teplota}°C
🌬️ Vítr: {vitr} m/s
⛅ Kód počasí: {kod}
🖼️ Ikona: {ikona}
📅 Čas: {cas}
"""

# 💾 Uložení do souboru
with open(soubor, "w") as f:
    f.write(obsah.strip())

print(f"📁 Výdech uložen do: {soubor}")
