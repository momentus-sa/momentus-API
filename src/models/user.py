""" Módulo destinado a definção do usuário no banco de dados"""
import uuid
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.dialects.postgresql import UUID
from src.extensions import db


class User(db.Model):
    """Classe que define os atributos do usuário no banco de dados"""
    __tablename__ = 'users'

    user_id = db.Column(UUID(as_uuid=True), primary_key=True, nullable=False, default=uuid.uuid4)
    name = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(70), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)
    birth_date = db.Column(db.Date)
    profile_image_url = db.Column(db.String(255))
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)
    user_type = db.Column(db.Enum('manager', 'client', name='user_type'), nullable=False)

    def to_dict(self) -> dict:
        """Retorna o objeto User na forma de um dicionário"""
        return {
            "user_id": self.user_id,
            "name": self.name,
            "email": self.email,
            "birth_date": self.birth_date,
            "profile_image_url": self.profile_image_url,
            "user_type": self.user_type,
            "created_at": self.created_at.strftime("%d/%m/%Y %H:%M"),
            "updated_at": self.updated_at.strftime("%d/%m/%Y %H:%M"),
        }


    def to_dict_with_password(self):
        """Returno o objeto User na forma de dicinonário (com senha)"""
        return {
            "user_id": self.user_id,
            "name": self.name,
            "email": self.email,
            "password_hash": self.password_hash,
            "birth_date": self.birth_date,
            "profile_image_url": self.profile_image_url,
            "user_type": self.user_type,
            "created_at": self.created_at.strftime("%d/%m/%Y %H:%M"),
            "updated_at": self.updated_at.strftime("%d/%m/%Y %H:%M"),
        }

    def set_password(self, password):
        """Salva o hash da senha especificada como senha do usuário"""
        self.password_hash = generate_password_hash(password)

    def check_password(self, password) ->bool:
        """"Checa se o hash da senha do usuário e a senha fornecida são os mesmos"""
        return check_password_hash(self.password_hash, password)
