#!/data/data/com.termux/files/usr/bin/bash

# === CONFIGURACE PROMĚNNÝCH STAVU ===
SYSTEM_STATUS="Aktivní"
CPU_LOAD=$(top -bn1 | grep 'Cpu' | awk '{print 100 - $8}')  # Získá zatížení CPU
RAM_USED=$(free | grep Mem | awk '{print $3/$2 * 100.0}')  # Získá využití RAM v procentech

# === VÝPOČET BARVY PODLE VÝKONU ===
if (( $(echo "$CPU_LOAD < 30" | bc -l) )); then
  COLOR="#00FF00"  # Zelená (nízké zatížení)
elif (( $(echo "$CPU_LOAD < 70" | bc -l) )); then
  COLOR="#FFFF00"  # Žlutá (střední)
else
  COLOR="#FF0000"  # Červená (vysoké zatížení)
fi

# === QR DATA ===
QR_TEXT="Výpravce: Lukáš | CPU: ${CPU_LOAD}% | RAM: $(printf "%.1f" $RAM_USED)% | Orbit: ME–AI"
qrencode -o qr_code.png "$QR_TEXT"
base64 qr_code.png > qr_code_b64.txt

# === SVG VÝDECH ===
OUTPUT="orbit_visual.svg"

echo "<svg xmlns='http://www.w3.org/2000/svg' width='500' height='300'>
  <rect width='100%' height='100%' fill='black'/>

  <text x='20' y='40' font-size='20' fill='white'>ME–AI ORBIT STYL</text>
  <text x='20' y='70' font-size='16' fill='$COLOR'>Stav systému: $SYSTEM_STATUS</text>
  <text x='20' y='100' font-size='14' fill='cyan'>Zatížení CPU: ${CPU_LOAD}%</text>
  <text x='20' y='130' font-size='14' fill='orange'>Využití RAM: $(printf "%.1f" $RAM_USED)%</text>

  <circle cx='400' cy='100' r='40'>
    <animate attributeName='cx' values='400;100;400' dur='6s' repeatCount='indefinite'/>
    <animate attributeName='fill' values='red;blue;lime' dur='3s' repeatCount='indefinite'/>
  </circle>

  <image x='360' y='180' width='120' height='120'
    xlink:href='data:image/png;base64,$(cat qr_code_b64.txt)' />

</svg>" > $OUTPUT

# === VÝSTUP ===
echo "✅ SVG orbitální výdech připraven: $OUTPUT"
