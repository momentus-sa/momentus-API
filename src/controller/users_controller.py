"""Módulo destinado ao controller de usuário"""
from flask import request, jsonify, Response
from src.services.users_services import UserServices

# estudar padrões de codigo de resposta
# regras sobre o dado (a string obtida), sao no controller

class UserController(object):
    """Classe que representa o controller de um usuário"""

    def __init__(self):
        self.service = UserServices()


    def login(self) -> tuple[Response, int]:
        """Autentica o usuário e gera um token JWT"""
        if not request.is_json:
            return jsonify({"error": "O corpo da requisição deve estar no formato JSON"}), 400

        data = request.get_json()
        email = data.get("email")
        password = data.get("password")

        try:
            access_token = self.service.login(email, password)

            return jsonify({"access_token": access_token}), 200

        except ValueError as e:
            return jsonify({"error": str(e)}), 400

    def create_user(self) -> tuple[Response, int]:
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

    def get_all_users(self) -> list[Response, int]:
        """Retorna todos os usuários do banco de dados"""
        try:
            users = self.service.get_all_users()
            return jsonify(users), 200
        except ValueError as e:
            return jsonify({"error": str(e)}), 400

    def get_user_by_id(self, user_id) -> tuple[Response, int]:
        """Retorna o usuário com o id especificado"""
        try:
            user = self.service.get_user_by_id(user_id)
            return jsonify(user), 200
        except ValueError as e:
            return jsonify({"error": str(e)}), 400

    def get_user_by_email(self, user_email: str) -> tuple[Response, int]:
        """Retorna o usuário com o email especificado"""

        try:
            user = self.service.get_user_by_email(user_email)
            return jsonify(user), 200
        except ValueError as e:
            return jsonify({"error": str(e)}), 400

    def update_user(self, user_id) -> tuple[Response, int]:
        """Atualiza os dados do usuário com o id especificado"""
        data = request.get_json()

        if not request.is_json:
            return jsonify({"error": "O corpo da requisição deve estar no formato JSON"}), 400

        try:
            user = self.service.update_user(user_id, data)

            if not user:
                return jsonify({"message": "Usuário não encontrado"}), 404

            return jsonify(user), 202
        except ValueError as e:
            return jsonify({"error": str(e)}), 400
