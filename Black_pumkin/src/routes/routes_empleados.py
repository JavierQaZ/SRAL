from flask import Blueprint, request, jsonify
from ..service.empleado_service import agregar_empleado_service,editar_empleado_service,delete_empleado_service, obtener_empleados_service

bp = Blueprint('empleados_Blueprint', __name__)

@bp.route('/add', methods=['POST'])
def add_empleado():
    try:
        data = request.get_json()
        
        # Validación de datos
        required_fields = ['rut_empleado', 'nombre_empleado', 'apellidos_empleado','codigo_rol']#, 'TotalHoras', 'SueldoTotal']
        for field in required_fields:
            if field not in data:
                return jsonify({"error": f"Falta el campo {field}"}), 400

        rut_empleado = data['rut_empleado']
        nombre_empleado = data['nombre_empleado']
        apellidos_empleado = data['apellidos_empleado']
        codigo_rol = data['codigo_rol']
        #TotalHoras = data['TotalHoras']
        #SueldoTotal = data['SueldoTotal']
        
        # Llamada al servicio para agregar empleado
        agregar_empleado_service(rut_empleado, nombre_empleado, apellidos_empleado, codigo_rol)# TotalHoras, SueldoTotal)
        
        return jsonify({"message": "Empleado agregado exitosamente"}), 201
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@bp.route('/edit', methods=['PUT'])
def edit_empleado():
    try:
        data = request.get_json()
        
        # Validación de datos
        required_fields = ['rut_empleado', 'nombre_empleado', 'apellidos_empleado', 'codigo_rol', 'TotalHoras', 'SueldoTotal']
        for field in required_fields:
            if field not in data:
                return jsonify({"error": f"Falta el campo {field}"}), 400

        rut_empleado = data['rut_empleado']
        nombre_empleado = data['nombre_empleado']
        apellidos_empleado = data['apellidos_empleado']
        codigo_rol = data['codigo_rol']
        TotalHoras = data['TotalHoras']
        SueldoTotal = data['SueldoTotal']
        
        # Llamada al servicio para editar empleado
        editar_empleado_service(rut_empleado, nombre_empleado, apellidos_empleado, codigo_rol, TotalHoras, SueldoTotal)
        
        return jsonify({"message": "Empleado editado exitosamente"}), 200
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    

@bp.route('/delete', methods=['DELETE'])
def delete_empleado():
    try:
        data = request.get_json()
        
        # Validación de datos
        if 'rut_empleado' not in data:
            return jsonify({"error": "Falta el campo rut_empleado"}), 400
        
        rut_empleado = data['rut_empleado']
        
        # Llamada al servicio para eliminar empleado
        delete_empleado_service(rut_empleado)
        
        return jsonify({"message": "Empleado eliminado exitosamente"}), 200
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@bp.route('/get', methods=['GET'])
def obtener_empleados():
    try:
        empleados = obtener_empleados_service()
        
        if empleados is None:
            return jsonify({"error": "No se pudieron obtener los empleados"}), 500
        
        # Formatear los empleados en una lista de diccionarios
        empleados_list = []
        for emp in empleados:
            empleados_list.append({
                'rut_empleado': emp[0],
                'nombre_empleado': emp[1],
                'apellidos_empleado': emp[2],
                'codigo_rol': emp[3],
                'totalHorasTrabajadas_empleado': emp[4],
                'sueldoTotal_empleado': emp[5]
            })
        
        return jsonify(empleados_list), 200
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500