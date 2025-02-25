"""Módulo destinado a definição dos times no banco de dados"""
from datetime import datetime
from src.extensions import db

class TeamMember(db.Model):
    """"Classe que define os atributos dos times no banco de dados"""
    __tablename__ = 'team_members'

    team_member_id = db.Column(db.Integer, primary_key=True)
    member_name = db.Column(db.String(100), nullable=False)
    event_id = db.Column(db.Integer, db.ForeignKey('event.id'), nullable=False)

    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

    roles = db.relationship('Role', secondary='team_member_roles', back_populates='members')


    def to_dict(self):
        """Retorna o objeto TeamMember na forma de um dicionário"""
        return {
            'id': self.id,
            'person_name': self.person_name,
            'event_id': self.event_id,
            'roles': [role.name for role in self.roles],
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }
