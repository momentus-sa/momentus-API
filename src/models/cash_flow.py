"""Módulo destinado a definção dos fluxos de caixa no banco de dados"""
from datetime import datetime
from src.extensions import db

class CashFlow(db.Model):
    """Classe que define os atributos dos fluxos de caixa no banco de dados"""
    __tablename__ = 'cash_flows'

    cash_flow_id = db.Column(db.Integer, primary_key=True,nullable=False, autoincrement=True)
    title = db.Column(db.String(50), nullable = False)
    description = db.Column(db.String(200))
    flow_type = db.Column(db.Enum('earning', 'expense', name = 'flow_type', nullable= False))
    value = db.Column(db.Numeric(precision= 10, scale= 2), nullable= False)
    answerable = db.Column(db.String(50), nullable= False)
    spent_at = db.Column(db.DateTime)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)

    #Relacionamento com o evento
    event_id = db.Column(db.Integer, db.ForeignKey('events.event_id'), nullable=False)
    event = db.relationship('Event', back_populates='cash_flows')


    def to_dict(self)->dict:
        """Retorna o objeto CashFlow na forma de dicionário"""
        return {
            "cash_flow_id": self.cash_flow_id,
            "event_id": self.event_id,
            "title": self.title,
            "description": self.description,
            "flow_type": self.flow_type,
            "value": self.value,
            "answerable": self.answerable,
            "spent_at": self.spent_at,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }
