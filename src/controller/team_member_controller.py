"""Módulo destinado ao controller dos membros de time"""
from flask import request, jsonify, Response
from src.services.team_member_services import TeamMemberServices

class TeamMemberController(object):
    """Classe que representa o controller dos membros de time"""

    def __init__(self):
        self.service = TeamMemberServices()

    def create_member(self) -> tuple[Response, int]:
        """Serviço que cria um novo membro"""
        if not request.is_json:
            return jsonify({"error": "O corpo da requisição deve estar no formato JSON"}), 400

        data = request.get_json()

        try:
            member = self.service.create_member(data)
            return jsonify(member), 201

        except ValueError as e:
            return jsonify({"error": str(e)}), 400

    def get_member_by_id(self, member_id: int) -> tuple[Response, int]:
        """Retorna o membro com o ID especificado"""
        try:
            member = self.service.get_member_by_id(member_id)
            return jsonify(member), 200
        except ValueError as e:
            return jsonify({"error": str(e)}), 404

    def get_members_by_event(self, event_id: int) -> tuple[Response, int]:
        """Retorna os membros associados a um evento específico"""
        try:
            members = self.service.get_members_by_event(event_id)
            return jsonify(members), 200
        except ValueError as e:
            return jsonify({"error": str(e)}), 400

    def update_member(self, member_id: int) -> tuple[Response, int]:
        """Atualiza os dados do membro com o ID especificado"""
        if not request.is_json:
            return jsonify({"error": "O corpo da requisição deve estar no formato JSON"}), 400

        data = request.get_json()

        try:
            updated_member = self.service.update_member(member_id, data)
            return jsonify(updated_member), 202

        except ValueError as e:
            return jsonify({"error": str(e)}), 400

    def delete_member(self, member_id: int) -> tuple[Response, int]:
        """Deleta o membro com o ID especificado"""
        try:
            self.service.delete_member(member_id)
            return jsonify({"message": "Membro deletado com sucesso"}), 200
        except ValueError as e:
            return jsonify({"error": str(e)}), 404
