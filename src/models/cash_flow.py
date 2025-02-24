"""Módulo destinado a definção dos fluxos de caixa no banco de dados"""
from src.extensions import db


class CashFlow(db.Model):
    """Classe que define os atributos dos fluxos de caixa no banco de dados"""
    __tablename__ = 'cash_flows'

    cash_flow_id = db.Column(db.Integer, primary_key=True,nullable=False, autoincrement=True)
    #event_id = db.Column(db.Integer, db.ForeignKey('events.event_id'))
    title = db.Column(db.String(50), nullable = False)
    description = db.Column(db.String(200))
    flow_type = db.Column(db.Enum('earning', 'expenses', name = 'flow_type', nullable= False))
    value = db.Column(db.Numeric(precision= 10, scale= 2), nullable= False)
    answerable = db.Column(db.String(50), nullable= False)
    spent_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)

    def to_dict(self)->dict:
        """Retorna o objeto CashFlow na forma de dicionário"""
        return {
            "cash_flow_id": self.cash_flow_id,
            "title": self.title,
            "description": self.description,
            "flow_tipe": self.flow_type,
            "value": self.value,
            "answerable": self.answerable,
            "spent_at": self.spent_at,
            "updated_at": self.updated_at
        }
