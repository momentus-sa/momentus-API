from flask import request, jsonify, Response
from src.services.role_services import RoleServices

class RoleController(object):
    """Classe que representa o controller das roles"""

    def __init__(self):
        self.service = RoleServices()

    def create_role(self) -> tuple[Response, int]:
        """Serviço que cria uma nova role"""
        if not request.is_json:
            return jsonify({"error": "O corpo da requisição deve estar no formato JSON"}), 400

        data = request.get_json()

        try:
            role = self.service.create_role(data)
            return jsonify(role), 201

        except ValueError as e:
            return jsonify({"error": str(e)}), 400

    def get_role_by_id(self, role_id: int) -> tuple[Response, int]:
        """Retorna a role com o ID especificado"""
        try:
            role = self.service.get_role_by_id(role_id)
            return jsonify(role), 200
        except ValueError as e:
            return jsonify({"error": str(e)}), 404

    def update_role(self, role_id: int) -> tuple[Response, int]:
        """Atualiza os dados da role com o ID especificado"""
        if not request.is_json:
            return jsonify({"error": "O corpo da requisição deve estar no formato JSON"}), 400

        data = request.get_json()

        try:
            updated_role = self.service.update_role(role_id, data)
            return jsonify(updated_role), 202

        except ValueError as e:
            return jsonify({"error": str(e)}), 400

    def delete_role(self, role_id: int) -> tuple[Response, int]:
        """Deleta a role com o ID especificado"""
        try:
            self.service.delete_role(role_id)
            return jsonify({"message": "Role deletada com sucesso"}), 200
        except ValueError as e:
            return jsonify({"error": str(e)}), 404

    def get_roles_by_event(self, event_id: int) -> tuple[Response, int]:
        """Retorna as roles associadas a um evento específico"""
        try:
            roles = self.service.get_roles_by_event(event_id)
            return jsonify(roles), 200
        except ValueError as e:
            return jsonify({"error": str(e)}), 400
