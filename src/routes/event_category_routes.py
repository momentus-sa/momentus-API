"""Módulo que registra as rotas das categorias de eventos"""
from flask import Blueprint
from src.controller.event_category_controller import EventCategoryController

event_category_controller = EventCategoryController()

event_category_bp = Blueprint(
    name= 'event_category',
    import_name= __name__,
    url_prefix= "/event-category"
)


@event_category_bp.post("/create")
def create_event_category():
    """Cria uma nova categoria de evento. Retorna o status da criação (sucesso ou erro)."""
    return event_category_controller.create_event_category()

@event_category_bp.get("/all")
def get_all_event_categories():
    """Retorna todas as categorias de evento, incluindo as padrão e personalizadas."""
    return event_category_controller.get_all_event_categories()

@event_category_bp.get("/default")
def get_all_default_event_categories():
    """Retorna as categorias de evento padrão."""
    return event_category_controller.get_all_default_event_categories()

@event_category_bp.get("/name/<string:category_name>")
def get_event_category_by_name(category_name):
    """Retorna a categoria de evento pelo nome fornecido."""
    return event_category_controller.get_event_category_by_name(category_name)
