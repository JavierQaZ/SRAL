# File: service/kpi_service.py

from ..database.db_conección import get_connection

def obtener_kpi_service(rut_empleado, mes, anio):
    try:
        connection = get_connection()
        cursor = connection.cursor()

        # Llamar al procedimiento almacenado para obtener el sueldo total
        cursor.callproc('calcular_sueldo_total', (rut_empleado, mes, anio, None))
        
        # Obtener el resultado del procedimiento almacenado
        cursor.execute('SELECT @_calcular_sueldo_total_3')
        sueldo_total = cursor.fetchone()[0]

        # Llamar al procedimiento almacenado para calcular las horas trabajadas
        cursor.callproc('calcular_horas_trabajadas', (rut_empleado, mes, anio, None))
        
        # Obtener el resultado del procedimiento almacenado
        cursor.execute('SELECT @_calcular_horas_trabajadas_3')
        horas_trabajadas = cursor.fetchone()[0]

        # Llamar al procedimiento almacenado para calcular la puntualidad promedio
        cursor.callproc('calcular_puntualidad_promedio', (rut_empleado, mes, anio, None))
        
        # Obtener el resultado del procedimiento almacenado
        cursor.execute('SELECT @_calcular_puntualidad_promedio_3')
        puntualidad_promedio = cursor.fetchone()[0]

        # Llamar al procedimiento almacenado para calcular la tasa de asistencia
        cursor.callproc('calcular_tasa_asistencia', (rut_empleado, mes, anio, None))
        
        # Obtener el resultado del procedimiento almacenado
        cursor.execute('SELECT @_calcular_tasa_asistencia_3')
        tasa_asistencia = cursor.fetchone()[0]

        # Llamar al procedimiento almacenado para calcular el índice de retraso
        cursor.callproc('calcular_indice_retraso', (rut_empleado, mes, anio, None))
        
        # Obtener el resultado del procedimiento almacenado
        cursor.execute('SELECT @_calcular_indice_retraso_3')
        indice_retraso = cursor.fetchone()[0]

        # Cerrar conexión y cursor
        cursor.close()
        connection.close()

        return {
            "rut_empleado": rut_empleado,
            "mes": mes,
            "anio": anio,
            "sueldo_total": sueldo_total,
            "horas_trabajadas": horas_trabajadas,
            "puntualidad_promedio": puntualidad_promedio,
            "tasa_asistencia": tasa_asistencia,
            "indice_retraso": indice_retraso
        }

    except Exception as e:
        # Manejar errores
        print("Error al obtener KPI:", e)
        raise
