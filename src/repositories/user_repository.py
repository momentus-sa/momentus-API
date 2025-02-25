"""Módulo que cria uma camada intermediária entre o banco de dados do usuário e o sistema"""
from datetime import datetime
from werkzeug.security import generate_password_hash
from src.models.user import User
from src.extensions import db


class UserRepository():
    """Classe que interliga o banco de dados do usuário e o sistema"""

    #definit o created_at como default no model
    def create(self, name: str, email: str, password: str, birth_date: str, profile_image_url: str = None, user_type='client') -> User:
        """Cria um novo usuário no banco de dados"""
        user = User(
            name=name,
            email=email,
            birth_date=birth_date,
            profile_image_url=profile_image_url,
            user_type=user_type
        )

        user.set_password(password)

        db.session.add(user)
        db.session.commit()

        return user

    def get_all_users(self):
        """Retorna todos os usuários"""
        return User.query.all()

    def find_by_name(self, name: str) ->  User:
        """Retorna um usuário que possui o nome especificado no parâmetro |
        caso não encontre nenhum usuário com o nome especificado, retorna False"""
        user = User.query.filter_by(name = name).first()

        if user is None:
            return False

        return user

    def find_by_email(self, email: str) -> User:
        """
        Retorna um usuário que possui o email especificado no parâmetro |
        caso não encontre nenhum usuário com o email especificado, retorna False
        """
        user = User.query.filter_by(email=email).first()

        if user is None:
            return False

        return user

    def find_by_id(self, user_id: str) -> User:
        """Retorna um usuário que possui o id especificado no parâmetro |
        caso não encontre nenhum usuário com o id especificado, retorna None"""
        user = User.query.filter_by(user_id=user_id).first()
        if user is None:
            return None

        return user

    def update(self, user_id: str, **kwargs) -> User:
        """Altera os atributos do usuário com base nos atributos fornecidos |
        Caso nao encontre nenhum usuário com o id especificado, retorna False"""
        user = self.find_by_id(user_id)
        if not user:
            return False

        for key, value in kwargs.items():
            if hasattr(user, key):
                if key == "password":
                    value = user.set_password(user)
                    key = "password_hash"

            setattr(user, key, value)

        db.session.commit()

        return user

    def delete(self, user_id: str) -> bool:
        """Deleta o usuário com o id especificado e retorna o usuário deletado |
        Caso nao encontre nenhum usuário com o id especificado, retorna False"""
        user = self.find_by_id(user_id)
        if not user:
            return False

        db.session.delete(user)
        db.session.commit()

        return True
