from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from .config import ORACLE_URI  # si vas a usar Oracle, cámbialo en el config

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # Configuración de BD (ajusta si usarás Oracle o MySQL)
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///productos.db"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    CORS(app)  # 🔓 Permite solicitudes desde el frontend

    # Registrar blueprint
    from .routes import productos_bp
    app.register_blueprint(productos_bp, url_prefix="/v1/api")

    return app
