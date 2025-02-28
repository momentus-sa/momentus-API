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

    def get_all_user_events(self, user_id: str) -> list[dict]:
        """Retorna todos os eventos criados por um usuário especificado."""
        events = self.event_repository.get_all_user_events(user_id)
        return [event.to_dict() for event in events]

    def update_event(self, event_id: int, updated_data: dict, user_id: str) -> tuple:
        """Lógica de negócios para atualizar um evento, garantindo que o usuário seja o dono"""
        event = self.event_repository.get_by_id(event_id)
        if not event:
            raise ValueError(f"Evento não encontrado com o id: '{event_id}'.")

        if str(event.event_creator_id) != str(user_id):
            return {"error": "Você não tem permissão para atualizar este evento."}, 403

        try:
            validated_data = self.event_update_schema.load(updated_data)
        except ValidationError as e:
            return {"error": f"Erro de validação: {e.messages}"}, 400

        updated_event = self.event_repository.update(event_id, **validated_data)
        if not updated_event:
            return {"error": "Erro ao tentar atualizar o evento."}, 500

        return updated_event.to_dict(), 200

    def delete_event(self, event_id: int, user_id) -> dict:
        """Deleta o evento com o ID especificado."""

        event = self.event_repository.get_by_id(event_id)
        if not event:
            raise ValueError(f"Evento não encontrado com o id: '{event_id}'.")

        if str(event.event_creator_id) != str(user_id):
            return {"error": "Você não tem permissão para excluir este evento."}, 403

        deleted_event = self.event_repository.delete(event_id)
        if not deleted_event:
            raise ValueError(f"Erro ao tentar deletar o evento com o id: '{event_id}'.")

        return {"message": "Evento deletado com sucesso."}, 200
