from flask import Blueprint, request, jsonify
from ..service.rol_service import add_rol_service, editar_rol_service, delete_rol_service

bp = Blueprint('rol_Blueprint', __name__)

@bp.route('/add', methods=['POST'])
def add_rol():
    try:
        data = request.get_json()
        
        # Validación de datos
        required_fields = {
            'Nombre': str,
            'SueldoPorHora': float
        }
        
        for field, field_type in required_fields.items():
            if field not in data:
                return jsonify({"error": f"Falta el campo {field}"}), 400
            if not isinstance(data[field], field_type):
                return jsonify({"error": f"El campo {field} debe ser de tipo {field_type.__name__}"}), 400

        Nombre = data['Nombre']
        SueldoPorHora = data['SueldoPorHora']
        
        # Llamada al servicio para agregar rol
        add_rol_service(Nombre, SueldoPorHora)
        
        return jsonify({"message": "rol agregado exitosamente"}), 201
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    

@bp.route('/edit', methods=['PUT'])
def edit_rol():
    try:
        data = request.get_json()
        
        # Validación de datos
        required_fields = ['Codigo', 'Nombre', 'SueldoPorHora']
        for field in required_fields:
            if field not in data:
                return jsonify({"error": f"Falta el campo {field}"}), 400

        Codigo = data['Codigo']
        Nombre = data['Nombre']
        SueldoPorHora = data['SueldoPorHora']
        
        # Llamada al servicio para editar rol
        editar_rol_service(Codigo, Nombre, SueldoPorHora)
        
        return jsonify({"message": "Rol editado exitosamente"}), 200
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@bp.route('/delete', methods=['DELETE'])
def delete_rol():
    try:
        data = request.get_json()
        
        # Validación de datos
        if 'Codigo' not in data:
            return jsonify({"error": "Falta el campo Codigo"}), 400

        Codigo = data['Codigo']
        
        # Llamada al servicio para eliminar el rol
        delete_rol_service(Codigo)
        
        return jsonify({"message": "Rol eliminado exitosamente"}), 200
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

