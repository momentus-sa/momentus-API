"""Módulo de camada intermediária entre o banco de dados das tarefas e o sistema"""
from src.extensions import db
from src.models.task import Task
from src.models.team_member import TeamMember

class TaskRepository:
    """Classe que gerencia as tarefas no banco de dados"""

    def create(self, data:dict) -> Task:
        """Cria uma nova tarefa"""
        new_task = Task(
            name= data["name"],
            description= data["description"]
        )
        db.session.add(new_task)
        db.session.commit()
        return new_task

    def find_by_name(self, task_name: str) -> Task:
        """Retorna uma tarefa com base no nome fornecido"""
        return Task.query.filter_by(name=task_name).first()

    def find_by_id(self, task_id: int) -> Task:
        """Retorna uma tarefa com base no ID fornecido"""
        return Task.query.get(task_id) 

    #redundante
    def get_tasks_by_team_member(self, team_member_id: int) -> list[Task]:
        """Retorna todas as tarefas atribuídas a um membro específico da equipe"""
        return Task.query.filter_by(team_member_id=team_member_id).all()

    def get_tasks_by_event(self, event_id: int) -> list[Task]:
        """Retorna todas as tarefas associadas a um evento específico"""
        return Task.query.filter_by(event_id=event_id).all()

    def update(self, task_id: int, new_name: str) -> Task:
        """Atualiza o nome de uma tarefa existente"""
        task = self.find_by_id(task_id)
        if not task:
            return None

        if task.task_name == new_name:
            return task

        task.task_name = new_name
        db.session.commit()
        return task

    def delete(self, task_id: int) -> Task:
        """Deleta a tarefa com base no ID fornecido"""
        task = self.find_by_id(task_id)
        if not task:
            return None

        db.session.delete(task)
        db.session.commit()
        return task

    def assign_to_member(self, task_id: int, member_id: int) -> Task:
        """Associa uma tarefa a um membro do time"""
        task = self.find_by_id(task_id)
        member = TeamMember.query.get(member_id)

        if not task or not member:
            return None

        if task not in member.tasks:
            member.tasks.append(task)

        db.session.commit()
        return task

    def remove_from_member(self, task_id: int, member_id: int) -> Task:
        """Remove uma tarefa de um membro do time"""
        task = self.find_by_id(task_id)
        member = TeamMember.query.get(member_id)

        if not task or not member:
            return None

        if task in member.tasks:
            member.tasks.remove(task)

        db.session.commit()
        return task
