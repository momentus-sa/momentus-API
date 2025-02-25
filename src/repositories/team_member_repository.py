"""Módulo de camada intermediária entre os membros do time e o sistema"""
from src.extensions import db
from src.models.team_member import TeamMember
from src.repositories.role_repository import RoleRepository

#trocar todos os person_name por member_name

class TeamMemberRepository:
    """Classe que interliga os membros do time e o sistema"""

    def __init__(self):
        self.role_repository = RoleRepository()

    def create(self, data: dict) -> TeamMember:
        """Cria um novo membro de time com suas funções"""
        new_member = TeamMember(
            member_name=data["member_name"],
            event_id=data["event_id"]
        )

        roles_data = data.get("roles", [])
        for role_name in roles_data:
            role = self.role_repository.find_by_name(role_name)
            if not role:
                role = self.role_repository.create(role_name)
            new_member.roles.append(role)

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

    def add_role_to_member(self, member_id: int, role_id: int) -> TeamMember:
        """Adiciona uma role a um membro"""
        member = self.find_by_id(member_id)
        if not member:
            return None

        role = self.role_repository.find_by_id(role_id)
        if not role:
            return None

        member.roles.append(role)
        db.session.commit()

        return member

    def get_roles_for_member(self, member_id: int) -> list[str]:
        """Retorna as funções de um membro"""
        member = self.find_by_id(member_id)

        if not member:
            return []

        return [role.name for role in member.roles]

    # def get_all_roles_of_event(self, event_id: int) -> list[str]:
    #     """Retorna todas as roles distintas associadas aos membros de um evento."""
    #     members = TeamMember.query.filter_by(event_id=event_id).all()

    #     distinct_roles = set()

    #     for member in members:
    #         for role in member.roles:
    #             distinct_roles.add(role.name)

    #     return list(distinct_roles)

    def update_member_role(self, member_id: int, role_id: int, new_role_name: str) -> TeamMember:
        """Atualiza o nome da role de um membro utilizando o ID da role"""

        member = TeamMember.query.get(member_id)
        if not member:
            return None

        role = next((role for role in member.roles if role.id == role_id), None)
        if not role:
            return None

        updated_role = self.role_repository.update(role_id, new_role_name)
        if not updated_role:
            return None

        db.session.commit()

        return member

    def remove_role_from_member(self, member_id: int, role_id: int) -> TeamMember:
        """Remove uma função de um membro"""
        member = self.find_by_id(member_id)
        if not member:
            return None

        role = self.role_repository.find_by_id(role_id)
        if role and role in member.roles:
            member.roles.remove(role)

        db.session.commit()
        return member
