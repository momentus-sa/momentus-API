"""Módulo para gerenciar os eventos"""
from marshmallow import ValidationError
from src.schemas.event_schema import EventSchema, EventUpdateSchema
from src.repositories.event_repository import EventRepository

class EventServices:
    """Classe que encapsula a lógica de negócios relacionada aos eventos."""

    def __init__(self):
        self.event_schema = EventSchema()
        self.event_update_schema = EventUpdateSchema()
        self.event_repository = EventRepository()

    def create_event(self, data: dict) -> dict:
        """Valida os dados e cria um novo evento."""
        try:
            event_data = self.event_schema.load(data)
        except ValidationError as e:
            raise ValueError(f"Erro de validação: {e.messages}") from e

        created_event = self.event_repository.create(event_data)

        return created_event.to_dict()

    def get_event_by_id(self, event_id: int) -> dict:
        """Retorna o evento com o ID especificado."""
        event = self.event_repository.get_by_id(event_id)
        if not event:
            raise ValueError(f"Evento não encontrado com o id: '{event_id}'.")
        return event.to_dict()

    def get_all_events(self) -> list[dict]:
        """Retorna todos os eventos registrados."""
        events = self.event_repository.get_all()
        return [event.to_dict() for event in events]

    def get_upcoming_events(self) -> list[dict]:
        """Retorna os eventos futuros."""
        events = self.event_repository.get_upcoming_events()
        return [event.to_dict() for event in events]

    def update_event(self, event_id: int, updated_data: dict) -> dict:
        """Atualiza os dados do evento com base no dicionário especificado."""
        event = self.event_repository.find_by_id(event_id)
        if not event:
            raise ValueError(f"Evento não encontrado com o id: '{event_id}'.")

        try:
            updated_data_validated = self.event_update_schema.load(updated_data)
        except ValidationError as e:
            raise ValueError(f"Erro de validação na atualização: {e.messages}") from e

        updated_event = self.event_repository.update(event_id, **updated_data_validated)
        if not updated_event:
            raise ValueError("Falha ao atualizar o evento.")

        return updated_event.to_dict()

    def deactivate_event(self, event_id: int) -> dict:
        """Desativa um evento (define o campo 'active' como False)."""
        event = self.event_repository.deactivate_event(event_id)
        if not event:
            raise ValueError(f"Evento não encontrado com o id: '{event_id}'.")
        return event.to_dict()

    def delete_event(self, event_id: int) -> dict:
        """Deleta o evento com o ID especificado."""
        event = self.event_repository.delete(event_id)
        if not event:
            raise ValueError(f"Evento não encontrado com o id: '{event_id}'.")
        return event.to_dict()
