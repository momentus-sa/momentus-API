"""Módulo destinado a definição do relacionamento entre os membros de time e suas funções"""
from src.extensions import db

class TeamMemberRoles(db.Model):
    """Classe que define os atributos do relacionamento de membros e funções no banco de dados"""
    __tablename__ = 'team_member_roles'

    team_member_id = db.Column(db.Integer, db.ForeignKey('team_member.id'), primary_key=True)
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'), primary_key=True)
