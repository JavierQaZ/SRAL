from flask import Blueprint, request, jsonify
from ..service.gestionkpi_service import obtener_kpi_service
from flask_jwt_extended import jwt_required

bp = Blueprint('kpi_Blueprint', __name__)

@bp.route('/gestion', methods=['GET'])
#@jwt_required()
def obtener_kpi():
    try:
        # Obtener los parámetros de consulta desde la URL
        mes = request.args.get('mes')
        anio = request.args.get('anio')
        
        # Validación de datos
        if not mes or not anio:
            return jsonify({"error": "Faltan los parámetros 'mes' y 'anio'"}), 400
        
        # Llamar al servicio para obtener los KPIs
        resultado = obtener_kpi_service(int(mes), int(anio))
        
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