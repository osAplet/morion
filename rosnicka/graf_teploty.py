import os
import re
from datetime import datetime

archiv_slozka = "/data/data/com.termux/files/home/MEAI/rosnicka/archiv"
soubory = sorted([f for f in os.listdir(archiv_slozka) if f.startswith("vydech_")])

data = []
for soubor in soubory[-24:]:  # posledních 24 výdechů
    path = os.path.join(archiv_slozka, soubor)
    with open(path, "r") as f:
        obsah = f.read()
    match = re.search(r"Teplota: ([\d\.]+)", obsah)
    if match:
        teplota = float(match.group(1))
        cas = soubor.replace("vydech_", "").replace(".txt", "")
        data.append((cas, teplota))

# SVG graf
width = 600
height = 200
padding = 40
max_temp = max([t for _, t in data]) + 2
min_temp = min([t for _, t in data]) - 2
scale = (height - 2 * padding) / (max_temp - min_temp)

svg = f"""<svg width="{width}" height="{height}" xmlns="http://www.w3.org/2000/svg">
  <rect width="100%" height="100%" fill="#f0f8ff"/>
  <text x="{width//2}" y="20" text-anchor="middle" font-size="16">📈 Vývoj teploty</text>
"""

for i, (cas, temp) in enumerate(data):
    x = padding + i * ((width - 2 * padding) / len(data))
    y = height - padding - (temp - min_temp) * scale
    svg += f'<circle cx="{x}" cy="{y}" r="3" fill="#00796b"/>\n'
    svg += f'<text x="{x}" y="{height - 10}" font-size="10" text-anchor="middle" fill="#333">{cas[-5:]}</text>\n'

svg += "</svg>"

with open(f"{archiv_slozka}/graf_teploty.svg", "w") as f:
    f.write(svg)

print("✅ Graf teploty vytvořen.")
