"""Módulo destinado ao controller das tarefas"""
from flask import Blueprint
from src.controller.task_controller import TaskController

task_controller = TaskController()

task_bp = Blueprint(
    name='tasks',
    import_name=__name__,
    url_prefix="/tasks"
)


@task_bp.post("/")
def create_task():
    """Cria uma nova tarefa e retorna o status da criação."""
    return task_controller.create_task()


@task_bp.get("/<int:task_id>")
def get_task_by_id(task_id):
    """Retorna a tarefa com o ID especificado."""
    return task_controller.get_task_by_id(task_id)


@task_bp.get("/event/<int:event_id>")
def get_tasks_by_event(event_id):
    """Retorna as tarefas associadas a um evento específico."""
    return task_controller.get_tasks_by_event(event_id)


@task_bp.get("/team_member/<int:team_member_id>")
def get_tasks_by_team_member(team_member_id):
    """Retorna as tarefas atribuídas a um membro específico da equipe."""
    return task_controller.get_tasks_by_team_member(team_member_id)


@task_bp.put("/<int:task_id>")
def update_task(task_id):
    """Atualiza a tarefa com o ID especificado."""
    return task_controller.update_task(task_id)


@task_bp.delete("/<int:task_id>")
def delete_task(task_id):
    """Deleta a tarefa com o ID especificado."""
    return task_controller.delete_task(task_id)


@task_bp.post("/<int:task_id>/assign/<int:team_member_id>")
def add_task_to_member(task_id, team_member_id):
    """Adiciona uma tarefa a um membro específico da equipe."""
    return task_controller.add_task_to_member(task_id, team_member_id)


@task_bp.delete("/<int:task_id>/remove/<int:team_member_id>")
def remove_task_from_member(task_id, team_member_id):
    """Remove uma tarefa de um membro específico da equipe."""
    return task_controller.remove_task_from_member(task_id, team_member_id)
