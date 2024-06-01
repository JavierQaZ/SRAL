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






#DELIMITER //
#
#CREATE PROCEDURE agregar_hora_ingreso (
#    IN p_HoraIngreso DATETIME,
#    IN p_RUT VARCHAR(15)
#)
#BEGIN
#    INSERT INTO registroentrada (HoraIngreso, RUT)
#    VALUES (p_HoraIngreso, p_RUT);
#END //
#
#DELIMITER ;