#!/bin/bash

VYDECH=~/MEAI/rosnicka/vydech.json
HTML=~/MEAI/rosnicka/assets/svg/orbit_rosnicka_meai.html

TEPLOTA=$(jq '.teplota' "$VYDECH")
VLHKOST=$(jq '.vlhkost' "$VYDECH")
VITR=$(jq '.vitr' "$VYDECH")
TLAK=$(jq '.tlak' "$VYDECH")

cat > "$HTML" <<EOF
<!DOCTYPE html>
<html lang="cs">
<head>
  <meta charset="UTF-8">
  <title>🪐 Orbitální Rosnička MEAI</title>
  <style>
    body {
      margin: 0;
      background: #0a0f1c;
      color: #ffffff;
      font-family: sans-serif;
      text-align: center;
    }
    svg {
      width: 100vw;
      height: 100vh;
    }
    .orbit {
      fill: none;
      stroke-width: 2;
      stroke-dasharray: 4 2;
    }
    .text {
      font-size: 4vw;
      fill: #ffffff;
      text-anchor: middle;
      cursor: pointer;
    }
  </style>
</head>
<body>
  <svg viewBox="0 0 300 300">
    <rect width="300" height="300" fill="#0a0f1c"/>
    <circle cx="150" cy="150" r="100" class="orbit" stroke="#00ffe0"/>
    <circle cx="150" cy="150" r="80" class="orbit" stroke="#ff4081"/>
    <circle cx="150" cy="150" r="60" class="orbit" stroke="#40c4ff"/>
    <circle cx="150" cy="150" r="40" class="orbit" stroke="#cddc39"/>

    <text id="vrstva" x="150" y="140" class="text">🌡️ Teplota: ${TEPLOTA} °C</text>
  </svg>

  <script>
    const vrstvy = [
      "🌡️ Teplota: ${TEPLOTA} °C",
      "💧 Vlhkost: ${VLHKOST} %",
      "🌪️ Vítr: ${VITR} m/s",
      "📉 Tlak: ${TLAK} hPa"
    ];
    let index = 0;
    const text = document.getElementById("vrstva");

    function prepni() {
      index = (index + 1) % vrstvy.length;
      text.textContent = vrstvy[index];
    }

    setInterval(prepni, 8000);
    text.addEventListener("click", prepni);
  </script>
</body>
</html>
EOF
