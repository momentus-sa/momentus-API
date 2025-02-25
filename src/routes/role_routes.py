"""Módulo que registra as rotas das roles"""
from flask import Blueprint
from src.controller.roles_controller import RoleController

role_controller = RoleController()

role_bp = Blueprint(
    name='roles',
    import_name=__name__,
    url_prefix="/roles"
)

@role_bp.post("/")
def create_role():
    """Cria uma nova role e retorna o status da criação."""
    return role_controller.create_role()

@role_bp.get("/<int:role_id>")
def get_role_by_id(role_id):
    """Retorna a role pelo ID especificado."""
    return role_controller.get_role_by_id(role_id)

# @role_bp.get("/<int:event_id>/roles")
# def get_roles_by_event(event_id):
#     """Retorna todas as roles associadas a um evento específico."""
#     return role_controller.get_roles_by_event(event_id)

@role_bp.put("/<int:role_id>")
def update_role(role_id):
    """Atualiza a role com o ID especificado. Retorna o status da atualização."""
    return role_controller.update_role(role_id)

@role_bp.delete("/<int:role_id>")
def delete_role(role_id):
    """Deleta a role com o ID especificado. Retorna o status da exclusão."""
    return role_controller.delete_role(role_id)
