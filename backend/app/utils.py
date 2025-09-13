# app/utils.py
#Este archivo puede contener funciones auxiliares como la prueba directa con oracledb:
import oracledb
from .config import DB_USER, DB_PASS, DB_HOST, DB_PORT, DB_SERVICE

# Construir el DSN dinámicamente
dsn = f"{DB_HOST}:{DB_PORT}/{DB_SERVICE}"


def get_connection():
    """
    Establece una conexión a Oracle usando credenciales del config.
    Retorna la conexión o lanza excepción en caso de error.
    """
    return oracledb.connect(
        user=DB_USER,
        password=DB_PASS,
        dsn=dsn
    )


def test_oracle_connection():
    """
    Prueba la conexión a Oracle y lista registros de la tabla PRODUCTOS.
    """
    try:
        conn = get_connection()
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM PRODUCTOS")
            rows = cursor.fetchall()
            if rows:
                print("✅ Productos encontrados:")
                for row in rows:
                    print(row)
                return rows
            else:
                print("⚠️ No hay registros en la tabla PRODUCTOS.")
                return []
    except oracledb.DatabaseError as e:
        print(f"❌ Error al conectar/consultar Oracle: {error.message}")
        return {"error": error.message}
    finally:
        if "conn" in locals() and conn:
            conn.close()