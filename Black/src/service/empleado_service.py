from ..database.db_conección import get_connection

def agregar_empleado_service(RUT, Nombre, Apellidos, CodRol, TotalHoras, SueldoTotal):
    try:
        connection = get_connection()
        cursor = connection.cursor()

        # Llamar al procedimiento almacenado para agregar un empleado
        cursor.callproc('agregar_empleado', (RUT, Nombre, Apellidos, CodRol, TotalHoras, SueldoTotal))
        
        # Commit para aplicar los cambios en la base de datos
        connection.commit()
        
        # Cerrar conexión y cursor
        cursor.close()
        connection.close()
        
    except Exception as e:
        # Manejar errores
        print("Error al agregar empleado:", e)