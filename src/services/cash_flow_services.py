"""Módulo para gerenciar os fluxos de caixa dos eventos"""
from marshmallow import ValidationError
from src.schemas.cash_flow_schema import CashFlowSchema, CashFlowUpdateSchema
from src.repositories.cash_flow_repository import CashFlowRepository


class CashFlowServices:
    """Classe que encapsula a lógica de negócios relacionada a fluxos de caixa."""

    def __init__(self):
        self.cash_flow_schema = CashFlowSchema()
        self.cash_flow_update_schema = CashFlowUpdateSchema()
        self.cash_flow_repository = CashFlowRepository()

    def create_cash_flow(self, data: dict) -> dict:
        """Valida os dados e cria um novo fluxo de caixa."""
        try:
            cash_flow_data = self.cash_flow_schema.load(data)
        except ValidationError as e:
            raise ValueError(f"Erro de validação: {e.messages}") from e

        return self.cash_flow_repository.create(cash_flow_data).to_dict()

    def get_cash_flow_by_id(self, cash_flow_id: int) -> dict:
        """Retorna o fluxo de caixa com o ID especificado."""
        cash_flow = self.cash_flow_repository.find_by_id(cash_flow_id)
        if not cash_flow:
            raise ValueError(f"Fluxo de caixa não encontrado como o id: '{cash_flow_id}'.")
        return cash_flow.to_dict()

    def update_cash_flow(self, cash_flow_id: int, updated_data: dict) -> dict:
        """Atualiza os dados do fluxo de caixa com base no dicionário especificado."""
        cash_flow = self.cash_flow_repository.find_by_id(cash_flow_id)
        if not cash_flow:
            raise ValueError(f"Fluxo de caixa não encontrado com o id: '{cash_flow_id}'.")

        forbidden_fields = ['cash_flow_id', 'created_at', 'updated_at', 'event_id']

        for field in forbidden_fields:
            if field in updated_data:
                raise ValueError(f"O campo '{field}' não pode ser alterado.")

        try:
            updated_data_validated = self.cash_flow_update_schema.load(updated_data)
        except ValidationError as e:
            raise ValueError(f"Erro de validação na atualização: {e.messages}") from e

        updated_cash_flow = self.cash_flow_repository.update(
            cash_flow_id, **updated_data_validated)
        if not updated_cash_flow:
            raise ValueError("Falha ao atualizar o fluxo de caixa")

        return updated_cash_flow.to_dict()

    def delete_cash_flow(self, cash_flow_id: int) -> dict:
        """Deleta o fluxo de caixa com o ID especificado."""
        cash_flow = self.cash_flow_repository.delete(cash_flow_id)
        if not cash_flow:
            raise ValueError(
                f"Fluxo de caixa não encontrado com o id: '{cash_flow_id}'.")
        return cash_flow.to_dict()
