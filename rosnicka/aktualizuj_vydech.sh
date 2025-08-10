#!/bin/bash

# 🌍 Souřadnice Nymburk
LAT=50.186
LON=15.042

# 📡 API URL
URL="https://api.open-meteo.com/v1/forecast?latitude=$LAT&longitude=$LON&current=temperature_2m,relative_humidity_2m,wind_speed_10m,pressure_msl"

# 📥 Načti data
DATA=$(curl -s "$URL")

# 🧠 Zpracuj JSON
TEPLOTA=$(echo "$DATA" | jq '.current.temperature_2m')
VLHKOST=$(echo "$DATA" | jq '.current.relative_humidity_2m')
VITR=$(echo "$DATA" | jq '.current.wind_speed_10m')
TLAK=$(echo "$DATA" | jq '.current.pressure_msl')

# 📝 Zapiš do vydech.json
cat > ~/MEAI/rosnicka/vydech.json <<EOF
{
  "teplota": $TEPLOTA,
  "vlhkost": $VLHKOST,
  "vitr": $VITR,
  "tlak": $TLAK
}
EOF
