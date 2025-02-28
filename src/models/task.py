""""Módulo destinado a definição das funções no banco de dados"""
from datetime import datetime
from src.extensions import db
from src.models.team_member_task import TeamMemberTask

class Task(db.Model):
    """Classe que define as tarefas no banco de dados"""
    __tablename__ = 'tasks'

    task_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=False)

    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

    # Relacionamento com a tabela intermediária
    team_member_tasks = db.relationship('TeamMemberTask', back_populates='task')

    def to_dict(self):
        """Converte a instância da tarefa em um dicionário"""
        return {
            'task_id': self.task_id,
            'name': self.name,
            'description': self.description,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }