"""Módulo destinado ao controller de usuário"""
from flask import request, jsonify

from src.services.users_services import UserServices

class UserController(object):
    """Classe que representa o controller de um usuário"""
    def __init__(self):
        self.service = UserServices()

    def create_user(self)-> tuple[dict, int]:
        """Serviço que cria um usuário"""
        if not request.is_json:
            return jsonify({"error": "The body must be a JSON"}), 400

        data = request.get_json()

        try:
            user = self.service.create_user(data)

            user_dict = user.to_dict()
            user_dict.pop('password_hash', None)

            return jsonify(user_dict), 201

        except ValueError as e:
            return jsonify({"error": str(e)}), 400
