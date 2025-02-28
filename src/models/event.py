"""Módulo destinado à definição dos eventos no banco de dados"""
from datetime import datetime
from sqlalchemy.dialects.postgresql import UUID
from src.extensions import db

class Event(db.Model):
    """Classe que define os atributos do evento no banco de dados"""
    __tablename__ = 'events'

    event_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(200))
    location = db.Column(db.String(100))
    event_picture_url = db.Column(db.String(255))
    event_date = db.Column(db.DateTime, nullable=False)
    registration_link = db.Column(db.String(255))
    budget = db.Column(db.Numeric(precision= 10, scale= 2), nullable= False, default=0)
    active = db.Column(db.Boolean, default=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

    # Relacionamento 1xN com User
    event_creator_id = db.Column(UUID(as_uuid=True), db.ForeignKey("users.user_id"), nullable=False)
    event_creator = db.relationship("User", back_populates="events")
    # Relacionamento 1:N com CashFlow
    cash_flows = db.relationship('CashFlow', back_populates='event', cascade='all, delete-orphan')
    #Relacionamento 1:N com Ticket:
    tickets = db.relationship('Ticket', back_populates='event', cascade='all, delete-orphan')
    # Relacionamento 1:N com Activity (Cronograma de Atividades)
    activities = db.relationship('Activity', back_populates='event', cascade='all, delete-orphan')
    # Relacionamento 1:N com TeamMember
    team_members = db.relationship('TeamMember', back_populates='event', cascade='all, delete-orphan')


    def to_dict(self) -> dict:
        """Retorna o objeto Event na forma de um dicionário"""
        return {
            "event_id": self.event_id,
            "name": self.name,
            "description": self.description,
            "location": self.location,
            "event_creator_id": str(self.event_creator_id),
            "event_creator_name": self.event_creator.name,
            "event_date": self.event_date,
            "active": self.active,
            #"event_creator": self.event_creator.to_dict() if self.event_creator else None,
            #"cash_flows": [cash_flow.to_dict() for cash_flow in self.cash_flows],
            "tickets": [ticket.to_dict() for ticket in self.tickets],
            "created_at": self.created_at.strftime("%d/%m/%Y %H:%M"),
            "updated_at": self.updated_at.strftime("%d/%m/%Y %H:%M"),
        }
