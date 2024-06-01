from flask import Flask
from flask_cors import CORS
from .routes import routes_empleados

app = Flask(__name__)

def create_app(Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    # Configurar CORS
    CORS(app, resources={"/empleados/*": {"origins": "http://localhost:3000", "methods": ["POST"]}})


    app.register_blueprint(routes_empleados.bp, url_prefix="/empleados")

    return app
