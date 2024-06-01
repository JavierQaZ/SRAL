from flask import Flask
from .routes import routes
from .routes import routes_empleados
from flask_cors import CORS

app = Flask(__name__)

def create_connection(Config):

    app.config.from_object(Config)


    CORS(app, resources={"/add_empleados/": {"origins": "http://localhost:3000", "methods": ["POST"]}})
    
    with app.app_context():
        # Importar rutas
        # Registrar rutas
        app.register_blueprint(routes.bp)
        app.register_blueprint(routes_empleados.bp, url_prefix ="/add_empleados")
    return app
