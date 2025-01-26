from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from app import db
from app.models import Usuario, Tarea, Categoria

category_routes= Blueprint('category', __name__)

@category_routes.route('/categorias', methods=['POST'])
@jwt_required()
def crear_categoria():
    data = request.get_json()
    nueva_categoria = Categoria(
        nombre=data['nombre'],
        descripcion=data.get('descripcion')
    )
    db.session.add(nueva_categoria)
    db.session.commit()
    return jsonify({"mensaje": "Categoría creada"}), 201

@category_routes.route('/categorias/<int:categoria_id>', methods=['DELETE'])
@jwt_required()
def eliminar_categoria(categoria_id):
    categoria = Categoria.query.get_or_404(categoria_id)
    db.session.delete(categoria)
    db.session.commit()
    return jsonify({"mensaje": "Categoría eliminada"}), 200

@category_routes.route('/categorias', methods=['GET'])
@jwt_required()
def obtener_categorias():
    categorias = Categoria.query.all()
    return jsonify([{
        'id': categoria.id,
        'nombre': categoria.nombre,
        'descripcion': categoria.descripcion
    } for categoria in categorias]), 200

@category_routes.route('/categorias/<int:categoria_id>', methods=['PUT'])
@jwt_required()
def actualizar_categoria(categoria_id):
    categoria = Categoria.query.get_or_404(categoria_id)
    data = request.get_json()

    if 'nombre' in data:
        categoria.nombre = data['nombre']
    if 'descripcion' in data:
        categoria.descripcion = data['descripcion']

    db.session.commit()
    return jsonify({"mensaje": "Categoría actualizada"}), 200