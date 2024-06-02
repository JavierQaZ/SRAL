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
        
        
def editar_empleado_service(RUT, Nombre, Apellidos, CodRol, TotalHoras, SueldoTotal):
    try:
        connection = get_connection()
        cursor = connection.cursor()

        # Llamar al procedimiento almacenado para editar un empleado
        cursor.callproc('editar_empleado', (RUT, Nombre, Apellidos, CodRol, TotalHoras, SueldoTotal))
        
        # Commit para aplicar los cambios en la base de datos
        connection.commit()
        
        # Cerrar conexión y cursor
        cursor.close()
        connection.close()
        
    except Exception as e:
        # Manejar errores
        print("Error al editar empleado:", e)
        raise e
    
def delete_empleado_service(RUT):
    try:
        connection = get_connection()
        cursor = connection.cursor()

        # Llamar al procedimiento almacenado para eliminar un empleado
        cursor.callproc('eliminar_empleado', (RUT,))
        
        # Commit para aplicar los cambios en la base de datos
        connection.commit()
        
        # Cerrar conexión y cursor
        cursor.close()
        connection.close()
        
    except Exception as e:
        # Manejar errores
        print("Error al eliminar empleado:", e)
        raise e
        
#{
#    "RUT": "1111111-8",
#    "Nombre": "perla",
#    "Apellidos": "Pérez",
#    "CodRol": "1",
#    "TotalHoras": 40,
#    "SueldoTotal": 1000
#}



