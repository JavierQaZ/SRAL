from flask import Blueprint, request, jsonify
from ..service.empleado_service import agregar_empleado_service
from ..service.empleado_service import editar_empleado_service
from ..service.empleado_service import delete_empleado_service

bp = Blueprint('empleados_Blueprint', __name__)

@bp.route('/add', methods=['POST'])
def add_empleado():
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


@bp.route('/edit', methods=['PUT'])
def edit_empleado():
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
        
        # Llamada al servicio para editar empleado
        editar_empleado_service(RUT, Nombre, Apellidos, CodRol, TotalHoras, SueldoTotal)
        
        return jsonify({"message": "Empleado editado exitosamente"}), 200
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    

@bp.route('/delete', methods=['DELETE'])
def delete_empleado():
    try:
        data = request.get_json()
        
        # Validación de datos
        if 'RUT' not in data:
            return jsonify({"error": "Falta el campo RUT"}), 400
        
        RUT = data['RUT']
        
        # Llamada al servicio para eliminar empleado
        delete_empleado_service(RUT)
        
        return jsonify({"message": "Empleado eliminado exitosamente"}), 200
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500