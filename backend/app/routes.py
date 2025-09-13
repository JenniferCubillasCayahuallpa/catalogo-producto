from flask import Blueprint, request, jsonify
from .models import Producto
from . import db

productos_bp = Blueprint("productos", __name__)

# Listar productos
@productos_bp.route("/productos", methods=["GET"])
def listar_productos():
    try:
        nombre = request.args.get("nombre")
        if nombre:
            productos = Producto.query.filter(
                Producto.nombre.ilike(f"%{nombre}%")
            ).all()
        else:
            productos = Producto.query.all()

        return jsonify([p.to_dict() for p in productos]), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Agregar producto
@productos_bp.route("/productos", methods=["POST"])
def agregar_producto():
    try:
        data = request.get_json()
        nuevo = Producto(
            nombre=data["nombre"],
            precio=data["precio"],
            descripcion=data.get("descripcion", ""),
        )
        db.session.add(nuevo)
        db.session.commit()
        return jsonify({"mensaje": "Producto agregado", "producto": nuevo.to_dict()}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500


# Modificar producto
@productos_bp.route("/productos/<int:id>", methods=["PUT"])
def modificar_producto(id):
    try:
        data = request.get_json()
        producto = Producto.query.get_or_404(id)
        producto.nombre = data["nombre"]
        producto.precio = data["precio"]
        producto.descripcion = data.get("descripcion", "")
        db.session.commit()
        return jsonify({"mensaje": "Producto modificado", "producto": producto.to_dict()}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500


# Eliminar producto
@productos_bp.route("/productos/<int:id>", methods=["DELETE"])
def eliminar_producto(id):
    try:
        producto = Producto.query.get_or_404(id)
        db.session.delete(producto)
        db.session.commit()
        return jsonify({"mensaje": "Producto eliminado"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500