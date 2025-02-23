""""Módulo destinado ao controller das categorias de eventos"""
from flask import request, Response, jsonify
from src.services.event_category_services import EventCategoryServices

# melhorar os comentários
# No controler sao formatadas as respostas

class EventCategoryController(object):
    """Classe responsável por gerenciar as requisições relacionadas às categorias de eventos."""

    def __init__(self):
        self.service = EventCategoryServices()

    def create_event_category(self) -> tuple[Response, int]:
        """"Cria uma nova categoria de evento"""
        if not request.is_json:
            return jsonify({"error": "The body must be a JSON"}), 400

        data = request.get_json()

        try:
            event_category = self.service.create_category(data)

            return jsonify(event_category), 201

        except ValueError as e:
            return jsonify({"Error": str(e)}), 400

    def get_all_event_categories(self) -> tuple[Response, int]:
        """Retorna todas as categorias de evento"""

        try:
            event_categories = self.service.get_all_categories()

            if not event_categories:
                return jsonify({"message": "Nenhuma categoria encontrada"}), 404

            return jsonify(event_categories), 200

        except ValueError as e:
            return jsonify({"Error": str(e)}), 400

    def get_all_default_event_categories(self) -> tuple[Response, int]:
        """Retorna todas as categorias de evento padrão"""

        try:
            event_default_categories = self.service.get_all_default_categories()

            if not event_default_categories:
                return jsonify({"message": "Nenhuma categoria padrão encontrada"}), 404

            return jsonify(event_default_categories), 200

        except ValueError as e:
            return jsonify({"Error": str(e)}), 400

    def get_event_category_by_name(self, category_name) -> tuple[Response, int]:
        """Retorna uma categoria que possua o nome especificado"""

        try:
            event_category = self.service.get_category_by_name(category_name)

            if not event_category:
                return jsonify({"message": "Nenhuma categoria encontrada com o nome especificado"}), 404

            return jsonify(event_category), 200
 
        except ValueError as e:
            return jsonify({"error": str(e)}), 400
