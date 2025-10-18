from flask import Flask, request, jsonify
import os
import python_aternos

app = Flask(__name__)

# ⚙️ Variables de entorno (deben estar configuradas en Render)
API_KEY = os.environ.get("API_KEY")
EMAIL = os.environ.get("EMAIL")
PASSWORD = os.environ.get("PASSWORD")

@app.route("/")
def home():
    return "Servidor Backend Aternos activo ✅"

@app.route("/api/start")
def start_server():
    key = request.args.get("key")

    if key != API_KEY:
        return jsonify({"error": "Acceso denegado"}), 403

    try:
        # 🔑 Conectarse a la cuenta de Aternos
        atclient = aternos.Client.from_credentials(EMAIL, PASSWORD)
        servers = atclient.list_servers()

        # 🔍 Buscar el servidor exacto por dirección
        srv = None
        for s in servers:
            if s.address == "dweller2.aternos.me":
                srv = s
                break

        if not srv:
            return jsonify({"error": "Servidor no encontrado"}), 404

        # 🚀 Intentar encender el servidor
        if srv.status == "offline":
            srv.start()
            return jsonify({"status": "Servidor iniciando..."})
        else:
            return jsonify({"status": f"Servidor ya está {srv.status}"})

    except Exception as e:
        return jsonify({"error": f"Error interno: {str(e)}"}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)