"""Módulo que registra as rotas dos membros de time"""
from flask import Blueprint
from src.controller.team_member_controller import TeamMemberController

team_member_controller = TeamMemberController()

team_member_bp = Blueprint(
    name='team_members',
    import_name=__name__,
    url_prefix="/team-members"
)

@team_member_bp.post("/")
def create_member():
    """Cria um novo membro de time e retorna o status da criação."""
    return team_member_controller.create_member()

@team_member_bp.get("/<int:member_id>")
def get_member_by_id(member_id):
    """Retorna o membro com o ID especificado."""
    return team_member_controller.get_member_by_id(member_id)


@team_member_bp.get("/event/<int:event_id>")
def get_members_by_event(event_id):
    """Retorna todos os membros do evento com o id especificado"""
    return team_member_controller.get_members_by_event(event_id)

@team_member_bp.put("/<int:member_id>")
def update_member(member_id):
    """Atualiza os dados do membro com o ID especificado. Retorna o status da atualização."""
    return team_member_controller.update_member(member_id)

@team_member_bp.delete("/<int:member_id>")
def delete_member(member_id):
    """Deleta o membro com o ID especificado. Retorna o status da exclusão."""
    return team_member_controller.delete_member(member_id)
