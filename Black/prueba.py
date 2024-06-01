from flask import Flask, jsonify
import unittest
from unittest.mock import patch
from src.routes.routes_empleados import add_empleado

class TestAddEmpleadoRoute(unittest.TestCase):
    def setUp(self):
        # Crear una instancia de Flask y configurarla para pruebas
        self.app = Flask(__name__)
        self.app.config['TESTING'] = True

    def test_add_empleado_route(self):
        # Configura el contexto de la aplicación para la prueba
        with self.app.test_request_context('/add_empleados/', method='POST', 
                                           json={
                                               'RUT': '12243672-9',
                                               'Nombre': 'Juan',
                                               'Apellidos': 'Pérez',
                                               'CodRol': '1',
                                               'TotalHoras': 40,
                                               'SueldoTotal': 1000
                                           }):
            # Llama a la función de la ruta directamente
            response = add_empleado()
            
            # Verifica que la respuesta sea un JSON con el mensaje esperado
            expected_response = jsonify({"message": "Empleado agregado exitosamente"})
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.get_json(), expected_response.get_json())

if __name__ == '__main__':
    unittest.main()
