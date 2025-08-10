import json

data_path = "/data/data/com.termux/files/home/MEAI/rosnicka/data/animace/teploty.json"
svg_path = "/data/data/com.termux/files/home/MEAI/rosnicka/assets/svg/teplota_vlhkost_graf.svg"

with open(data_path, "r", encoding="utf-8") as f:
    data = json.load(f)

width = 400
height = 250
padding = 40

max_t = max([d["teplota"] for d in data]) + 2
min_t = min([d["teplota"] for d in data]) - 2
max_v = max([d["vlhkost"] for d in data]) + 5
min_v = min([d["vlhkost"] for d in data]) - 5

scale_t = (height - 2 * padding) / (max_t - min_t)
scale_v = (height - 2 * padding) / (max_v - min_v)

svg = f"""<svg width="{width}" height="{height}" xmlns="http://www.w3.org/2000/svg">
  <rect width="100%" height="100%" fill="#f9fbe7"/>
  <text x="{width//2}" y="20" text-anchor="middle" font-size="16">📊 Teplota + Vlhkost</text>
  <text x="60" y="35" font-size="12" fill="#d32f2f">● Teplota</text>
  <text x="200" y="35" font-size="12" fill="#1976d2">● Vlhkost</text>
"""

points_t = []
points_v = []

for i, entry in enumerate(data):
    x = padding + i * ((width - 2 * padding) / (len(data) - 1))
    y_t = height - padding - (entry["teplota"] - min_t) * scale_t
    y_v = height - padding - (entry["vlhkost"] - min_v) * scale_v
    points_t.append((x, y_t))
    points_v.append((x, y_v))
    svg += f'<circle cx="{x:.1f}" cy="{y_t:.1f}" r="3" fill="#d32f2f"/>\n'
    svg += f'<circle cx="{x:.1f}" cy="{y_v:.1f}" r="3" fill="#1976d2"/>\n'
    svg += f'<text x="{x:.1f}" y="{height - 10}" font-size="10" text-anchor="middle">{entry["čas"]}</text>\n'

# Spojnice
for i in range(len(points_t) - 1):
    x1, y1 = points_t[i]
    x2, y2 = points_t[i + 1]
    svg += f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="#d32f2f" stroke-width="2"/>\n'

for i in range(len(points_v) - 1):
    x1, y1 = points_v[i]
    x2, y2 = points_v[i + 1]
    svg += f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="#1976d2" stroke-width="2"/>\n'

svg += "</svg>"

with open(svg_path, "w", encoding="utf-8") as f:
    f.write(svg)

print("✅ Kombinovaný SVG graf vytvořen.")
