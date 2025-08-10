from flask import Flask, jsonify
import psutil
import time

app = Flask(__name__)
start_time = time.time()

@app.route("/system")
def system_status():
    uptime = time.time() - start_time
    return jsonify({
        "cpu_percent": psutil.cpu_percent(interval=1),
        "memory": {
            "used": psutil.virtual_memory().used,
            "total": psutil.virtual_memory().total,
            "percent": psutil.virtual_memory().percent
        },
        "uptime_seconds": int(uptime),
        "active_connections": len(psutil.net_connections())
    })

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
