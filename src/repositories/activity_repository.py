"""Módulo de camada intermediária entre o banco de dados das atividades e o sistema"""
from datetime import timedelta
from src.extensions import db
from src.models.activity import Activity
from src.repositories.event_repository import EventRepository


class ActivityRepository:
    """Classe que interliga o banco de dados de atividades e o sistema"""
    def __init__(self):
        self.event_repository = EventRepository()


    def create(self, data: dict) -> Activity:
        """Cria uma nova atividade de acordo com os campos do dicionário"""
        new_activity = Activity(
            event_id= data["event_id"],
            name=data["name"],
            description=data.get("description"),
            activity_time=data["activity_time"],
        )

        db.session.add(new_activity)
        db.session.commit()

        return new_activity

    def find_by_id(self, activity_id: int) -> Activity:
        """
        Retorna uma atividade que possui o id especificado no parâmetro |
        Caso não encontre nenhuma atividade com o id especificado, retorna None
        """
        return Activity.query.filter_by(activity_id=activity_id).first()

    def find_by_name(self, name: str) -> Activity:
        """Retorna uma atividade que possui o nome especificado no parâmetro |
        Caso não encontre nenhuma atividade com o nome especificado, retorna None"""
        return Activity.query.filter_by(name=name).first()

    def get_all_by_event(self, event_id: int) -> list[Activity]:
        """Retorna todas as atividades associadas a um evento específico"""
        return Activity.query.filter_by(event_id=event_id).all()

    def get_upcoming_activities(self, event_id: int, time_window: timedelta = timedelta(days=7)) -> list[Activity]:
        """
        Retorna as atividades que ainda não aconteceram e estão dentro de uma janela de tempo próxima do evento especificado.
        O parâmetro 'time_window' define a proximidade, por exemplo, 7 dias antes do evento.
        """
        event = self.event_repository.get_by_id(event_id)
        if not event:
            return []

        upcoming_start_time = event.event_date - time_window  # Data de início da janela de tempo
        upcoming_end_time = event.event_date + time_window  # Data de término da janela de tempo

        activities = self.get_all_by_event(event_id)

        upcoming_activities = [
            activity for activity in activities
            if upcoming_start_time <= activity.activity_time <= upcoming_end_time and activity.activity_time > db.func.now()
        ]

        return upcoming_activities

    def update(self, activity_id: int, **kwargs) -> Activity:
        """Atualiza os campos da atividade de acordo com os valores fornecidos
        Caso não encontre nenhuma atividade com o id especificado, retorna None"""
        activity = self.find_by_id(activity_id)

        if not activity:
            return None

        for key, value in kwargs.items():
            if hasattr(activity, key):
                setattr(activity, key, value)

        db.session.commit()

        return activity

    def delete(self, activity_id: int) -> Activity:
        """
        Deleta a atividade com o id especificado e a retorna |
        Caso não encontre nenhuma atividade com o id especificado, retorna None
        """
        activity = self.find_by_id(activity_id)
        if not activity:
            return None

        db.session.delete(activity)
        db.session.commit()

        return activity
