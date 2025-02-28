""""Módulo destinado a definção dos ingressos no banco de dados"""
from datetime import datetime
from src.extensions import db

class Activity(db.Model):
    """Classe que define as atividades no banco de dados"""
    activity_id = db.Column(db.Integer, primary_key=True)
    event_id = db.Column(db.Integer, db.ForeignKey('events.event_id'), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    activity_time = db.Column(db.DateTime, nullable=False)

    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

    event = db.relationship('Event', back_populates='activities')

    def to_dict(self):
        """Retorna o objeto activity na forma de um dicionário"""
        return {
            "activity_id": self.activity_id,
            "name": self.name,
            "description": self.description,
            "activity_time": self.activity_time.isoformat(),
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }
