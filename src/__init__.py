"""Módulo para criar o app (servidor)"""
from flask import Flask, request, jsonify
from src.extensions import db, migrate, jwt
from src.routes import register_routes
from config import DevelopmentConfig, ProductionConfig
from src.models.activity import Activity
from src.models.cash_flow import CashFlow
from src.models.event_category import EventCategory
from src.models.event import Event
from src.models.task import Task
from src.models.team_member import TeamMember
from src.models.team_member_task import TeamMemberTask
from src.models.ticket import Ticket
from src.models.user import User


def create_app():
    """Cria o server e inicializa alguns módulos"""
    app = Flask(__name__)
    app.config.from_object(ProductionConfig)

    # Extensões:
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)

    register_routes(app)

    return app
