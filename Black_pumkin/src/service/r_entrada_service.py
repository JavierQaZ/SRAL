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


#CREATE TABLE registro_diario (
#    ID INT AUTO_INCREMENT PRIMARY KEY,
#    RUT VARCHAR(15),
#    Fecha DATE,
#    HoraEntrada DATETIME,
#    HoraSalida DATETIME,
#    FOREIGN KEY (RUT) REFERENCES empleados(RUT)
#);

#DELIMITER //
#
#CREATE TRIGGER after_insert_registroentrada
#AFTER INSERT ON registroentrada
#FOR EACH ROW
#BEGIN
#    DECLARE fecha_entrada DATE;
#    SET fecha_entrada = DATE(NEW.HoraIngreso);
#    
#    UPDATE registro_diario
#    SET HoraEntrada = NEW.HoraIngreso
#    WHERE RUT = NEW.RUT
#    AND Fecha = fecha_entrada;
#    
#    IF ROW_COUNT() = 0 THEN
#        INSERT INTO registro_diario (RUT, Fecha, HoraEntrada)
#        VALUES (NEW.RUT, fecha_entrada, NEW.HoraIngreso);
#    END IF;
#END//
#
#DELIMITER ;

#
#CREATE TRIGGER after_insert_registrosalida
#AFTER INSERT ON registrosalida
#FOR EACH ROW
#BEGIN
#    DECLARE fecha_salida DATE;
#    SET fecha_salida = DATE(NEW.HoraSalida);
#    
#    UPDATE registro_diario
#    SET HoraSalida = NEW.HoraSalida
#    WHERE RUT = NEW.RUT
#    AND Fecha = fecha_salida;
#    
#    IF ROW_COUNT() = 0 THEN
#        INSERT INTO registro_diario (RUT, Fecha, HoraSalida)
#        VALUES (NEW.RUT, fecha_salida, NEW.HoraSalida);
#    END IF;
#END//

