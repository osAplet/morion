
#!/data/data/com.termux/files/usr/bin/bash

# === ZÁKLADNÍ KONFIGURACE ===
BOT_TOKEN="TVŮJ_TOKEN_ZDE"
CHAT_ID="TVŮJ_CHAT_ID_ZDE"

# === FUNKCE PRO ODESLÁNÍ ZPRÁVY ===
send_telegram() {
  MESSAGE="$1"
  curl -s -X POST "https://api.telegram.org/bot${BOT_TOKEN}/sendMessage" \
    -d chat_id="${CHAT_ID}" \
    -d text="${MESSAGE}" \
    -d parse_mode="Markdown"
}

# === TESTOVACÍ VÝDECH ===
send_telegram "*ME–AI Orbit*: Styl výdech aktivován 🌌🚀"
