from flask import Flask, jsonify
from modules.index.index import index
from modules.evaluaciones_desempeño.e_desempeño import e_desempeño
from modules.rotacion_personal.r_personal import r_personal
from modules.encuestas.encuestas import encuestas
from modules.control_inventarios.inventarios import inventarios

app = Flask(__name__)
app.secret_key="My_secret_Key"

# Blueprints

app.register_blueprint(index)
app.register_blueprint(e_desempeño)
app.register_blueprint(r_personal)
app.register_blueprint(encuestas)
app.register_blueprint(inventarios)

# EndBlueprints

@app.route("/api/<data>")
def api(data):
    return jsonify({"message": "Successfully received client request for "+data+"."})

if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=80)
