""" Módulo destinado a definção do usuário no banco de dados"""
import uuid
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
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
    user_type = db.Column(db.Enum('manager', 'client', name='user_type'), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relacionamento 1xN com Event
    events = db.relationship("Event", back_populates="event_creator", cascade="all, delete-orphan")

    def to_dict(self) -> dict:
        """Retorna o objeto User na forma de um dicionário"""
        return {
            "user_id": str(self.user_id),
            "name": self.name,
            "email": self.email,
            "birth_date": self.birth_date.strftime("%Y-%m-%d") if self.birth_date else None,
            "profile_image_url": self.profile_image_url,
            "user_type": self.user_type,
            "created_at": self.created_at.strftime("%d/%m/%Y %H:%M"),
            "updated_at": self.updated_at.strftime("%d/%m/%Y %H:%M"),
        }

    def set_password(self, password: str) -> None:
        """Gera o hash da senha e armazena no campo password_hash"""
        self.password_hash = generate_password_hash(password)

    def check_password(self, password: str) -> bool:
        """Verifica se a senha fornecida confere com o hash armazenado"""
        return check_password_hash(self.password_hash, password)
    