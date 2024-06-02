from ..database.db_conección import get_connection

def add_rol_service(Nombre,SueldoPorHora):
    try:
        connection = get_connection()
        cursor = connection.cursor()

        # Llamar al procedimiento almacenado para agregar un empleado
        cursor.callproc('agregar_rol', (Nombre, SueldoPorHora))
        
        # Commit para aplicar los cambios en la base de datos
        connection.commit()
        
        # Cerrar conexión y cursor
        cursor.close()
        connection.close()
        
    except Exception as e:
        # Manejar errores
        print("Error al agregar empleado:", e)
        
def editar_rol_service(Codigo, Nombre, SueldoPorHora):
    try:
        # Obtener la conexión a la base de datos
        connection = get_connection()
        cursor = connection.cursor()

        # Llamar al procedimiento almacenado para editar un rol
        cursor.callproc('editar_rol', (Codigo, Nombre, SueldoPorHora))
        
        # Commit para aplicar los cambios en la base de datos
        connection.commit()
        
        # Cerrar conexión y cursor
        cursor.close()
        connection.close()
        
    except Exception as e:
        # Manejar errores
        print("Error al editar rol:", e)
        raise e
        
def delete_rol_service(Codigo):
    try:
        connection = get_connection()
        cursor = connection.cursor()

        # Llamar al procedimiento almacenado para eliminar un rol
        cursor.callproc('eliminar_rol', (Codigo,))
        
        # Commit para aplicar los cambios en la base de datos
        connection.commit()
        
        # Cerrar conexión y cursor
        cursor.close()
        connection.close()
        
    except Exception as e:
        # Manejar errores
        print("Error al eliminar rol:", e)
        raise e
       
        
#{
#    "Nombre": "Limpieza",
#    "SueldoPorHora": 20.50
#}

