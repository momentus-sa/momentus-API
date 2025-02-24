"""Módulo para gerenciar os serviços de usuário"""
# from datetime import datetime, timezone
from flask_jwt_extended import create_access_token
from marshmallow import ValidationError
from src.models.user import User
from src.schemas.user_schema import UserSchema
from src.repositories.user_repository import UserRepository

class UserServices:
    """Classe que encapsula a lógica de negócios relacionada a usuários."""

    # verificar se o email é válido
    # senha válida

    def __init__(self):
        self.user_schema = UserSchema()
        self.user_repository = UserRepository()

    def login(self, email: str, password: str) -> str:
        """Verifica credenciais do usuário e retorna um token JWT"""

        if not email:
            raise ValueError("Email is not provided", 400)

        if not password:
            raise ValueError("Password is not provided", 400)

        user = self.user_repository.find_by_email(email)

        if not user:
            raise ValueError(f"User {email} doesn't exist", 400)

        if not user.check_password(password):
            raise ValueError("Incorrect password", 401)

        access_token = create_access_token(identity=user.user_id)

        return access_token


    def create_user(self, data: dict) -> User:
        """Valida os dados para a criação de um usuário"""
        try:
            user_data = self.user_schema.load(data)

        except ValidationError as e:
            raise ValueError(f"Erro de validação: {e.messages}") from e

        self._validate_unique_user_fields(user_data)

        return self.user_repository.create(**user_data)

    def _validate_unique_user_fields(self, user_data):
        """Função que valida se a condição de unicidade dos campos do usuário são satisfeitas"""

        user_name = user_data["name"]
        user_email = user_data["email"]

        if self.user_repository.find_by_name(user_name):
            raise ValueError("Erro de validação: Já existe um usuário com o nome especificado")

        if self.user_repository.find_by_email(user_email):
            raise ValueError("Erro de validação: Já existe um usuário com o email especificado")


    def get_all_users(self):
        """Retorna todos os usuários"""
        users = self.user_repository.get_all_users()

        return [user.to_dict() for user in users]

    def get_user_by_email(self, user_email):
        """Retorna o usuário com o email especificado"""
        user = self.user_repository.find_by_email(user_email)

        user_dict = user.to_dict()
        user_dict.pop('password_hash', None)

        return user_dict()

    def get_user_by_id(self, user_id):
        """Retorna o usuário com o id especificado"""
        user = self.user_repository.find_by_id(user_id)

        return user.to_dict()

    def update_user(self, user_id:str, updated_data:dict)-> User:
        """Atualiza os dados do usuário com base no dicionário especificado"""
        user = self.user_repository.find_by_id(user_id)
        
        if not user:
            return False

        updated_user = self.user_repository.update(user_id, **updated_data)

        if not updated_user:
            raise ValueError("Falha ao atualizar o usuário")

        return updated_user.to_dict()
