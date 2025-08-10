from flask import Flask, request, jsonify, send_from_directory
import json, os
from datetime import datetime, timedelta

app = Flask(__name__)
DATA_FILE = "/sdcard/rosnicka/data.json"
HTML_DIR = "/sdcard/rosnicka"

@app.route('/')
def index():
    return send_from_directory(HTML_DIR, "rosnicka_dashboard.html")

@app.route('/api/vydech', methods=['POST'])
def pridej_vydech():
    data = request.json
    data['timestamp'] = datetime.utcnow().isoformat()

    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            zaznamy = json.load(f)
    else:
        zaznamy = []

    zaznamy.append(data)

    cutoff = datetime.utcnow() - timedelta(hours=24)
    zaznamy = [z for z in zaznamy if datetime.fromisoformat(z['timestamp']) > cutoff]

    with open(DATA_FILE, 'w') as f:
        json.dump(zaznamy, f, indent=2)

    return jsonify({"status": "✅ Výdech uložen"}), 200

@app.route('/api/data')
def vrat_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            zaznamy = json.load(f)
        return jsonify(zaznamy)
    else:
        return jsonify([])

app.run(host='0.0.0.0', port=5000)
