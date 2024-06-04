from flask import Blueprint, request, jsonify
from ..service.r_salida_service import add_r_salida_service
from ..service.r_salida_service import edit_r_salida_service
from ..service.r_salida_service import delete_r_salida_service

bp = Blueprint('r_salida_Blueprint', __name__)

@bp.route('/add', methods=['POST'])
def add_r_salida():
    try:
        data = request.get_json()
        
        # Validación de datos
        required_fields = {
            'HoraSalida': str,  # Asumimos que la fecha y hora se envían como cadena en formato ISO 8601
            'RUT': str
        }
        
        for field, field_type in required_fields.items():
            if field not in data:
                return jsonify({"error": f"Falta el campo {field}"}), 400
            if not isinstance(data[field], field_type):
                return jsonify({"error": f"El campo {field} debe ser de tipo {field_type.__name__}"}), 400

        HoraSalida = data['HoraSalida']
        RUT = data['RUT']
        
        # Convertir HoraSalida a datetime si es necesario
        from datetime import datetime
        try:
            HoraSalida = datetime.fromisoformat(HoraSalida)
        except ValueError:
            return jsonify({"error": "HoraSalida debe estar en formato ISO 8601"}), 400
        
        # Llamada al servicio para agregar rol
        add_r_salida_service(HoraSalida, RUT)
        
        return jsonify({"message": "Hora de ingreso agregada exitosamente"}), 201
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    

@bp.route('/edit', methods=['PUT'])
def edit_r_salida():
    try:
        data = request.get_json()
        
        # Validación de datos
        required_fields = {
            'HoraSalida': str,  # Asumimos que la fecha y hora se envían como cadena en formato ISO 8601
            'RUT': str
        }
        
        for field, field_type in required_fields.items():
            if field not in data:
                return jsonify({"error": f"Falta el campo {field}"}), 400
            if not isinstance(data[field], field_type):
                return jsonify({"error": f"El campo {field} debe ser de tipo {field_type.__name__}"}), 400

        HoraSalida = data['HoraSalida']
        RUT = data['RUT']
        
        # Convertir HoraSalida a datetime si es necesario
        from datetime import datetime
        try:
            HoraSalida = datetime.fromisoformat(HoraSalida)
        except ValueError:
            return jsonify({"error": "HoraSalida debe estar en formato ISO 8601"}), 400
        
        # Llamada al servicio para editar la hora de salida
        edit_r_salida_service(HoraSalida, RUT)
        
        return jsonify({"message": "Hora de salida editada exitosamente"}), 200
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@bp.route('/delete', methods=['DELETE'])
def delete_r_salida():
    try:
        data = request.get_json()
        
        # Validación de datos
        required_fields = {
            'HoraSalida': str,  # Asumimos que la fecha y hora se envían como cadena en formato ISO 8601
            'RUT': str
        }
        
        for field, field_type in required_fields.items():
            if field not in data:
                return jsonify({"error": f"Falta el campo {field}"}), 400
            if not isinstance(data[field], field_type):
                return jsonify({"error": f"El campo {field} debe ser de tipo {field_type.__name__}"}), 400

        HoraSalida = data['HoraSalida']
        RUT = data['RUT']
        
        # Convertir HoraSalida a datetime si es necesario
        from datetime import datetime
        try:
            HoraSalida = datetime.fromisoformat(HoraSalida)
        except ValueError:
            return jsonify({"error": "HoraSalida debe estar en formato ISO 8601"}), 400
        
        # Llamada al servicio para eliminar registro de salida
        delete_r_salida_service(HoraSalida, RUT)
        
        return jsonify({"message": "Registro de salida eliminado exitosamente"}), 200
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500