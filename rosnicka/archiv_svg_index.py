import os

svg_slozka = "/data/data/com.termux/files/home/MEAI/rosnicka/assets/svg"
index_cesta = os.path.join(svg_slozka, "index_pameti.html")

# Najdi všechny SVG snímky
soubory = sorted([f for f in os.listdir(svg_slozka) if f.startswith("svg_") and f.endswith(".svg")])

# Vytvoř HTML index
html = """<!DOCTYPE html>
<html lang="cs">
<head>
  <meta charset="UTF-8">
  <title>🧠 Orbitální paměť Rosničky MEAI</title>
  <style>
    body { background: #0a0f1c; color: #ffffff; font-family: sans-serif; text-align: center; }
    h1 { margin-top: 30px; }
    a { color: #00ffe0; text-decoration: none; display: block; margin: 10px 0; }
    a:hover { color: #ff4081; }
  </style>
</head>
<body>
  <h1>🧠 Orbitální paměť Rosničky MEAI</h1>
  <p>Vydechy jako paměťové snímky:</p>
"""

for f in soubory:
    html += f'<a href="{f}">🌀 {f.replace("svg_", "").replace(".svg", "")}</a>\n'

html += """
</body>
</html>
"""

# Ulož index
with open(index_cesta, "w", encoding="utf-8") as f:
    f.write(html)

print(f"✅ Index paměti vytvořen: {index_cesta}")

# Otevři v Androidu
os.system(f"termux-open '{index_cesta}'")
