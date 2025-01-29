"""Módulo para criar os usuários"""
from datetime import datetime, timezone
from werkzeug.security import generate_password_hash
from marshmallow import ValidationError
from src.models.user import User
from src.schemas.user_schema import UserSchema
from src.repositories.user_repository import UserRepository
from src.extensions import db



class UserServices:
    """Classe que encapsula a lógica de negócios relacionada a usuários."""

    #verificar se o email é válido
    #senha válida
    #email único
    #nome único
    
    def __init__(self):
        self.user_schema = UserSchema()
        self.user_repository = UserRepository()

    def create_user(self, data: dict):
        """ Valida os dados para a criação de um usuário"""
        try:
            user_data = self.user_schema.load(data)
            return self.user_repository.create(**user_data)

        except ValidationError as e:
            raise ValueError(f"Erro de validação: {e.messages}") from e
