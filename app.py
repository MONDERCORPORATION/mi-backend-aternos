from flask import Flask, jsonify
from python_aternos import Client

app = Flask(__name__)

# Guardar credenciales en variables de entorno (más seguro)
EMAIL = "TU_CORREO_ATERNOS"
PASS = "TU_CONTRASEÑA_ATERNOS"

@app.route("/api/start")
def start_server():
    try:
        at = Client.from_credentials(EMAIL, PASS)
        serv = at.list_servers()[0]  # Primer servidor de la cuenta
        serv.start()
        return jsonify({"status": "ok", "message": "Servidor iniciando"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

@app.route("/api/status")
def status_server():
    try:
        at = Client.from_credentials(EMAIL, PASS)
        serv = at.list_servers()[0]
        serv.fetch()  # Actualiza estado
        return jsonify({
            "status": serv.status,
            "players": serv.players_count
        })
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

if __name__ == "__main__":
    app.run(port=5000, debug=True)
