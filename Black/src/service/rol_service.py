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
        
        
        
#{
#    "Nombre": "Limpieza",
#    "SueldoPorHora": 20.50
#}


#DELIMITER // Procedimiento almacenado Add
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

#DELIMITER // Procedimiento almacenado Edit
#
#CREATE PROCEDURE editar_rol (
#    IN p_Codigo INT,
#    IN p_Nombre VARCHAR(100),
#    IN p_SueldoPorHora DECIMAL(10, 2)
#)
#BEGIN
#    UPDATE rol
#    SET Nombre = p_Nombre,
#        SueldoPorHora = p_SueldoPorHora
#    WHERE Codigo = p_Codigo;
#END //
#
#DELIMITER ;
