"""Módulo de camada intermediária entre os membros do time e o sistema"""
from src.extensions import db
from src.models.team_member import TeamMember
from src.repositories.task_repository import TaskRepository

class TeamMemberRepository:
    """Classe que interliga os membros do time e o sistema"""

    def __init__(self):
        self.task_repository = TaskRepository()

    def create(self, data: dict) -> TeamMember:
        """Cria um novo membro de time com suas tarefas"""
        new_member = TeamMember(
            member_name=data["member_name"],
            event_id=data["event_id"],
            task=data["task"]  # Alterado de role
        )

        tasks_data = data.get("tasks", [])
        for task_name in tasks_data:
            task = self.task_repository.find_by_name(task_name)
            if not task:
                task = self.task_repository.create(task_name)
            new_member.tasks.append(task)

        db.session.add(new_member)
        db.session.commit()
        return new_member

    def find_by_id(self, member_id: int) -> TeamMember:
        """Retorna um membro de time que possui o id especificado no parâmetro"""
        return TeamMember.query.get(member_id)

    def find_by_name_and_event(self, member_name: str, event_id: int) -> TeamMember:
        """Busca um membro pelo nome e pelo ID do evento"""
        return TeamMember.query.filter_by(member_name=member_name, event_id=event_id).first()

    def get_members_by_event(self, event_id: int) -> list[TeamMember]:
        """Retorna todos os membros de um evento específico"""
        return TeamMember.query.filter_by(event_id=event_id).all()

    def update(self, member_id: int, **kwargs) -> TeamMember:
        """Atualiza os campos do membro de time de acordo com os campos do dicionário"""
        member = self.find_by_id(member_id)

        if not member:
            return None

        for key, value in kwargs.items():
            if hasattr(member, key):
                setattr(member, key, value)

        db.session.commit()

        return member

    def delete(self, member_id: int) -> TeamMember:
        """Deleta um membro de time pelo id"""
        member = self.find_by_id(member_id)
        if not member:
            return None

        db.session.delete(member)
        db.session.commit()

        return member
