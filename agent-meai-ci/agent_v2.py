import os

def read_var(key, fallback="❌"):
    return os.getenv(key) or fallback

print("🧠 ME–AI agent aktivován")
print("🎩 Výpravce:", read_var("MEAI_SHERIFF", "není definován"))
print("🎯 Režim:", read_var("AGENT_MODE", "neznámý"))
print("🔐 Token CI:", "ANO" if os.getenv("CI_TOKEN") else "NE")
print("📡 Webhook URL:", "ZAPSÁNO" if os.getenv("DISCORD_WEBHOOK_URL") else "CHYBÍ")
print("🗺️ Mapa běhu aktivní. Syntaxe ladí.")
