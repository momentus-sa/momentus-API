"""Módulo que registra as rotas dos ingressos"""
from flask import Blueprint
from src.controller.ticket_controller import TicketController

ticket_controller = TicketController()

ticket_bp = Blueprint(
    name='ticket',
    import_name=__name__,
    url_prefix="/tickets"
)


@ticket_bp.post("/")
def create_ticket():
    """Cria um novo ingresso e retorna o status da criação."""
    return ticket_controller.create_ticket()


@ticket_bp.get("/<int:ticket_id>")
def get_ticket_by_id(ticket_id):
    """Retorna o ingresso pelo ID especificado."""
    return ticket_controller.get_ticket_by_id(ticket_id)


@ticket_bp.put("/<int:ticket_id>")
def update_ticket(ticket_id):
    """Atualiza o ingresso com o ID especificado. Retorna o status da atualização."""
    return ticket_controller.update_ticket(ticket_id)


@ticket_bp.delete("/<int:ticket_id>")
def delete_ticket(ticket_id):
    """Deleta o ingresso com o ID especificado. Retorna o status da exclusão."""
    return ticket_controller.delete_ticket(ticket_id)


@ticket_bp.post("/<int:ticket_id>/sell")
def sell_ticket(ticket_id):
    """Vende ingressos. Recebe a quantidade a ser vendida e retorna o status da venda."""
    return ticket_controller.sell_ticket(ticket_id)


@ticket_bp.get("/<int:event_id>/available")
def get_available_tickets(event_id):
    """Retorna todos os ingressos disponíveis para um evento específico."""
    return ticket_controller.get_available_tickets(event_id)
