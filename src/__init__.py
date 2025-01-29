"""Módulo para criar o app (servidor)"""
from flask import Flask, request, jsonify
# from src.routes import register_routes
from config import DevelopmentConfig, ProductionConfig
from src.routes.user_routes import user_bp
from src.extensions import db, migrate
from src.models import *


def create_app():
    """Cria o server e inicializa alguns módulos"""
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)

    db.init_app(app)
    migrate.init_app(app, db)

    # register_routes(app)
    app.register_blueprint(user_bp)
    #url_prefix='/api'

    return app
