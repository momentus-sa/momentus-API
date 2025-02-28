from flask import request, jsonify, Response
from src.services.task_services import TaskServices

class TaskController(object):
    """Classe que representa o controller das tarefas"""

    def __init__(self):
        self.service = TaskServices()

    def create_task(self) -> tuple[Response, int]:
        """Serviço que cria uma nova tarefa"""
        if not request.is_json:
            return jsonify({"error": "O corpo da requisição deve estar no formato JSON"}), 400

        data = request.get_json()

        try:
            task = self.service.create_task(data)
            return jsonify(task), 201

        except ValueError as e:
            return jsonify({"error": str(e)}), 400

    def get_task_by_id(self, task_id: int) -> tuple[Response, int]:
        """Retorna a tarefa com o ID especificado"""
        try:
            task = self.service.get_task_by_id(task_id)
            return jsonify(task), 200
        except ValueError as e:
            return jsonify({"error": str(e)}), 404

    def get_tasks_by_event(self, event_id: int) -> tuple[Response, int]:
        """Retorna as tarefas associadas a um evento específico"""
        try:
            tasks = self.service.get_tasks_by_event(event_id)
            return jsonify(tasks), 200
        except ValueError as e:
            return jsonify({"error": str(e)}), 400

    def get_tasks_by_team_member(self, team_member_id: int) -> tuple[Response, int]:
        """Retorna as tarefas atribuídas a um membro específico da equipe"""
        try:
            tasks = self.service.get_tasks_by_team_member(team_member_id)
            return jsonify(tasks), 200
        except ValueError as e:
            return jsonify({"error": str(e)}), 400

    def update_task(self, task_id: int) -> tuple[Response, int]:
        """Atualiza os dados da tarefa com o ID especificado"""
        if not request.is_json:
            return jsonify({"error": "O corpo da requisição deve estar no formato JSON"}), 400

        data = request.get_json()

        try:
            updated_task = self.service.update_task(task_id, data)
            return jsonify(updated_task), 202

        except ValueError as e:
            return jsonify({"error": str(e)}), 400

    def delete_task(self, task_id: int) -> tuple[Response, int]:
        """Deleta a tarefa com o ID especificado"""
        try:
            self.service.delete_task(task_id)
            return jsonify({"message": "Tarefa deletada com sucesso"}), 200
        except ValueError as e:
            return jsonify({"error": str(e)}), 404

    def add_task_to_member(self, task_id: int, team_member_id: int) -> tuple[Response, int]:
        """Adiciona uma tarefa a um membro de time específico"""
        try:
            task = self.service.add_task_to_member(task_id, team_member_id)
            return jsonify(task), 200
        except ValueError as e:
            return jsonify({"error": str(e)}), 400

    def remove_task_from_member(self, task_id: int, team_member_id: int) -> tuple[Response, int]:
        """Remove uma tarefa de um membro de time específico"""
        try:
            task = self.service.remove_task_from_member(task_id, team_member_id)
            return jsonify(task), 200
        except ValueError as e:
            return jsonify({"error": str(e)}), 400