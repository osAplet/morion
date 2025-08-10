import json

data_path = "/data/data/com.termux/files/home/MEAI/rosnicka/data/animace/teploty.json"
svg_path = "/data/data/com.termux/files/home/MEAI/rosnicka/assets/svg/vlhkost_graf.svg"

with open(data_path, "r", encoding="utf-8") as f:
    data = json.load(f)

width = 400
height = 200
padding = 40
max_v = max([d["vlhkost"] for d in data]) + 5
min_v = min([d["vlhkost"] for d in data]) - 5
scale = (height - 2 * padding) / (max_v - min_v)

svg = f"""<svg width="{width}" height="{height}" xmlns="http://www.w3.org/2000/svg">
  <rect width="100%" height="100%" fill="#e3f2fd"/>
  <text x="{width//2}" y="20" text-anchor="middle" font-size="16">💧 Vývoj vlhkosti</text>
"""

points = []
for i, entry in enumerate(data):
    x = padding + i * ((width - 2 * padding) / (len(data) - 1))
    y = height - padding - (entry["vlhkost"] - min_v) * scale
    points.append((x, y))
    svg += f'<circle cx="{x:.1f}" cy="{y:.1f}" r="4" fill="#0288d1"/>\n'
    svg += f'<text x="{x:.1f}" y="{height - 10}" font-size="10" text-anchor="middle">{entry["čas"]}</text>\n'

# Spojnice
for i in range(len(points) - 1):
    x1, y1 = points[i]
    x2, y2 = points[i + 1]
    svg += f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="#01579b" stroke-width="2"/>\n'

svg += "</svg>"

with open(svg_path, "w", encoding="utf-8") as f:
    f.write(svg)

print("✅ SVG graf vlhkosti vytvořen.")
