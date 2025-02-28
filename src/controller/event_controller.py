"""Módulo destinado ao controller dos eventos"""
from flask import request, jsonify, Response
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

    def update_event(self, event_id: int) -> tuple[Response, int]:
        """Atualiza os dados do evento com o ID especificado"""
        if not request.is_json:
            return jsonify({"error": "O corpo da requisição deve estar no formato JSON"}), 400

        data = request.get_json()

        try:
            updated_event = self.service.update_event(event_id, data)
            return jsonify(updated_event), 202

        except ValueError as e:
            return jsonify({"error": str(e)}), 400

    def deactivate_event(self, event_id: int) -> tuple[Response, int]:
        """Desativa o evento com o ID especificado"""
        try:
            deactivated_event = self.service.deactivate_event(event_id)
            return jsonify(deactivated_event), 200
        except ValueError as e:
            return jsonify({"error": str(e)}), 404

    def delete_event(self, event_id: int) -> tuple[Response, int]:
        """Deleta o evento com o ID especificado"""
        try:
            self.service.delete_event(event_id)
            return jsonify({"message": "Evento deletado com sucesso"}), 200
        except ValueError as e:
            return jsonify({"error": str(e)}), 404
