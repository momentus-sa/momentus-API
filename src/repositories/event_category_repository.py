"""Módulo de camada intermediária entre o banco de dados das categorias de evento e o sistema"""
from src.models.event_category import EventCategory
from src.extensions import db

# Validação de nao poder criar uma categoria que seja default

class EventCategoryRepository():
    """Classe interliga o banco de dados das categorias de evento e o sistema"""

    def create(self, name: str, is_default: bool = True):
        """Cria um novo usuário no banco de dados e retorna o usuário criado"""
        new_category = EventCategory(
            name=name,
            is_default=is_default
        )

        db.session.add(new_category)
        db.session.commit()

        return new_category

    def get_all_categories(self):
        """Retorna todas as categorias de eventos"""
        return EventCategory.query.all()

    def get_all_default_categories(self)->list[EventCategory]:
        """Retorna todas as categorias padrão |
        caso não encontre nenhuma, retorna falso"""

        event_categories = EventCategory.query.filter_by(is_default= True).all()

        if event_categories is None:
            return False

        return event_categories

    def get_category_by_name(self, category_name: str) -> EventCategory:
        """"Retorna uma categoria que possua o nome especificado no parâmetro |
        caso não encontre nenhuma categoria com o nome especificado, retorna False"""

        event_category = EventCategory.query.filter_by(name=category_name).first()

        if event_category is None:
            return False

        return event_category
