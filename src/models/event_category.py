"""" Módulo destinado a definção das categorias de evento no banco de dados """
from src.extensions import db


class EventCategory(db.Model):
    """Classe que define os atributos das categorias de evento no banco de dados"""
    __tablename__ = 'Event_categories'
    event_category_id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True, unique=True)
    name = db.Column(db.String(30), unique=True, nullable=False)
    is_default = db.Column(db.Boolean, nullable=False, default=True)

    def to_dict(self):
        """Retorna um dicionário com todas as colunas da classe categoria"""
        return {
            "event_category_id": self.event_category_id,
            "name": self.name,
            "is_default": self.is_default
        }
