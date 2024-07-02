CREATE TABLE `usuarios` (
  `id` int NOT NULL AUTO_INCREMENT,
  `rut_empleado` varchar(15) NOT NULL,
  `contrasena` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `rut_empleado_unique` (`rut_empleado`),
  CONSTRAINT `usuarios_empleado_fk` FOREIGN KEY (`rut_empleado`) REFERENCES `empleados` (`rut_empleado`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


