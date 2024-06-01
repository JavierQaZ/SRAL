from flask import Blueprint, request, jsonify
from ..service.empleado_service import agregar_empleado_service

bp = Blueprint('empleado_routes', __name__)

@bp.route('/add_empleado', methods=['POST'])
def add_empleado():
    data = request.json
    RUT = data['RUT']
    Nombre = data['Nombre']
    Apellidos = data['Apellidos']
    CodRol = data['CodRol']
    TotalHoras = data['TotalHoras']
    SueldoTotal = data['SueldoTotal']
    
    agregar_empleado_service(RUT, Nombre, Apellidos, CodRol, TotalHoras, SueldoTotal)
    return jsonify({"message": "Empleado agregado exitosamente"})