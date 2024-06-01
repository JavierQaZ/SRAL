from flask import Flask
from flask_cors import CORS
from .routes import routes_empleados
from .routes import routes_rol
from .routes import routes_r_entrada
from .routes import routes_r_salida

app = Flask(__name__)

def create_app(Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    # Configurar CORS
    CORS(app, resources={"/empleados/*": {"origins": "http://localhost:3000", "methods": ["POST"]}})
    CORS(app, resources={"/rol/*": {"origins": "http://localhost:3000", "methods": ["POST"]}})
    CORS(app, resources={"/r_entrada/*": {"origins": "http://localhost:3000", "methods": ["POST"]}})
    CORS(app, resources={"/r_salida/*": {"origins": "http://localhost:3000", "methods": ["POST"]}})


    app.register_blueprint(routes_empleados.bp, url_prefix="/empleados")
    app.register_blueprint(routes_rol.bp, url_prefix="/rol")
    app.register_blueprint(routes_r_entrada.bp, url_prefix="/r_entrada")
    app.register_blueprint(routes_r_salida.bp, url_prefix="/r_salida")

    return app
