from marshmallow import ValidationError
from src.schemas.role_schema import RoleSchema, RoleUpdateSchema
from src.repositories.role_repository import RoleRepository

class RoleServices:
    """Classe que encapsula a lógica de negócios relacionada às roles de membros."""

    def __init__(self):
        self.role_schema = RoleSchema()
        self.role_update_schema = RoleUpdateSchema()
        self.role_repository = RoleRepository()

    def _validate_unique_name(self, role_name: str) -> None:
        """Verifica se já existe uma role com o mesmo nome"""
        if self.role_repository.find_by_name(role_name):
            raise ValueError(f"Já existe uma role com o nome: {role_name}.")

    def create_role(self, data: dict) -> dict:
        """Valida os dados e cria uma nova role."""
        try:
            role_data = self.role_schema.load(data)
        except ValidationError as e:
            raise ValueError(f"Erro de validação: {e.messages}") from e

        self._validate_unique_name(role_data.get('name'))

        return self.role_repository.create(role_data).to_dict()

    def get_role_by_id(self, role_id: int) -> dict:
        """Retorna a role com o ID especificado."""
        role = self.role_repository.find_by_id(role_id)
        if not role:
            raise ValueError(f"Role não encontrada com o id: '{role_id}'.")
        return role.to_dict()

    def update_role(self, role_id: int, updated_data: dict) -> dict:
        """Atualiza os dados da role com base no dicionário especificado."""
        role = self.role_repository.find_by_id(role_id)
        if not role:
            raise ValueError(f"Role não encontrada com o id: '{role_id}'.")

        try:
            updated_data_validated = self.role_update_schema.load(updated_data)
        except ValidationError as e:
            raise ValueError(f"Erro de validação na atualização: {e.messages}") from e

        if 'name' in updated_data_validated:
            self._validate_unique_name(updated_data_validated['name'])

        updated_role = self.role_repository.update(role_id, **updated_data_validated)
        if not updated_role:
            raise ValueError("Falha ao atualizar a role")

        return updated_role.to_dict()

    def delete_role(self, role_id: int) -> dict:
        """Deleta a role com o ID especificado."""
        role = self.role_repository.delete(role_id)
        if not role:
            raise ValueError(f"Role não encontrada com o id: '{role_id}'.")
        return role.to_dict()

    def get_roles_by_event(self, event_id: int) -> list[dict]:
        """Retorna todas as roles associadas a um evento específico."""
        roles = self.role_repository.get_roles_by_event(event_id)
        return [role.to_dict() for role in roles]
