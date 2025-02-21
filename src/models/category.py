from sqlalchemy.dialects.postgresql import UUID
from src.extensions import db

class Category(db.Model):
    """Classe que define os atributos das categorias de evento no bacno de dados"""
    __tablename__ = 'Categories'
    id = db.Column(primary_key= True, nullable = False)
    name = db.Column(db.String(30), unique = True, nullable = False)
