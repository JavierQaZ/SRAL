from ..database.db_conección import get_connection

def add_r_entrada_service(HoraIngreso, RUT):
    try:
        connection = get_connection()
        cursor = connection.cursor()

        # Llamar al procedimiento almacenado para agregar una hora de entrada
        cursor.callproc('agregar_hora_ingreso', (HoraIngreso, RUT))
        
        # Commit para aplicar los cambios en la base de datos
        connection.commit()
        
        # Cerrar conexión y cursor
        cursor.close()
        connection.close()
        
    except Exception as e:
        # Manejar errores
        print("Error al agregar hora de ingreso:", e)
        raise e


def edit_r_entrada_service(HoraIngreso, RUT):
    try:
        connection = get_connection()
        cursor = connection.cursor()

        # Llamar al procedimiento almacenado para editar la hora de ingreso
        cursor.callproc('editar_hora_ingreso', (HoraIngreso, RUT))
        
        # Commit para aplicar los cambios en la base de datos
        connection.commit()
        
        # Cerrar conexión y cursor
        cursor.close()
        connection.close()
        
    except Exception as e:
        # Manejar errores
        print("Error al editar la hora de ingreso:", e)
        raise e

def delete_r_entrada_service(HoraIngreso, RUT):
    try:
        connection = get_connection()
        cursor = connection.cursor()

        # Llamar al procedimiento almacenado para eliminar un registro de entrada
        cursor.callproc('eliminar_hora_salida', (HoraIngreso, RUT))
        
        # Commit para aplicar los cambios en la base de datos
        connection.commit()
        
        # Cerrar conexión y cursor
        cursor.close()
        connection.close()
        
    except Exception as e:
        # Manejar errores
        print("Error al eliminar registro de entrada:", e)
        raise e
#
#{
#	"HoraIngreso": "2024-06-01T08:00:00",
#	"RUT": "1111111-0"
#}