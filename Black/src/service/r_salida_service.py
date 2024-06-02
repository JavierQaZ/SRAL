from ..database.db_conección import get_connection

def add_r_salida_service(HoraSalida, RUT):
    try:
        connection = get_connection()
        cursor = connection.cursor()

        # Llamar al procedimiento almacenado para agregar una hora de salida
        cursor.callproc('agregar_hora_salida', (HoraSalida, RUT))
        
        # Commit para aplicar los cambios en la base de datos
        connection.commit()
        
        # Cerrar conexión y cursor
        cursor.close()
        connection.close()
        
    except Exception as e:
        # Manejar errores
        print("Error al agregar hora de salida:", e)
        raise e


def edit_r_salida_service(HoraSalida, RUT):
    try:
        connection = get_connection()
        cursor = connection.cursor()

        # Llamar al procedimiento almacenado para editar la hora de salida
        cursor.callproc('editar_hora_salida', (HoraSalida, RUT))
        
        # Commit para aplicar los cambios en la base de datos
        connection.commit()
        
        # Cerrar conexión y cursor
        cursor.close()
        connection.close()
        
    except Exception as e:
        # Manejar errores
        print("Error al editar la hora de salida:", e)
        raise e

def delete_r_salida_service(HoraSalida, RUT):
    try:
        connection = get_connection()
        cursor = connection.cursor()

        # Llamar al procedimiento almacenado para eliminar un registro de salida
        cursor.callproc('eliminar_r_salida', (HoraSalida, RUT))
        
        # Commit para aplicar los cambios en la base de datos
        connection.commit()
        
        # Cerrar conexión y cursor
        cursor.close()
        connection.close()
        
    except Exception as e:
        # Manejar errores
        print("Error al eliminar registro de salida:", e)
        raise e
    
#DELIMITER //

#CREATE PROCEDURE agregar_hora_salida (
#    IN p_HoraSalida DATETIME,
#    IN p_RUT VARCHAR(15)
#)
#BEGIN
#    INSERT INTO registrosalida (HoraSalida, RUT)
#    VALUES (p_HoraSalida, p_RUT);
#END //
#
#DELIMITER ;

#{ 
#	"HoraSalida": "2024-06-01T08:08:54",
#	"RUT": "12345678-9"
#}

#DELIMITER //

#DELIMITER //

#DELIMITER //

#CREATE PROCEDURE editar_hora_salida (
#    IN p_HoraSalida DATETIME,
#    IN p_RUT VARCHAR(255)
#)
#BEGIN
#    UPDATE registrosalida
#    SET HoraSalida = p_HoraSalida
#    WHERE RUT = p_RUT;
#END //

#DELIMITER ;