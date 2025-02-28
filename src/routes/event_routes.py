"""Módulo de camada intermediária entre o controller de eventos e o sistema"""
from flask import Blueprint
from flask_jwt_extended import jwt_required
from src.controller.event_controller import EventController

event_controller = EventController()

event_bp = Blueprint(
    name='events',
    import_name=__name__,
    url_prefix="/events"
)


@event_bp.post('/create')
@jwt_required()
def create_event():
    """Cria um novo evento e associa ao usuário autenticado"""
    return event_controller.create_event()


@event_bp.get('/<int:event_id>')
def get_event_by_id(event_id: int):
    """Retorna um evento pelo ID"""
    return event_controller.get_event_by_id(event_id)


@event_bp.get('/')
def get_all_events():
    """Retorna todos os eventos"""
    return event_controller.get_all_events()


@event_bp.get('/upcoming')
def get_upcoming_events():
    """Retorna os eventos futuros"""
    return event_controller.get_upcoming_events()


@event_bp.get('/user/:user_id')
def get_all_user_events(user_id:int):
    """Retorna todos os eventos"""
    return event_controller.get_all_user_events(user_id)


@event_bp.get('/category/<int:category_id>')
@jwt_required()
def get_events_by_category(category_id: int):
    """Retorna todos os eventos associados a uma categoria específica"""
    return event_controller.get_events_by_category(category_id)


@event_bp.put('/<int:event_id>')
@jwt_required()
def update_event(event_id: int):
    """Atualiza os dados de um evento"""
    return event_controller.update_event(event_id)


@event_bp.delete('/<int:event_id>')
@jwt_required()
def delete_event(event_id: int):
    """Deleta um evento"""
    return event_controller.delete_event(event_id)
