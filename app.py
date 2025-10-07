from flask import Flask, request, jsonify
import os
import aternos

app = Flask(__name__)

API_KEY = os.environ.get("API_KEY")
EMAIL = os.environ.get(monderpro11@gmail.com)
PASSWORD = os.environ.get(MondeR13)

@app.route("/")
def home():
    return "Servidor Backend Aternos activo!"

@app.route("/api/start")
def start_server():
    key = request.args.get("key")
    if key != API_KEY:
        return jsonify({"error": "Acceso denegado"}), 403

    atclient = aternos.Client.from_credentials(EMAIL, PASSWORD)
    srv = atclient.list_servers()[0]  # Usa tu primer server
    srv.start()

    return jsonify({"status": "Servidor iniciando..."})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
