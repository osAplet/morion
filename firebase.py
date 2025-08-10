import requests
import json

# 🔧 Změň na svůj Firebase projekt ID
project_id = "62542292475"

# 🔑 Vlož svůj API klíč
api_key = "AIzaSyBk_eUDNCSrd4yEU37n6Zzl9VWnt1KMvDg"

# URL Firestore REST API
url = f"https://firestore.googleapis.com/v1/projects/{project_id}/databases/(default)/documents/rosnicka?key={api_key}"

# Data k odeslání
data = {
    "fields": {
        "teplota": {"doubleValue": 23.5},
        "vlhkost": {"doubleValue": 60.2}
    }
}

headers = {
    "Content-Type": "application/json"
}

response = requests.post(url, headers=headers, data=json.dumps(data))

print(response.status_code)
print(response.text)
