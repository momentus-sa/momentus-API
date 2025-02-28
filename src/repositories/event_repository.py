"""Módulo destinado à camada intermediária entre o banco de dados de eventos e o sistema"""
import uuid
import re
from src.extensions import db
from src.models.event import Event

class EventRepository:
    """Classe que interliga o banco de dados de eventos e o sistema"""


    def _generate_registration_link(self, event_name: str) -> str:
        """Gera um link de registro para o evento"""

        event_slug = re.sub(r'[^a-z0-9\s-]', '', event_name.lower())
        event_slug = re.sub(r'[\s-]+', '-', event_slug)

        unique_id = uuid.uuid4().hex
        registration_link = f"https://www.momentus/register/{event_slug}-{unique_id}"

        return registration_link

    def create(self, data: dict) -> Event:
        """Cria um novo evento de acordo com os campos do dicionário"""

        name = data["name"]

        new_event = Event(
            name= name,
            description=data.get("description"),
            location=data.get("location"),
            event_picture_url=data.get("event_picture_url"),
            event_date=data["event_date"],
            registration_link= self._generate_registration_link(name),
            budget=data.get("budget", 0),
            event_creator_id=data["event_creator_id"],
        )

        db.session.add(new_event)
        db.session.commit()

        return new_event

    def get_by_id(self, event_id: int) -> Event:
        """Retorna um evento com o id especificado | Caso não encontre nenhum, retorna None"""
        return Event.query.filter_by(event_id=event_id).first()

    def get_by_name(self, name: str) -> Event:
        """Retorna um evento com o nome especificado | Caso não encontre nenhum, etorna None"""
        return Event.query.filter_by(name=name).first()

    def get_all(self) -> list[Event]:
        """Retorna todos os eventos registrados"""
        return Event.query.all()

    def get_upcoming_events(self) -> list[Event]:
        """Retorna os eventos que ainda não aconteceram (baseado na data atual)"""
        return Event.query.filter(Event.event_date > db.func.now()).all()

    def update(self, event_id: int, **kwargs) -> Event:
        """Atualiza os campos do evento de acordo com os valores fornecidos | Caso não encontre nenhum evento com o id especificado, retorna None"""
        event = self.get_by_id(event_id)

        if not event:
            return None

        for key, value in kwargs.items():
            if hasattr(event, key):
                setattr(event, key, value)

        db.session.commit()

        return event

    def deactivate_event(self, event_id: int) -> Event:
        """Desativa um evento (define o campo 'active' como False)"""
        event = Event.query.filter_by(event_id=event_id).first()

        if not event:
            return None  # Caso o evento não seja encontrado

        # Alterando o status para inativo
        event.active = False
        db.session.commit()

        return event

    def delete(self, event_id: int) -> Event:
        """Deleta o evento com o id especificado e o retorna | Caso não encontre nenhum evento com o id especificado, retorna None"""
        event = self.get_by_id(event_id)
        if not event:
            return None

        db.session.delete(event)
        db.session.commit()

        return event
