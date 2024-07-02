

from ..database.db_conección import get_connection

def obtener_kpi_service(mes, anio):
    try:
        connection = get_connection()  # Obtener conexión a la base de datos
        cursor = connection.cursor()

        # Llamar al procedimiento almacenado para calcular el costo total por mes
        cursor.callproc('calcular_costo_total_por_mes', (mes, anio,))
        costo_total_por_mes = cursor.fetchall()

        # Llamar al procedimiento almacenado para calcular el costo por hora trabajada
        cursor.callproc('calcular_costo_por_hora_trabajada', (mes, anio,))
        costo_por_hora_trabajada = cursor.fetchone()[0]

        # Llamar al procedimiento almacenado para calcular el promedio de horas trabajadas
        cursor.callproc('calcular_promedio_horas_trabajadas', (mes, anio,))
        promedio_horas_trabajadas = cursor.fetchone()[0]

        # Llamar al procedimiento almacenado para calcular el costo total por rol
        cursor.callproc('calcular_costo_total_por_rol', (mes, anio,))
        costo_total_por_rol = cursor.fetchall()

        # Cerrar conexión y cursor
        cursor.close()
        connection.close()

        # Retornar los resultados finales
        return {
            "mes": mes,
            "anio": anio,
            "costo_total_por_mes": str(costo_total_por_mes[0][0]) if costo_total_por_mes else None,
            "costo_por_hora_trabajada": f"{costo_por_hora_trabajada:.2f}" if costo_por_hora_trabajada is not None else None,
            "promedio_horas_trabajadas": f"{promedio_horas_trabajadas:.2f}" if promedio_horas_trabajadas is not None else None,
            "costo_total_por_rol": [
                [row[0], row[1], f"{row[2]:.2f}"] for row in costo_total_por_rol
            ] if costo_total_por_rol else None
        }

    except Exception as e:
        print("Error al obtener KPI:", e)
        raise
