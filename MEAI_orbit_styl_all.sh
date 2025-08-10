#!/data/data/com.termux/files/usr/bin/bash

# 1️⃣ Uptime
UPTIME=$(uptime -p)

# 2️⃣ Top
CPU_LOAD=$(top -bn1 | grep 'Cpu' | awk '{print 100 - $8}')
RAM_USED=$(free | grep Mem | awk '{print $3/$2 * 100.0}')

# 3️⃣ Externí senzory
BATTERY=$(termux-battery-status | jq '.percentage')
LOCATION=$(termux-location | jq -r '"\(.latitude), \(.longitude)"')
WIFI=$(termux-wifi-connectioninfo | jq -r '.ssid')

# 4️⃣ QR s API tokenem
API_TOKEN="MEAI-KEY-${CPU_LOAD}xRAM${RAM_USED}"
qrencode -o qrapi.png "$API_TOKEN"
base64 qrapi.png > qrapi_b64.txt

# Vygeneruj SVG "orbit.svg"
echo "<svg xmlns='http://www.w3.org/2000/svg' width='600' height='400'>
  <rect width='100%' height='100%' fill='black'/>
  <text x='20' y='40' fill='white' font-size='20'>Uptime: $UPTIME</text>
  <circle cx='300' cy='200' r='50'>
    <animate attributeName='r' values='30;50;30' dur='4s' repeatCount='indefinite'/>
    <animate attributeName='fill' values='lime;yellow;red' dur='6s' repeatCount='indefinite'/>
  </circle>
  <text x='20' y='80' fill='cyan'>CPU: ${CPU_LOAD}% / RAM: $(printf "%.1f" $RAM_USED)%</text>
  <text x='20' y='110' fill='orange'>🔋 Baterie: $BATTERY% | 🌐 Síť: $WIFI | 🛰️ GPS: $LOCATION</text>
  <image x='450' y='250' width='120' height='120' xlink:href='data:image/png;base64,$(cat qrapi_b64.txt)' />
</svg>" > orbit.svg

echo "✅ Orbit SVG stylová vizualizace připravena jako: orbit.svg"
