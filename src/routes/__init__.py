"""
Este módulo tem como objetivo registrar todos os blueprints da API 
de forma centralizada para facilitar a modularização do sistema
"""
from flask import Blueprint
from src.routes.user_routes import user_bp
from src.routes.event_category_routes import event_category_bp
from src.routes.cash_flow_routes import cash_flow_bp

# Blueprint principal
momentus_bp = Blueprint('momentus', __name__, url_prefix='/momentus')

def register_routes(app):
    """Registra todas as rotas da API de forma centralizada"""
    momentus_bp.register_blueprint(user_bp)
    momentus_bp.register_blueprint(event_category_bp)
    momentus_bp.register_blueprint(cash_flow_bp)

    app.register_blueprint(momentus_bp)
