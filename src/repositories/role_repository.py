"""Módulo de camada intermediária entre o banco de dados das funções e o sistema"""
from src.extensions import db
from src.models.role import Role

class RoleRepository:
    """Classe que gerencia as funções no banco de dados"""

    def create(self, role_name: str) -> Role:
        """Cria uma nova função"""
        new_role = Role(role_name=role_name)
        db.session.add(new_role)
        db.session.commit()
        return new_role

    def find_by_name(self, role_name: str) -> Role:
        """Retorna uma função com base no nome fornecido"""
        return Role.query.filter_by(role_name=role_name).first()

    def find_by_id(self, role_id: int) -> Role:
        """Retorna uma função com base no ID fornecido"""
        return Role.query.filter_by(id=role_id).first()

    #Remover
    def get_roles_by_event(self, event_id: int) -> list[Role]:
        """Retorna todas as funções associadas a um evento"""
        return Role.query.filter(Role.event_id == event_id).all()
    
    def update(self, role_id: int, new_name: str) -> Role:
        """Atualiza o nome de uma função existente."""
        role = self.find_by_id(role_id)
        if not role:
            return None

        if role.role_name == new_name:
            return role

        role.role_name = new_name
        db.session.commit()

        return role

    def delete(self, role_id: int) -> Role:
        """Deleta a função com base no ID fornecido"""
        role = self.find_by_id(role_id)
        if not role:
            return None

        db.session.delete(role)
        db.session.commit()
        return role
