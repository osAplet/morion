from PIL import Image

# Cesta k ikoně
ikona_path = "/data/data/com.termux/files/home/MEAI/rosnicka/ikony/rain.png"

# Otevři a zobraz
img = Image.open(ikona_path)
img.show()
