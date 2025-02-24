"""Módulo para criar o app (servidor)"""
from flask import Flask, request, jsonify
from src.routes import register_routes
from config import DevelopmentConfig, ProductionConfig
from src.extensions import db, migrate, jwt
from src.models import *


def create_app():
    """Cria o server e inicializa alguns módulos"""
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)

    #Extensões:
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)

    register_routes(app)

    return app
