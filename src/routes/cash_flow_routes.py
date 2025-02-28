"""Módulo que registra as rotas dos fluxos de caixa"""
from flask import Blueprint
from src.controller.cash_flow_controller import CashFlowController

cash_flow_controller = CashFlowController()

cash_flow_bp = Blueprint(
    name='cash_flows',
    import_name=__name__,
    url_prefix="/cash-flows"
)


@cash_flow_bp.post("/")
def create_cash_flow():
    """Cria um novo fluxo de caixa e retorna o status da criação."""
    return cash_flow_controller.create_cash_flow()


@cash_flow_bp.get("/<int:cash_flow_id>")
def get_cash_flow_by_id(cash_flow_id):
    """Retorna o fluxo de caixa pelo ID especificado."""
    return cash_flow_controller.get_cash_flow_by_id(cash_flow_id)


@cash_flow_bp.get("/event/<int:event_id>")
def get_cash_flows_by_event(event_id):
    """Retorna todos os fluxos de caixa do evento com o ID especificado."""
    return cash_flow_controller.get_cash_flows_by_event(event_id)


@cash_flow_bp.put("/<int:cash_flow_id>")
def update_cash_flow(cash_flow_id):
    """Atualiza o fluxo de caixa com o ID especificado. Retorna o status da atualização."""
    return cash_flow_controller.update_cash_flow(cash_flow_id)


@cash_flow_bp.delete("/<int:cash_flow_id>")
def delete_cash_flow(cash_flow_id):
    """Deleta o fluxo de caixa com o ID especificado. Retorna o status da exclusão."""
    return cash_flow_controller.delete_cash_flow(cash_flow_id)
