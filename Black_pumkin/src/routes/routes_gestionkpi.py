from flask import Blueprint, request, jsonify
from ..service.gestionkpi_service import obtener_kpi_service
from flask_jwt_extended import jwt_required

bp = Blueprint('kpi_Blueprint', __name__)

@bp.route('/gestion', methods=['POST'])
@jwt_required()
def obtener_kpi():
    try:
        data = request.get_json()
        
        # Validación de datos
        required_fields = ['mes', 'anio']
        for field in required_fields:
            if field not in data:
                return jsonify({"error": f"Falta el campo {field}"}), 400

        mes = data['mes']
        anio = data['anio']
        
        # Llamada al servicio para obtener los KPIs
        resultado = obtener_kpi_service(mes, anio)
        
        # Asegurarse de que el JSON devuelto esté en el formato correcto
        response = {
            "mes": resultado["mes"],
            "anio": resultado["anio"],
            "costo_total_por_mes": resultado["costo_total_por_mes"],
            "costo_por_hora_trabajada": resultado["costo_por_hora_trabajada"],
            "promedio_horas_trabajadas": resultado["promedio_horas_trabajadas"],
            "costo_total_por_rol": resultado["costo_total_por_rol"]
        }
        
        return jsonify(response), 200
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500