from app import create_app ,db
from app.utils import test_oracle_connection

# Probar conexión con Oracle (solo si ya tienes configurado en config.py)
test_oracle_connection()

app = create_app()

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
