"""Módulo destinado a definição do relacionamento entre os membros de time e suas funções"""
from src.extensions import db

class TeamMemberTask(db.Model):
    """Tabela intermediária para o relacionamento muitos-para-muitos entre TeamMember e Task"""
    __tablename__ = 'team_member_tasks'

    team_member_id = db.Column(db.Integer, db.ForeignKey('team_members.team_member_id'), primary_key=True)
    task_id = db.Column(db.Integer, db.ForeignKey('tasks.task_id'), primary_key=True)

    # Relacionamento com TeamMember e Task
    team_member = db.relationship('TeamMember', back_populates='tasks')
    task = db.relationship('Task', back_populates='team_member_tasks')
