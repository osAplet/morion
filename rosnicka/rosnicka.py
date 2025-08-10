from PIL import Image
import datetime

# 🌦️ Zadej typ počasí ručně (nebo později z API)
pocasi = input("Zadej počasí (rain, snow, clear...): ").strip()
# 🕒 Zjisti aktuální hodinu
hodina = datetime.datetime.now().hour

# 🌙 Noční režim
if hodina >= 20 or hodina < 6:
    ikona = "naithcolor.png"
else:
    ikona = f"{pocasi}.png"

# 📂 Cesta k ikoně
ikona_path = "/data/data/com.termux/files/home/MEAI/rosnicka/ikony/" + ikona

# 🖼️ Zobraz obrázek
try:
    img = Image.open(ikona_path)
    img.show()
    print(f"✅ Zobrazeno: {ikona_path}")
except Exception as e:
    print(f"❌ Chyba: {e}")
