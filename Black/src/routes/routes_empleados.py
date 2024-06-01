from flask import Blueprint, request, jsonify
from ..service.empleado_service import agregar_empleado_service

bp = Blueprint('rol_Blueprint', __name__)

@bp.route('/add', methods=['POST'])
def add_rol():
    try:
        data = request.get_json()
        
        # Validación de datos
        required_fields = ['RUT', 'Nombre', 'Apellidos', 'CodRol', 'TotalHoras', 'SueldoTotal']
        for field in required_fields:
            if field not in data:
                return jsonify({"error": f"Falta el campo {field}"}), 400

        RUT = data['RUT']
        Nombre = data['Nombre']
        Apellidos = data['Apellidos']
        CodRol = data['CodRol']
        TotalHoras = data['TotalHoras']
        SueldoTotal = data['SueldoTotal']
        
        # Llamada al servicio para agregar empleado
        agregar_empleado_service(RUT, Nombre, Apellidos, CodRol, TotalHoras, SueldoTotal)
        
        return jsonify({"message": "Empleado agregado exitosamente"}), 201
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500
