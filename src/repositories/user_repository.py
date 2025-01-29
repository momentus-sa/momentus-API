"""Módulo do repositório usuário, que cria uma camada intermediária entre o banco de dados do usuário e o sistema"""
from uuid import uuid4 as uuid
from datetime import datetime
from werkzeug.security import generate_password_hash
from src.models.user import User
from src.extensions import db


class UserRepository:
    """Classe que interliga o banco de dados do usuário e o sistema"""

    def create(self, name: str, email: str, password: str, birth_date: str, profile_image_url: str = None, user_type='client') -> User:
        """Cria um novo usuário no banco de dados"""
        user = User(
            id=str(uuid()),
            name=name,
            email=email,
            password_hash=generate_password_hash(password),
            birth_date=birth_date,
            profile_image_url=profile_image_url,
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow(),
            user_type=user_type
        )

        db.session.add(user)
        db.session.commit()

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
        """
        Retorna um usuário que possui o id especificado no parâmetro |
        caso não encontre nenhum usuário com o id especificado, retorna False
        """
        user = User.query.filter_by(id=user_id)
        if user is None:
            return False

        return user

    def delete(self, user_id: str) -> bool:
        """Deleta o usuário com o id especificado"""
        user = self.find_by_id(user_id)
        if not user:
            return False

        db.session.delete(user)
        db.session.commit()

        return True

    def update(self, user_id: str, **kwargs) -> bool:
        """Altera os atributos do usuário com base nos atributos fornecidos"""
        user = self.find_by_id(user_id)
        if not user:
            return False

        for key, value in kwargs.items():
            if hasattr(user, key):
                if key == "password":
                    value = generate_password_hash(value)
                    key = "password_hash"

            setattr(user, key, value)

        user.updated_at = datetime.utcnow()
        db.session.commit()

        return user
