from app import create_app, db
from app.utils import test_oracle_connection

app = create_app()

if __name__ == "__main__":
    print("🔎 Probando conexión a Oracle...")
    result = test_oracle_connection()
    
    if isinstance(result, dict) and "error" in result:
        print("⚠️ No se pudo establecer la conexión con Oracle. Revisa credenciales o servicio.")
    else:
        print("✅ Conexión exitosa.")

    # Crear tablas si no existen
    with app.app_context():
        # 👉 Importar modelos aquí dentro para evitar circular imports
        from app import models  
        db.create_all()
        print("📦 Tablas creadas/verificadas en Oracle.")

    # Levantar servidor
    app.run(host="0.0.0.0", port=5000, debug=True)
