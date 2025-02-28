"""Módulo que registra as rotas das atividades"""
from flask import Blueprint
from src.controller.activity_controller import ActivityController

activity_controller = ActivityController()

activity_bp = Blueprint(
    name="activities",
    import_name=__name__,
    url_prefix="/activities"
)


@activity_bp.post("/")
def create_activity():
    """Cria uma nova atividade e retorna o status da criação."""
    return activity_controller.create_activity()


@activity_bp.get("/<int:activity_id>")
def get_activity_by_id(activity_id):
    """Retorna a atividade pelo ID especificado."""
    return activity_controller.get_activity_by_id(activity_id)


@activity_bp.get("/event/<int:event_id>")
def get_all_by_event(event_id):
    """Retorna todas as atividades associadas a um evento específico."""
    return activity_controller.get_all_by_event(event_id)


@activity_bp.get("/upcoming/<int:event_id>")
def get_upcoming_activities(event_id):
    """Retorna todas as atividades futuras de um evento específico."""
    return activity_controller.get_upcoming_activities(event_id)


@activity_bp.put("/<int:activity_id>")
def update_activity(activity_id):
    """Atualiza a atividade com o ID especificado. Retorna o status da atualização."""
    return activity_controller.update_activity(activity_id)


@activity_bp.delete("/<int:activity_id>")
def delete_activity(activity_id):
    """Deleta a atividade com o ID especificado. Retorna o status da exclusão."""
    return activity_controller.delete_activity(activity_id)
