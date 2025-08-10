#!/data/data/com.termux/files/usr/bin/bash
DATE=$(date +%Y%m%dT%H%M%S)
OUT="rosnicka/media/radar_$DATE.png"
curl -s -o "$OUT" "https://radar.bourky.cz/data/image.png"
echo "✅ Radarový výdech uložen do: $OUT"
