"""" Módulo destinado a definção dos ingressos no banco de dados """
from datetime import datetime
from src.extensions import db

class Ticket(db.Model):
    """Classe que define os atributos dos ingressos no banco de dados"""
    __tablename__ = 'tickets'

    ticket_id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    event_id = db.Column(db.Integer, db.ForeignKey('events.event_id'), nullable=False)
    ticket_type = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Numeric(precision=10, scale=2), nullable=False)
    available_quantity = db.Column(db.Integer, nullable=False, default=0)
    sold_quantity = db.Column(db.Integer, nullable=False, default=0)

    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self) -> dict:
        """Retorna o objeto Ticket na forma de um dicionário"""
        return {
            "ticket_id": self.ticket_id,
            "event_id": self.event_id,
            "ticket_type": self.ticket_type,
            "price": str(self.price),
            "available_quantity": self.available_quantity,
            "sold_quantity": self.sold_quantity,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None
        }
