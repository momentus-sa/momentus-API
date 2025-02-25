"""Módulo para gerenciar os ingressos dos eventos"""
from marshmallow import ValidationError
from src.schemas.ticket_schema import TicketSchema, TicketUpdateSchema
from src.repositories.ticket_repository import TicketRepository

class TicketServices:
    """Classe que encapsula a lógica de negócios relacionada aos ingressos."""

    def __init__(self):
        self.ticket_schema = TicketSchema()
        self.ticket_update_schema = TicketUpdateSchema()
        self.ticket_repository = TicketRepository()

    def _validate_unique_name(self, ticket_type: str) -> None:
        """Verifica se já existe um ingresso com o mesmo nome"""
        if self.ticket_repository.find_by_type(ticket_type):
            raise ValueError(f"Já existe um ingresso com o nome: {ticket_type}.")

    def create_ticket(self, data: dict) -> dict:
        """Valida os dados e cria um novo ingresso."""
        try:
            ticket_data = self.ticket_schema.load(data)
        except ValidationError as e:
            raise ValueError(f"Erro de validação: {e.messages}") from e

        self._validate_unique_name(ticket_data.get('ticket_type'))

        return self.ticket_repository.create(ticket_data).to_dict()

    def get_ticket_by_id(self, ticket_id: int) -> dict:
        """Retorna o ingresso com o ID especificado."""
        ticket = self.ticket_repository.find_by_id(ticket_id)
        if not ticket:
            raise ValueError(f"Ingresso não encontrado com o id: '{ticket_id}'.")
        return ticket.to_dict()

    def update_ticket(self, ticket_id: int, updated_data: dict) -> dict:
        """Atualiza os dados do ingresso com base no dicionário especificado."""
        ticket = self.ticket_repository.find_by_id(ticket_id)
        if not ticket:
            raise ValueError(f"Ingresso não encontrado com o id: '{ticket_id}'.")

        try:
            updated_data_validated = self.ticket_update_schema.load(updated_data)
        except ValidationError as e:
            raise ValueError(f"Erro de validação na atualização: {e.messages}") from e

        if "price" in updated_data_validated and updated_data_validated["price"] <= 0:
            raise ValueError("O preço do ingresso deve ser um valor positivo.")

        if 'ticket_type' in updated_data_validated:
            self._validate_unique_name(updated_data_validated['ticket_type'])

        updated_ticket = self.ticket_repository.update(ticket_id, **updated_data_validated)
        if not updated_ticket:
            raise ValueError("Falha ao atualizar o ingresso")

        return updated_ticket.to_dict()

    def delete_ticket(self, ticket_id: int) -> dict:
        """Deleta o ingresso com o ID especificado."""
        ticket = self.ticket_repository.delete(ticket_id)
        if not ticket:
            raise ValueError(f"Ingresso não encontrado com o id: '{ticket_id}'.")
        return ticket.to_dict()

    def sell_ticket(self, ticket_id: int, quantity: int) -> dict:
        """Realiza a venda de ingressos, verificando a disponibilidade."""
        if quantity <= 0:
            raise ValueError("A quantidade deve ser um número positivo.")

        ticket = self.ticket_repository.find_by_id(ticket_id)
        if not ticket:
            raise ValueError(f"Ingresso não encontrado com o id: '{ticket_id}'.")

        available_quantity = ticket.total_available_quantity - ticket.sold_quantity

        if available_quantity < quantity:
            raise ValueError("Quantidade insuficiente de ingressos disponíveis.") #,409

        ticket.sold_quantity += quantity
        updated_ticket = self.ticket_repository.update(ticket_id, sold_quantity=ticket.sold_quantity)

        return updated_ticket.to_dict()

    def get_available_tickets(self, event_id: int) -> list[dict]:
        """Retorna todos os ingressos disponíveis para um determinado evento."""
        tickets = self.ticket_repository.get_available_tickets(event_id)
        available_tickets = [ticket.to_dict() for ticket in tickets if ticket.available_quantity > 0]

        return available_tickets
