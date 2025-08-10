#!/data/data/com.termux/files/usr/bin/bash

# 📍 Cesta k datovému souboru
DATA_FILE="/sdcard/rosnicka/data.json"

# 🌞 Nastavení jasu displeje na maximum
termux-brightness 255

# 🕒 Aktuální čas
NOW=$(date -u +"%Y-%m-%dT%H:%M:%S")

# 📥 Nový výdech (můžeš upravit hodnoty podle reálných dat)
NEW_ENTRY=$(cat <<EOF
{ "timestamp": "$NOW", "temperature": 28.3, "humidity": 58, "pressure": 1013, "wind": 3.5 }
EOF
)

# 📂 Načti existující data
if [ -f "$DATA_FILE" ]; then
  EXISTING=$(cat "$DATA_FILE")
else
  EXISTING="[]"
fi

# 🧠 Python filtr: přidá nový výdech a smaže staré
python3 - <<END
import json, datetime

data = json.loads('''$EXISTING''')
now = datetime.datetime.utcnow()
cutoff = now - datetime.timedelta(hours=24)

# Přidání nového výdechu
data.append($NEW_ENTRY)

# Filtrování starých záznamů
data = [entry for entry in data if datetime.datetime.strptime(entry["timestamp"], "%Y-%m-%dT%H:%M:%S") > cutoff]

# Uložení zpět
with open("$DATA_FILE", "w") as f:
    json.dump(data, f, indent=2)
END

# ✅ Hotovo
echo "✅ Výdech přidán, staré záznamy odstraněny."
