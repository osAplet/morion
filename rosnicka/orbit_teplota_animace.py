import json
import math

# Cesty
data_path = "/data/data/com.termux/files/home/MEAI/rosnicka/data/animace/teploty.json"
svg_path = "/data/data/com.termux/files/home/MEAI/rosnicka/assets/svg/teplota_animace.svg"

# Načti data
with open(data_path, "r", encoding="utf-8") as f:
    data = json.load(f)

# SVG hlavička
svg = f"""<?xml version="1.0" encoding="UTF-8"?>
<svg width="300" height="300" xmlns="http://www.w3.org/2000/svg">
  <rect width="100%" height="100%" fill="#f0f8ff"/>
  <g transform="rotate(0 150 150)">
    <animateTransform attributeName="transform" attributeType="XML"
                      type="rotate" from="0 150 150" to="360 150 150"
                      dur="20s" repeatCount="indefinite"/>
"""

# Vykresli body
center_x = 150
center_y = 150
radius = 100

def barva_teploty(t):
    if t < 10: return "#00f"
    elif t < 20: return "#0ff"
    elif t < 25: return "#f90"
    else: return "#f00"

for i, entry in enumerate(data):
    angle_deg = (360 / len(data)) * i
    angle_rad = math.radians(angle_deg)
    x = center_x + radius * math.cos(angle_rad)
    y = center_y + radius * math.sin(angle_rad)
    r = entry["vlhkost"] / 20  # škálování vlhkosti
    barva = barva_teploty(entry["teplota"])
    svg += f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r:.1f}" fill="{barva}"/>\n'
    svg += f'<text x="{x:.1f}" y="{y + 12:.1f}" font-size="10" text-anchor="middle" fill="#333">{entry["čas"]}</text>\n'

svg += "</g></svg>"

# Ulož SVG
with open(svg_path, "w", encoding="utf-8") as f:
    f.write(svg)

print("✅ Orbitální SVG animace vytvořena.")
