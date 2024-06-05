-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: localhost    Database: black_pumpkin
-- ------------------------------------------------------
-- Server version	8.2.0

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `registrosalida`
--

DROP TABLE IF EXISTS `registrosalida`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `registrosalida` (
  `horaSalida_registro` datetime NOT NULL,
  `rut_empleado` varchar(15) NOT NULL,
  PRIMARY KEY (`horaSalida_registro`,`rut_empleado`),
  KEY `registrosalida_ibfk_1` (`rut_empleado`),
  CONSTRAINT `registrosalida_ibfk_1` FOREIGN KEY (`rut_empleado`) REFERENCES `empleados` (`rut_empleado`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `registrosalida`
--

LOCK TABLES `registrosalida` WRITE;
/*!40000 ALTER TABLE `registrosalida` DISABLE KEYS */;
INSERT INTO `registrosalida` VALUES ('2024-06-04 02:20:49','12345678-7'),('2024-06-05 12:22:27','12345678-7'),('2024-06-04 00:22:27','12345678-8'),('2024-06-03 23:57:55','12345678-9'),('2024-09-01 18:00:00','12345678-9');
/*!40000 ALTER TABLE `registrosalida` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `trigger_actualizar_horas_y_sueldo` AFTER INSERT ON `registrosalida` FOR EACH ROW BEGIN
    DECLARE entrada DATETIME;
    DECLARE horas_trabajadas DECIMAL(10, 2);
    DECLARE total_horas DECIMAL(10, 2);
    DECLARE sueldo_por_hora DECIMAL(10, 2);

    -- Obtener la hora de entrada del mismo día
    SELECT horaIngreso_registro INTO entrada
    FROM registroentrada
    WHERE rut_empleado = NEW.rut_empleado
    AND DATE(horaIngreso_registro) = DATE(NEW.horaSalida_registro)
    LIMIT 1;

    -- Calcular horas trabajadas del día
    SET horas_trabajadas = TIMESTAMPDIFF(HOUR, entrada, NEW.horaSalida_registro);

    -- Obtener el total de horas trabajadas actuales
    SELECT totalHorasTrabajadas_empleado INTO total_horas
    FROM empleados
    WHERE rut_empleado = NEW.rut_empleado;

    -- Actualizar el total de horas trabajadas
    SET total_horas = total_horas + horas_trabajadas;
    UPDATE empleados
    SET totalHorasTrabajadas_empleado = total_horas
    WHERE rut_empleado = NEW.rut_empleado;

    -- Obtener el sueldo por hora del rol del empleado
    SELECT sueldoPorHora_rol INTO sueldo_por_hora
    FROM rol
    WHERE codigo_rol = (SELECT codigo_rol FROM empleados WHERE rut_empleado = NEW.rut_empleado);

    -- Calcular y actualizar el sueldo total
    UPDATE empleados
    SET sueldoTotal_empleado = total_horas * sueldo_por_hora
    WHERE rut_empleado = NEW.rut_empleado;
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-06-04 20:44:57
