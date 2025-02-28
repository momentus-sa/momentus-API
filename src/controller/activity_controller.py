"""Módulo destinado ao controller das atividades"""
from flask import request, jsonify, Response
from src.services.activity_services import ActivityServices
from datetime import timedelta

class ActivityController:
    """Classe que representa o controller das atividades"""

    def __init__(self):
        self.service = ActivityServices()

    def create_activity(self) -> tuple[Response, int]:
        """Cria uma nova atividade"""
        if not request.is_json:
            return jsonify({"error": "O corpo da requisição deve estar no formato JSON"}), 400

        data = request.get_json()

        try:
            activity = self.service.create_activity(data)
            return jsonify(activity), 201
        except ValidationError as e:
            return jsonify({"error": "Erro de validação", "details": e.messages}), 400
        except ValueError as e:
            return jsonify({"error": str(e)}), 400

    def get_activity_by_id(self, activity_id: int) -> tuple[Response, int]:
        """Retorna a atividade com o ID especificado"""
        try:
            activity = self.service.get_activity_by_id(activity_id)
            return jsonify(activity), 200
        except ValueError as e:
            return jsonify({"error": str(e)}), 404

    def get_all_by_event(self, event_id):
        """Retorna todas as atividades do evento com o ID especificado"""
        try:
            activities = self.service.get_all_by_event(event_id)
            return jsonify(activities), 200
        except ValueError as e:
            return jsonify({"error": str(e)}), 400

    def update_activity(self, activity_id: int) -> tuple[Response, int]:
        """Atualiza os dados da atividade com o ID especificado"""
        if not request.is_json:
            return jsonify({"error": "O corpo da requisição deve estar no formato JSON"}), 400

        data = request.get_json()

        try:
            updated_activity = self.service.update_activity(activity_id, data)
            return jsonify(updated_activity), 202
        except ValueError as e:
            return jsonify({"error": str(e)}), 400

    def delete_activity(self, activity_id: int) -> tuple[Response, int]:
        """Deleta a atividade com o ID especificado"""
        try:
            self.service.delete_activity(activity_id)
            return jsonify({"message": "Atividade deletada com sucesso"}), 200

        except ValueError as e:
            return jsonify({"error": str(e)}), 404

    def get_upcoming_activities(self, event_id) -> tuple[Response, int]:
        """Retorna todas as atividades futuras"""
        time_window_str = request.args.get("time_window", "7")  # Pega da URL, padrão 7 dias
        
        try:
            time_window = timedelta(days=int(time_window_str))  # Converte para inteiro
            activities = self.service.get_upcoming_activities(event_id, time_window)
            return jsonify(activities), 200
        except (ValueError, TypeError) as e:
            return jsonify({"error": f"Parâmetro 'time_window' inválido: {str(e)}"}), 400
