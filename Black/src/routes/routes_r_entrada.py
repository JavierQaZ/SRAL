from flask import Blueprint, request, jsonify
from ..service.r_entrada_service import add_r_entrada_service

bp = Blueprint('r_entrada_Blueprint', __name__)

@bp.route('/add', methods=['POST'])
def add_r_entrada():
    try:
        data = request.get_json()
        
        # Validación de datos
        required_fields = {
            'HoraIngreso': str,  # Asumimos que la fecha y hora se envían como cadena en formato ISO 8601
            'RUT': str
        }
        
        for field, field_type in required_fields.items():
            if field not in data:
                return jsonify({"error": f"Falta el campo {field}"}), 400
            if not isinstance(data[field], field_type):
                return jsonify({"error": f"El campo {field} debe ser de tipo {field_type.__name__}"}), 400

        HoraIngreso = data['HoraIngreso']
        RUT = data['RUT']
        
        # Convertir HoraIngreso a datetime si es necesario
        from datetime import datetime
        try:
            HoraIngreso = datetime.fromisoformat(HoraIngreso)
        except ValueError:
            return jsonify({"error": "HoraIngreso debe estar en formato ISO 8601"}), 400
        
        # Llamada al servicio para agregar rol
        add_r_entrada_service(HoraIngreso, RUT)
        
        return jsonify({"message": "Hora de ingreso agregada exitosamente"}), 201
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500