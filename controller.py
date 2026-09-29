from flask import Flask,jsonify
from servicio import PacienteService

app = Flask(__name__)

servicio_paciente = PacienteService()

@app.route('/pacientes/activos', methods=['GET'])
def obtener_pacientes_activos():
    try:

        pacientes_procesados = servicio_paciente.obtener_pacientes_activos()
        return jsonify({
            "codigo_estado": 200,
            "mensaje": "Pacientes activos obtenidos correctamente",
            "data": pacientes_procesados
        }),200

    except Exception as e:
        return jsonify({
            "codigo_estado": 500,
            "mensaje": "Error al obtener pacientes activos",
            "error": str(e)
        }), 500

if __name__ == '__main__':
    app.run(debug=True)