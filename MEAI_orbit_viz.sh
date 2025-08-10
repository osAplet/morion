#!/data/data/com.termux/files/usr/bin/bash

CONFIG="orbit_config.json"
SVG_PATH="orbit_visual.svg"

# Načíst nastavení
CPU_USAGE=$(top -bn1 | grep "CPU" | awk '{print $2}' | cut -d'%' -f1)
CONNECTION=$(ping -c 1 google.com &> /dev/null && echo "connected" || echo "disconnected")
SENSOR_DATA=$(termux-sensor -n accelerometer | jq '.')

# Aktivace zvuku & vibrace
if [ "$CPU_USAGE" -gt 85 ]; then
  termux-vibrate -d 1000
  termux-media-player play alert_cpu.mp3
  curl -s -X POST https://api.telegram.org/bot$TELEGRAM_BOT/sendMessage \
       -d chat_id=$CHAT_ID \
       -d text="⚠️ CPU přetížení detekováno! Vibrace + alarm aktivovány."
fi

# SVG re-generace (mock)
echo "<svg xmlns='http://www.w3.org/2000/svg' width='600' height='400'>
  <circle cx='300' cy='200' r='$(($CPU_USAGE + 20))' fill='blue'>
    <animateTransform attributeName='transform' type='rotate' from='0 300 200' to='360 300 200' dur='30s' repeatCount='indefinite'/>
  </circle>
</svg>" > $SVG_PATH

# Výdech vizualizace & QR
qrencode -o qrcode.png "$(date) $CPU_USAGE%"
curl -s -X POST https://api.telegram.org/bot$TELEGRAM_BOT/sendPhoto \
     -F chat_id=$CHAT_ID \
     -F photo=@qrcode.png
