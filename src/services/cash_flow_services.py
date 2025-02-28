"""Módulo para gerenciar os fluxos de caixa dos eventos"""
from marshmallow import ValidationError
from src.schemas.cash_flow_schema import CashFlowSchema, CashFlowUpdateSchema
from src.repositories.cash_flow_repository import CashFlowRepository
from src.repositories.event_repository import EventRepository


class CashFlowServices:
    """Classe que encapsula a lógica de negócios relacionada a fluxos de caixa."""

    def __init__(self):
        self.cash_flow_schema = CashFlowSchema()
        self.cash_flow_update_schema = CashFlowUpdateSchema()
        self.cash_flow_repository = CashFlowRepository()
        self.event_repository = EventRepository()

    #validar no services se o id do evento existe
    def create_cash_flow(self, data: dict) -> dict:
        """Valida os dados e cria um novo fluxo de caixa, atualizando o budget do evento."""
        try:
            cash_flow_data = self.cash_flow_schema.load(data)
        except ValidationError as e:
            raise ValueError(f"Erro de validação: {e.messages}") from e

        self._get_event_or_raise(cash_flow_data["event_id"])

        cash_flow = self.cash_flow_repository.create(cash_flow_data)

        self._update_event_budget(cash_flow.event_id, cash_flow.value, cash_flow.flow_type)

        return cash_flow.to_dict()

    def get_cash_flow_by_id(self, cash_flow_id: int) -> dict:
        """Retorna o fluxo de caixa com o ID especificado."""
        cash_flow = self.cash_flow_repository.find_by_id(cash_flow_id)

        if not cash_flow:
            raise ValueError(f"Fluxo de caixa não encontrado como o id: '{cash_flow_id}'.")

        return cash_flow.to_dict()

    def update_cash_flow(self, cash_flow_id: int, updated_data: dict) -> dict:
        """Atualiza os dados do fluxo de caixa e reflete no budget do evento."""
        cash_flow = self.cash_flow_repository.find_by_id(cash_flow_id)
        if not cash_flow:
            raise ValueError(f"Fluxo de caixa não encontrado com id: '{cash_flow_id}'.")

        forbidden_fields = ['cash_flow_id', 'created_at', 'updated_at', 'event_id']
        for field in forbidden_fields:
            if field in updated_data:
                raise ValueError(f"O campo '{field}' não pode ser alterado.")

        try:
            updated_data_validated = self.cash_flow_update_schema.load(updated_data)
        except ValidationError as e:
            raise ValueError(f"Erro de validação na atualização: {e.messages}") from e

        self._update_event_budget(cash_flow.event_id, -cash_flow.value, cash_flow.flow_type)

        updated_cash_flow = self.cash_flow_repository.update(cash_flow_id, **updated_data_validated)
        if not updated_cash_flow:
            raise ValueError("Falha ao atualizar o fluxo de caixa")

        self._update_event_budget(updated_cash_flow.event_id, updated_cash_flow.value, updated_cash_flow.flow_type)

        return updated_cash_flow.to_dict()

    def delete_cash_flow(self, cash_flow_id: int) -> dict:
        """Deleta o fluxo de caixa com o ID especificado e ajusta o budget do evento."""
        cash_flow = self.cash_flow_repository.find_by_id(cash_flow_id)

        if not cash_flow:
            raise ValueError(f"Fluxo de caixa não encontrado com o id: '{cash_flow_id}'.")

        deleted_cash_flow = self.cash_flow_repository.delete(cash_flow_id)

        self._update_event_budget(cash_flow.event_id, -cash_flow.value, cash_flow.flow_type)

        return deleted_cash_flow.to_dict()

    def get_cash_flows_by_event(self, event_id:int) -> list[dict]:
        """Retorna todos os fluxo de caixa do evento com o id especificado"""

        self._get_event_or_raise(event_id)

        cash_flows = self.cash_flow_repository.get_cash_flows_by_event(event_id)

        return [cash_flow.to_dict() for cash_flow in cash_flows]

    def _update_event_budget(self, event_id: int, value: float, flow_type: str) -> None:
        """Atualiza o saldo (budget) do evento com base no fluxo de caixa."""
        event = self._get_event_or_raise(event_id)

        if flow_type == "earning":
            event.budget += value
        elif flow_type == "expense":
            event.budget -= value

        self.event_repository.update(event_id)

    def _get_event_or_raise(self, event_id: int):
        """Obtém um evento ou levanta um erro caso não seja encontrado."""
        event = self.event_repository.get_by_id(event_id)
        if not event:
            raise ValueError(f"Nenhum evento encontrado com id: '{event_id}'")
        return event
