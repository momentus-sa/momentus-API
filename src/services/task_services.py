from marshmallow import ValidationError
from src.schemas.task_schema import TaskSchema, TaskUpdateSchema
from src.repositories.task_repository import TaskRepository
from src.repositories.team_member_repository import TeamMemberRepository

class TaskServices:
    """Classe que encapsula a lógica de negócios relacionada às tarefas."""

    def __init__(self):
        self.task_schema = TaskSchema()
        self.task_update_schema = TaskUpdateSchema()
        self.task_repository = TaskRepository()
        self.team_member_repository = TeamMemberRepository()

    def _validate_unique_name(self, task_name: str) -> None:
        """Verifica se já existe uma tarefa com o mesmo nome"""
        if self.task_repository.find_by_name(task_name):
            raise ValueError(f"Já existe uma tarefa com o nome: {task_name}.")

    def create_task(self, data: dict) -> dict:
        """Valida os dados e cria uma nova tarefa."""
        try:
            task_data = self.task_schema.load(data)
        except ValidationError as e:
            raise ValueError(f"Erro de validação: {e.messages}") from e

        self._validate_unique_name(task_data.get('name'))

        return self.task_repository.create(task_data).to_dict()

    def get_task_by_id(self, task_id: int) -> dict:
        """Retorna a tarefa com o ID especificado."""
        task = self.task_repository.find_by_id(task_id)
        if not task:
            raise ValueError(f"Tarefa não encontrada com o id: '{task_id}'.")
        return task.to_dict()

    def get_tasks_by_event(self, event_id: int) -> list[dict]:
        """Retorna todas as tarefas associadas a um evento específico."""
        tasks = self.task_repository.get_tasks_by_event(event_id)
        return [task.to_dict() for task in tasks]

    def get_tasks_by_team_member(self, team_member_id: int) -> list[dict]:
        """Retorna todas as tarefas atribuídas a um membro da equipe específico."""
        tasks = self.task_repository.get_tasks_by_team_member(team_member_id)
        return [task.to_dict() for task in tasks]

    def update_task(self, task_id: int, updated_data: dict) -> dict:
        """Atualiza os dados da tarefa com base no dicionário especificado."""
        task = self.task_repository.find_by_id(task_id)
        if not task:
            raise ValueError(f"Tarefa não encontrada com o id: '{task_id}'.")

        try:
            updated_data_validated = self.task_update_schema.load(updated_data)
        except ValidationError as e:
            raise ValueError(f"Erro de validação na atualização: {e.messages}") from e

        if 'name' in updated_data_validated:
            self._validate_unique_name(updated_data_validated['name'])

        updated_task = self.task_repository.update(task_id, **updated_data_validated)
        if not updated_task:
            raise ValueError("Falha ao atualizar a tarefa")

        return updated_task.to_dict()

    def delete_task(self, task_id: int) -> dict:
        """Deleta a tarefa com o ID especificado."""
        task = self.task_repository.delete(task_id)
        if not task:
            raise ValueError(f"Tarefa não encontrada com o id: '{task_id}'.")
        return task.to_dict()

    def add_task_to_member(self, task_id: int, team_member_id: int) -> dict:
        """Adiciona uma tarefa a um membro de time específico."""
        task = self.task_repository.find_by_id(task_id)
        if not task:
            raise ValueError(f"Tarefa não encontrada com o id: '{task_id}'.")

        team_member = self.team_member_repository.find_by_id(team_member_id)
        if not team_member:
            raise ValueError(f"Membro de time não encontrado com o id: '{team_member_id}'.")

        self.task_repository.assign_to_member(task_id, team_member_id)

        return task.to_dict()

    def remove_task_from_member(self, task_id: int, team_member_id: int) -> dict:
        """Remove uma tarefa de um membro de time específico."""
        task = self.task_repository.find_by_id(task_id)
        if not task:
            raise ValueError(f"Tarefa não encontrada com o id: '{task_id}'.")

        team_member = self.team_member_repository.find_by_id(team_member_id)
        if not team_member:
            raise ValueError(f"Membro de time não encontrado com o id: '{team_member_id}'.")

        self.task_repository.remove_from_member(task_id, team_member_id)

        return task.to_dict()
