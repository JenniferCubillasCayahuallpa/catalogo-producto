# app/config.py
# Configuración de conexión a Oracle con SQLAlchemy
import os
from dotenv import load_dotenv

# Cargar variables de entorno desde .env
load_dotenv()

# Variables de conexión
DB_USER = os.getenv("DB_USER", "JUANA")
DB_PASS = os.getenv("DB_PASS", "Admin12345")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "1521")
DB_SERVICE = os.getenv("DB_SERVICE", "XEPDB1")

# URI que Flask-SQLAlchemy espera
SQLALCHEMY_DATABASE_URI = (
    f"oracle+oracledb://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/?service_name={DB_SERVICE}"
)
# Config extra
SQLALCHEMY_TRACK_MODIFICATIONS = False