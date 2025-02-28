"""Módulo destinado a definição dos times no banco de dados"""
from datetime import datetime
from src.extensions import db
from src.models.team_member_task import TeamMemberTask

class TeamMember(db.Model):
    """Classe que define os atributos dos membros do time no banco de dados"""
    __tablename__ = 'team_members'

    team_member_id = db.Column(db.Integer, primary_key=True)
    member_name = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(50), nullable=False, default="Equipe de organização")
    event_id = db.Column(db.Integer, db.ForeignKey('events.event_id'), nullable=False)

    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

    # Relacionamento com as tarefas
    tasks = db.relationship('TeamMemberTask', back_populates='team_member')

    event = db.relationship('Event', back_populates='team_members')

    def to_dict(self):
        """Retorna o objeto TeamMember na forma de um dicionário"""
        return {
            'team_member_id': self.team_member_id,
            'member_name': self.member_name,
            'role': self.role,
            'event_id': self.event_id,
            'tasks': [task.task.name for task in self.tasks],  # Retorna os nomes das tarefas
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }
