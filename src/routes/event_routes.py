"""Módulo de camada intermediária entre o controller de eventos e o sistema"""
from flask import Blueprint
from src.controller.event_controller import EventController

event_controller = EventController()

event_bp = Blueprint(
    name='events',
    import_name=__name__,
    url_prefix="/events"
)

@event_bp.post('/create')
def create_event():
    """Cria um novo evento"""
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

@event_bp.put('/<int:event_id>')
def update_event(event_id: int):
    """Atualiza os dados de um evento"""
    return event_controller.update_event(event_id)

@event_bp.put('/<int:event_id>/deactivate')
def deactivate_event(event_id: int):
    """Desativa um evento"""
    return event_controller.deactivate_event(event_id)

@event_bp.delete('/<int:event_id>')
def delete_event(event_id: int):
    """Deleta um evento"""
    return event_controller.delete_event(event_id)
