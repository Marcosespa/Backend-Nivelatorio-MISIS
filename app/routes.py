from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from app import db
from app.models import Usuario, Tarea, Categoria
from datetime import datetime

main_routes = Blueprint('main', __name__)

# Endpoint para obtener todas las tareas de un usuario
@main_routes.route('/usuarios/<int:usuario_id>/tareas', methods=['GET'])
@jwt_required()
def obtener_tareas(usuario_id):
    tareas = Tarea.query.filter_by(id_usuario=usuario_id).all()
    return jsonify([{
        'id': tarea.id,
        'texto_tarea': tarea.texto_tarea,
        'fecha_creacion': tarea.fecha_creacion,
        'estado': tarea.estado
    } for tarea in tareas])

# Endpoint para crear una tarea

@main_routes.route('/tareas', methods=['POST'])
@jwt_required()
def crear_tarea():
    data = request.get_json()
    # Verificar si se proporcionó un id_categoria
    if 'id_categoria' in data:
        # Verificar si la categoría existe
        categoria = Categoria.query.get(data['id_categoria'])
        if not categoria:
            return jsonify({"mensaje": "La categoría no existe"}), 400  # 400: Bad Request

    # Convertir la cadena de fecha a un objeto date
    try:
        fecha_creacion = datetime.strptime(data['fecha_creacion'], '%Y-%m-%d').date()
    except ValueError:
        return jsonify({"mensaje": "Formato de fecha inválido. Use 'YYYY-MM-DD'"}), 400

    # Crear la tarea
    nueva_tarea = Tarea(
        texto_tarea=data['texto_tarea'],
        fecha_creacion=fecha_creacion,  
        id_usuario=data['id_usuario'],
        id_categoria=data.get('id_categoria')  
    )

    # Guardar la tarea en la base de datos
    db.session.add(nueva_tarea)
    db.session.commit()

    return jsonify({"mensaje": "Tarea creada"}), 201

# @main_routes.route('/tareas', methods=['POST'])
# @jwt_required()
# def crear_tarea():
#     data = request.get_json()

#     # Verificar si se proporcionó un id_categoria
#     if 'id_categoria' in data:
#         # Verificar si la categoría existe
#         categoria = Categoria.query.get(data['id_categoria'])
#         if not categoria:
#             return jsonify({"mensaje": "La categoría no existe"}), 400  # 400: Bad Request

#     # Crear la tarea
#     nueva_tarea = Tarea(
#         texto_tarea=data['texto_tarea'],
#         fecha_creacion=data['fecha_creacion'],
#         id_usuario=data['id_usuario'],
#         id_categoria=data.get('id_categoria')  # Opcional
#     )

#     # Guardar la tarea en la base de datos
#     db.session.add(nueva_tarea)
#     db.session.commit()

#     return jsonify({"mensaje": "Tarea creada"}), 201



# Endpoint para eliminar una tarea
@main_routes.route('/tareas/<int:tarea_id>', methods=['DELETE'])
@jwt_required()
def eliminar_tarea(tarea_id):
    tarea = Tarea.query.get_or_404(tarea_id)
    db.session.delete(tarea)
    db.session.commit()
    return jsonify({"mensaje": "Tarea eliminada"}), 200

@main_routes.route('/tareas/<int:tarea_id>', methods=['PUT'])
@jwt_required()
def actualizar_tarea(tarea_id):
    tarea = Tarea.query.get_or_404(tarea_id)
    data = request.get_json()

    if 'texto_tarea' in data:
        tarea.texto_tarea = data['texto_tarea']
    if 'estado' in data:
        tarea.estado = data['estado']

    db.session.commit()
    return jsonify({"mensaje": "Tarea actualizada"}), 200

@main_routes.route('/tareas/<int:tarea_id>', methods=['GET'])
@jwt_required()
def obtener_tarea(tarea_id):
    tarea = Tarea.query.get_or_404(tarea_id)
    return jsonify({
        'id': tarea.id,
        'texto_tarea': tarea.texto_tarea,
        'fecha_creacion': tarea.fecha_creacion,
        'estado': tarea.estado
    }), 200