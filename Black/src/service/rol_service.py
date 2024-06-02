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
        
        
        
        
#{
#    "Nombre": "Limpieza",
#    "SueldoPorHora": 20.50
#}


#DELIMITER // Procedimiento almacenado
#
#CREATE PROCEDURE agregar_rol (
#    IN p_Nombre VARCHAR(100),
#    IN p_SueldoPorHora DECIMAL(10, 2)
#)
#BEGIN
#    INSERT INTO rol (Nombre, SueldoPorHora)
#    VALUES (p_Nombre, p_SueldoPorHora);
#END //
#
#DELIMITER ;