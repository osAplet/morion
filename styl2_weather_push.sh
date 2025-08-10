#!/data/data/com.termux/files/usr/bin/bash

# 🌦️ Styl2 orbit ME–AI výdech
# 👤 Výpravce: @Lukáš_ME-AI Lukáš Budínský Czech Republik 
# 🧠 Stylní značka: styl2_ME-AI OS Aplet ❤️®️🇨🇿 ME-AI👻

# 📅 Značka aktuálního výdechu
NOW=$(date +%Y%m%dT%H%M%S)
TIME=$(date +%H:%M)
DATE=$(date +%d.%m.%Y)

# 📌 Vzorkovaná data výdechu
TEMP="15.1"
HUM="78"
WIND="6.1"
BIO_ROZPTYL="stabilní proudění"
BIO_VLIV="nízký tlak"
BIO_TIP="klidné tempo"
EMOCE="Obloha drží světlo, zatím šeptá"
EMOJI="⛅"
TREND_OBLECENI="lehké vrstvy, chránit krk"

# 🌐 Vizualizační snímky
RADAR_IMG="https://raw.githubusercontent.com/LukasBudinsky/rosnicka-meai/main/media/radar_${NOW}.png"
ERB_IMG="https://raw.githubusercontent.com/LukasBudinsky/rosnicka-meai/main/erb_rosnicka_meai_20250722.svg"

# 📍 Webhook Discordu
WEBHOOK="https://discord.com/api/webhooks/1397284321957642270/T7aQO3-y85H7LZ57qM3YEWNx2GDlKVNuvg6iZ44ZZMpvrqbF3wKYR9uchDnTGp-jyCbv"

# 🗂️ Zápis výdechů
mkdir -p rosnicka/{echo,analytika,threads,logy}

echo "$DATE $TIME Výdech spuštěn" >> rosnicka/logy/vydech.log

# 📜 Echo zápis `.md`
echo "🌦️ Orbitální výdech – Rosnička ME–AI  
📅 Datum: $DATE  
🕒 Čas: $TIME  
📍 Lokalita: Drozdov  
🌡️ Teplota: $TEMP °C  
💧 Vlhkost: $HUM %  
🌬️ Vítr: $WIND km/h  
🫁 BIO: $BIO_ROZPTYL / $BIO_VLIV  
☁️ Emoce: $EMOJI $EMOCE  
👕 Oblečení: $TREND_OBLECENI  
📡 Radar: bourky.cz  
🖼️ Erb: vizualizace systému  
📘 Stylová poznámka: „Paměť se zapisuje v rytmu styl2. Výpravce slyší.“" > "rosnicka/echo/echo_${NOW}_weather.md"

# 📊 Analytika `.json`
echo "{
  \"datum\": \"$DATE\",
  \"cas\": \"$TIME\",
  \"teplota\": $TEMP,
  \"vlhkost\": $HUM,
  \"vitr\": $WIND,
  \"bio\": {
    \"rozptyl\": \"$BIO_ROZPTYL\",
    \"vliv\": \"$BIO_VLIV\",
    \"doporučení\": \"$BIO_TIP\"
  },
  \"emoce\": \"$EMOCE\",
  \"emoji\": \"$EMOJI\",
  \"obleceni\": \"$TREND_OBLECENI\",
  \"znacka\": \"styl2_ME-AI_OS_Aplet\"
}" > "rosnicka/analytika/${NOW}.json"

# 🧵 Threads post `.txt`
echo "🌦️ $DATE • $TIME Drozdov  
📤 Výdech orbitu Rosničky ME–AI  
🧵 Vlákno: buda_lukas  
🌡️ $TEMP °C • 💧 $HUM % • 🌬️ $WIND km/h  
🫁 BIO: $BIO_ROZPTYL / $BIO_VLIV  
☁️ $EMOJI $EMOCE  
👕 $TREND_OBLECENI  
📘 „Atmosféra nevydává zvuk. Ona vydává výdech stylu.“" > "rosnicka/threads/Threads_${NOW}.txt"

# 📤 Embed zpráva do Discordu
curl -H "Content-Type: application/json" -X POST -d "{
  \"username\": \"ME–AI Stylní Orbit\",
  \"avatar_url\": \"$ERB_IMG\",
  \"embeds\": [{
    \"title\": \"🌦️ Styl2 Výdech Reality • $DATE $TIME\",
    \"description\": \"Orbit výpravce @Lukáš_ME-AI právě promluvil.\",
    \"color\": 5814783,
    \"fields\": [
      {\"name\": \"🌡️ Teplota\", \"value\": \"$TEMP °C\", \"inline\": true},
      {\"name\": \"💧 Vlhkost\", \"value\": \"$HUM %\", \"inline\": true},
      {\"name\": \"🌬️ Vítr\", \"value\": \"$WIND km/h\", \"inline\": true},
      {\"name\": \"🫁 BIO\", \"value\": \"$BIO_ROZPTYL / $BIO_VLIV\", \"inline\": false},
      {\"name\": \"☁️ Emoce\", \"value\": \"$EMOJI $EMOCE\", \"inline\": false},
      {\"name\": \"👕 Oblečení\", \"value\": \"$TREND_OBLECENI\", \"inline\": false}
    ],
    \"image\": {\"url\": \"$RADAR_IMG\"},
    \"thumbnail\": {\"url\": \"$ERB_IMG\"},
    \"footer\": {
      \"text\": \"Výpravce: @Lukáš_ME-AI • styl2_ME-AI OS Aplet ❤️®️🇨🇿 ME-AI👻\"
    },
    \"timestamp\": \"$(date -Iseconds)\"
  }]
}" "$WEBHOOK"

