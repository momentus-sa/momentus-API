"""Módulo destinado ao controller dos eventos"""
from flask import request, jsonify, Response
from flask_jwt_extended import get_jwt_identity
from uuid import UUID
from src.services.event_services import EventServices

class EventController(object):
    """Classe que representa o controller dos eventos"""

    def __init__(self):
        self.service = EventServices()

    def create_event(self) -> tuple[Response, int]:
        """Serviço que cria um novo evento"""
        if not request.is_json:
            return jsonify({"error": "O corpo da requisição deve estar no formato JSON"}), 400

        data = request.get_json()

        user_id = get_jwt_identity()
        data['event_creator_id'] = user_id

        try:
            event = self.service.create_event(data)
            return jsonify(event), 201

        except ValueError as e:
            return jsonify({"error": str(e)}), 400

    def get_event_by_id(self, event_id: int) -> tuple[Response, int]:
        """Retorna o evento com o ID especificado"""
        try:
            event = self.service.get_event_by_id(event_id)
            return jsonify(event), 200
        except ValueError as e:
            return jsonify({"error": str(e)}), 404

    def get_all_events(self) -> tuple[Response, int]:
        """Retorna todos os eventos registrados"""
        try:
            events = self.service.get_all_events()
            return jsonify(events), 200
        except ValueError as e:
            return jsonify({"error": str(e)}), 400

    def get_upcoming_events(self) -> tuple[Response, int]:
        """Retorna todos os eventos que ainda não aconteceram"""
        try:
            upcoming_events = self.service.get_upcoming_events()
            return jsonify(upcoming_events), 200
        except ValueError as e:
            return jsonify({"error": str(e)}), 400

    def get_all_user_events(self, user_id) -> tuple[Response, int]:
        """Retorna todos os eventos do usuário"""

        try:
            events = self.service.get_all_user_events(user_id)
            return jsonify(events), 200
        except ValueError as e:
            return jsonify({"error": str(e)}), 400

    def get_events_by_category(self, category_id: int) -> tuple[Response, int]:
        """Retorna todos os eventos associados à categoria especificada."""

        try:
            events = self.service.get_events_by_category(category_id)

            if not events:
                return jsonify({"message": "Nenhum evento encontrado para esta categoria"}), 404

            return jsonify({"events": events}), 200

        except ValueError as e:
            return jsonify({"error": str(e)}), 400

    def update_event(self, event_id: int) -> tuple[Response, int]:
        """Atualiza os dados do evento com o ID especificado"""
        if not request.is_json:
            return jsonify({"error": "O corpo da requisição deve estar no formato JSON"}), 400

        data = request.get_json()

        user_id = get_jwt_identity()
        try:
            user_id = UUID(user_id)  # Converte para UUID
        except ValueError:
            return jsonify({"error": "ID de usuário inválido"}), 400

        try:
            updated_event = self.service.update_event(event_id, data, user_id=user_id)
            return jsonify(updated_event), 202

        except ValueError as e:
            return jsonify({"error": str(e)}), 400

    def delete_event(self, event_id: int) -> tuple[Response, int]:
        """Deleta o evento com o ID especificado"""
        user_id = get_jwt_identity()
        try:
            user_id = UUID(user_id)
        except ValueError:
            return jsonify({"error": "ID de usuário inválido"}), 400

        try:
            return self.service.delete_event(event_id, user_id)
        except ValueError as e:
            return jsonify({"error": str(e)}), 404
