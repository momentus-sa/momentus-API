from marshmallow import ValidationError
from src.schemas.team_member_schema import TeamMemberSchema, TeamMemberUpdateSchema
from src.repositories.role_repository import RoleRepository
from src.repositories.team_member_repository import TeamMemberRepository

#ajeitar isso depois
class TeamMemberServices:
    """Classe que encapsula a lógica de negócios relacionada aos membros do time."""

    def __init__(self):
        self.team_member_schema = TeamMemberSchema()
        self.team_member_update_schema = TeamMemberUpdateSchema()
        self.team_member_repository = TeamMemberRepository()
        self.role_repository = RoleRepository()
        #self.event_id = 

    def _validate_unique_member(self, member_name: str, event_id: int) -> None:
        """Verifica se já existe um membro com o mesmo nome e evento"""
        if self.team_member_repository.find_by_name_and_event(member_name, event_id):
            raise ValueError(f"Já existe um membro com o nome '{member_name}' no evento {event_id}.")

    # def _validate_role_exists_in_event(self, role_id: int) -> None:
    #     """Verifica se a role com o id especificado já existe no evento."""
    #     roles = self.team_member_repository.get_all_roles_of_event(role_id)

    #     if not any(role.id == role_id for role in roles):
    #         raise ValueError(f"Role com id: '{role_id}' não encontrada no evento com id: '{event_id}'.")

    def create_member(self, data: dict) -> dict:
        """Valida os dados e cria um novo membro."""
        try:
            member_data = self.team_member_schema.load(data)
        except ValidationError as e:
            raise ValueError(f"Erro de validação: {e.messages}") from e

        self._validate_unique_member(member_data.get('member_name'), member_data.get('event_id'))

        return self.team_member_repository.create(member_data).to_dict()

    def get_member_by_id(self, member_id: int) -> dict:
        """Retorna o membro com o ID especificado."""
        member = self.team_member_repository.find_by_id(member_id)
        if not member:
            raise ValueError(f"Membro não encontrado com o id: '{member_id}'.")
        return member.to_dict()

    def update_member(self, member_id: int, updated_data: dict) -> dict:
        """Atualiza os dados do membro com base no dicionário especificado."""
        member = self.team_member_repository.find_by_id(member_id)
        if not member:
            raise ValueError(f"Membro não encontrado com o id: '{member_id}'.")

        if 'member_name' in updated_data:
            member_name = updated_data['member_name']
            event_id = updated_data.get('event_id', member.event_id)
            self._validate_unique_member(member_name, event_id)

        try:
            updated_data_validated = self.team_member_update_schema.load(updated_data)
        except ValidationError as e:
            raise ValueError(f"Erro de validação na atualização: {e.messages}") from e

        updated_member = self.team_member_repository.update(member_id, **updated_data_validated)
        if not updated_member:
            raise ValueError("Falha ao atualizar o membro")

        return updated_member.to_dict()

    def delete_member(self, member_id: int) -> dict:
        """Deleta o membro com o ID especificado."""
        member = self.team_member_repository.delete(member_id)
        if not member:
            raise ValueError(f"Membro não encontrado com o id: '{member_id}'.")
        return member.to_dict()

    def add_role_to_member(self, member_id: int, role_id: int,) -> dict:
        """Adiciona uma role a um membro do time."""
        # self._validate_role_exists_in_event(role_id)

        member = self.team_member_repository.add_role_to_member(member_id, role_id)
        if not member:
            raise ValueError("Falha ao adicionar a role ao membro")

        return member.to_dict()

    def remove_role_from_member(self, member_id: int, role_id: str) -> dict:
        """Remove uma role de um membro."""
        # self._validate_role_exists_in_event(role_id)

        member = self.team_member_repository.remove_role_from_member(member_id, role_id)
        if not member:
            raise ValueError("Falha ao remover a role do membro")

        return member.to_dict()
