"""Módulo para gerenciar as atividades dos eventos"""
from marshmallow import ValidationError
from src.schemas.activity_schema import ActivitySchema, ActivityUpdateSchema
from src.repositories.activity_repository import ActivityRepository
from datetime import timedelta
from src.repositories.event_repository import EventRepository


class ActivityServices:
    """Classe que encapsula a lógica de negócios relacionada às atividades."""

    def __init__(self):
        self.activity_schema = ActivitySchema()
        self.activity_update_schema = ActivityUpdateSchema()
        self.activity_repository = ActivityRepository()
        self.event_repository = EventRepository()

    def _validate_event_exists(self, event_id: int) -> None:
        """Verifica se o 'event_id' fornecido existe no banco de dados."""
        if not self.event_repository.get_by_id(event_id):
            raise ValueError(f"Evento com o ID '{event_id}' não encontrado.")

    def create_activity(self, data: dict) -> dict:
        """Valida os dados e cria uma nova atividade."""
        try:
            activity_data = self.activity_schema.load(data)
        except ValidationError as e:
            raise ValueError(f"Erro de validação: {e.messages}") from e
        
        self._validate_event_exists(activity_data["event_id"])

        return self.activity_repository.create(activity_data).to_dict()

    def get_activity_by_id(self, activity_id: int) -> dict:
        """Retorna a atividade com o ID especificado."""
        activity = self.activity_repository.find_by_id(activity_id)
        if not activity:
            raise ValueError(f"Atividade não encontrada com o id: '{activity_id}'.")
        return activity.to_dict()
    
    def get_all_by_event(self, event_id):
        """Retorna todas as atividade do evento com o id especificado"""
        self._validate_event_exists(event_id)
        activities = self.activity_repository.get_all_by_event(event_id)

        return [activity.to_dict() for activity in activities]
    
    def get_upcoming_activities(self, event_id:int, time_window: timedelta = timedelta(days=7)) -> list[dict]:
        """Retorna todas as atividades futuras."""
        self._validate_event_exists(event_id)
        activities = self.activity_repository.get_upcoming_activities(event_id, time_window)

        return [activity.to_dict() for activity in activities]


    def update_activity(self, activity_id: int, updated_data: dict) -> dict:
        """Atualiza os dados da atividade com base no dicionário especificado."""
        activity = self.activity_repository.find_by_id(activity_id)

        if not activity:
            raise ValueError(f"Atividade não encontrada com o id: '{activity_id}'.")

        try:
            updated_data_validated = self.activity_update_schema.load(updated_data)

        except ValidationError as e:
            raise ValueError(f"Erro de validação na atualização: {e.messages}") from e

        updated_activity = self.activity_repository.update(activity_id, **updated_data_validated)
        if not updated_activity:
            raise ValueError(f"Falha ao atualizar a atividade com o id '{activity_id}'")

        return updated_activity.to_dict()

    def delete_activity(self, activity_id: int) -> dict:
        """Deleta a atividade com o ID especificado."""
        activity = self.activity_repository.delete(activity_id)

        if not activity:
            raise ValueError(f"Atividade não encontrada com o id: '{activity_id}'.")

        return activity.to_dict()
