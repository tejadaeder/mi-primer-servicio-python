class PacienteService:
    def obtener_pacientes_activos(self):
        # Lógica para obtener pacientes activos
        pacientes_db = [
            {"id": 1, "nombre": "Juan Perez", "activo": True},
            {"id": 2, "nombre": "Maria Lopez", "activo": False},
            {"id": 3, "nombre": "Carlos Garcia", "activo": True},
        ]

        resultado = {
            "total_registros": len(pacientes_db),
            "clinica": "Clinica San Juan",
            "pacientes": pacientes_db
        }

        return resultado