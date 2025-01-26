from app import db

class Usuario(db.Model):
    __tablename__ = 'usuarios'

    id = db.Column(db.Integer, primary_key=True)
    nombre_usuario = db.Column(db.String(100), nullable=False)
    contrasena = db.Column(db.String(100), nullable=False)
    imagen_perfil = db.Column(db.String(255), nullable=True)

    # Relación con tareas
    tareas = db.relationship('Tarea', backref='usuario', lazy=True)


class Categoria(db.Model):
    __tablename__ = 'categorias'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.String(255), nullable=True)

    # Relación con tareas
    tareas = db.relationship('Tarea', backref='categoria', lazy=True)


class Tarea(db.Model):
    __tablename__ = 'tareas'

    id = db.Column(db.Integer, primary_key=True)
    texto_tarea = db.Column(db.String(255), nullable=False)
    fecha_creacion = db.Column(db.Date, nullable=False)
    fecha_tentativa_finalizacion = db.Column(db.Date, nullable=True)
    estado = db.Column(db.String(50), nullable=False, default='Pendiente')

    # Foreign keys
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)
    id_categoria = db.Column(db.Integer, db.ForeignKey('categorias.id'), nullable=True)