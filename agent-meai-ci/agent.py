print("🧠 ME–AI agent aktivován")
import os

print("🎩 ME–AI agent aktivován")
print("👤 Výpravce:", os.getenv("MEAI_SHERIFF"))
print("🎯 Režim:", os.getenv("AGENT_MODE") or "neznámý")
print("🔐 Token:", "ANO" if os.getenv("CI_TOKEN") else "NE")
