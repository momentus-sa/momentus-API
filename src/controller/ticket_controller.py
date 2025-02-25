"""Módulo destinado ao controller dos ingressos"""
from flask import request, jsonify, Response
from src.services.ticket_services import TicketServices

class TicketController(object):
    """Classe que representa o controller dos ingressos"""

    def __init__(self):
        self.service = TicketServices()

    def create_ticket(self) -> tuple[Response, int]:
        """Serviço que cria um novo ingresso"""
        if not request.is_json:
            return jsonify({"error": "O corpo da requisição deve estar no formato JSON"}), 400

        data = request.get_json()

        try:
            ticket = self.service.create_ticket(data)
            return jsonify(ticket), 201

        except ValueError as e:
            return jsonify({"error": str(e)}), 400

    def get_ticket_by_id(self, ticket_id: int) -> tuple[Response, int]:
        """Retorna o ingresso com o ID especificado"""
        try:
            ticket = self.service.get_ticket_by_id(ticket_id)
            return jsonify(ticket), 200
        except ValueError as e:
            return jsonify({"error": str(e)}), 404

    def update_ticket(self, ticket_id: int) -> tuple[Response, int]:
        """Atualiza os dados do ingresso com o ID especificado"""
        if not request.is_json:
            return jsonify({"error": "O corpo da requisição deve estar no formato JSON"}), 400

        data = request.get_json()

        try:
            updated_ticket = self.service.update_ticket(ticket_id, data)
            return jsonify(updated_ticket), 202

        except ValueError as e:
            return jsonify({"error": str(e)}), 400

    def delete_ticket(self, ticket_id: int) -> tuple[Response, int]:
        """Deleta o ingresso com o ID especificado"""
        try:
            self.service.delete_ticket(ticket_id)
            return jsonify({"message": "Ingresso deletado com sucesso"}), 200
        except ValueError as e:
            return jsonify({"error": str(e)}), 404

    def sell_ticket(self, ticket_id: int) -> tuple[Response, int]:
        """Realiza a venda de ingressos"""
        if not request.is_json:
            return jsonify({"error": "O corpo da requisição deve estar no formato JSON"}), 400

        data = request.get_json()

        try:
            quantity = data.get("quantity")
            if quantity is None or quantity <= 0:
                return jsonify({"error": "A quantidade deve ser um número positivo."}), 400

            updated_ticket = self.service.sell_ticket(ticket_id, quantity)
            return jsonify(updated_ticket), 200

        except ValueError as e:
            return jsonify({"error": str(e)}), 400

    def get_available_tickets(self, event_id: int) -> tuple[Response, int]:
        """Retorna os ingressos disponíveis para um evento específico"""
        try:
            available_tickets = self.service.get_available_tickets(event_id)
            return jsonify(available_tickets), 200
        except ValueError as e:
            return jsonify({"error": str(e)}), 400
