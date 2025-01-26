from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

db = SQLAlchemy()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)

    # Configuración de la aplicación
    app.config.from_object('app.config.Config')
    app.config['JWT_SECRET_KEY'] = 'super-secret-key'  # Cambia esto en producción


    # Inicializar extensiones
    db.init_app(app)
    jwt.init_app(app)

    # Registrar blueprints (rutas)
    from app.routes import main_routes
    from app.auth import auth_routes 
    from app.category import category_routes  
    app.register_blueprint(main_routes)
    app.register_blueprint(auth_routes)
    app.register_blueprint(category_routes)


    return app