""""Módulo destinado a definição das funções no banco de dados"""
from datetime import datetime
from src.extensions import db

class Role(db.Model):
    """Classe que define as funções dos membros de time no banco de dados"""
    __tablename__ = 'roles'

    role_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

    members = db.relationship('TeamMember', secondary='team_member_roles', back_populates='roles')

    def to_dict(self):
        """Converte a instância do Role em um dicionário."""
        return {
            'role_id': self.role_id,
            'name': self.name,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }
