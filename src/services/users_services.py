"""Módulo para criar os usuários"""
from datetime import datetime, timezone
from werkzeug.security import generate_password_hash
from marshmallow import ValidationError
from src.models.user import User
from src.schemas.user_schema import UserSchema
from src.repositories.user_repository import UserRepository

#regas de negócio (nao criar o mesmo usuário 2 vezes), sao no services

class UserServices:
    """Classe que encapsula a lógica de negócios relacionada a usuários."""

    # verificar se o email é válido
    # senha válida
    # email único
    # nome único
    # validar as buscas e etc

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

    def get_all_users(self):
        """Retorna todos os usuários"""
        users = self.user_repository.get_all_users()

        return [user.to_dict() for user in users]

    def get_user_by_email(self, user_email):
        """Retorna o usuário com o email especificado"""
        user = self.user_repository.find_by_email(user_email)

        user_dict = user.to_dict()
        user_dict.pop('password_hash', None)

        return user_dict

    def get_user_by_id(self, user_id):
        """Retorna o usuário com o id especificado"""
        user = self.user_repository.find_by_id(user_id)

        return user.to_dict()

    def update_user(self, user_id:str, updated_data:dict)-> User:
        #Tem que validar né pae
        """Atualiza os dados do usuário com base no dicionário especificado"""
        user = self.user_repository.find_by_id(user_id)
        if not user:
            raise ValueError("Usuário não encontrado")

        updated_user = self.user_repository.update(user_id, **updated_data)

        if not updated_user:
            raise ValueError("Falha ao atualizar o usuário")

        return updated_user.to_dict()
