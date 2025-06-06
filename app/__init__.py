from flask import Flask
from config import Config
from app.extensions import db

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    with app.app_context():
        db.create_all()

    from .controllers.administrator_controller import admin_bp
    from .controllers.user_controller import users_bp

    app.register_blueprint(users_bp, url_prefix='/api/user')
    app.register_blueprint(admin_bp, url_prefix='/api/admin')#

    return app
