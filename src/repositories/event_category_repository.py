"""Módulo de camada intermediária entre o banco de dados das categorias de evento e o sistema"""
from src.models.event_category import EventCategory
from src.repositories.event_repository import EventRepository
from src.extensions import db

# Validação de nao poder criar uma categoria que seja default

class EventCategoryRepository():
    """Classe interliga o banco de dados das categorias de evento e o sistema"""

    def __init__(self):
        self.event_repository = EventRepository()

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

    def get_category_by_id(self, category_id: int) -> EventCategory:
        """Retorna a categoria de evento com o ID especificado, ou None se não encontrar."""
        return EventCategory.query.filter_by(event_category_id=category_id).first()

    def get_category_by_name(self, category_name: str) -> EventCategory:
        """"Retorna uma categoria que possua o nome especificado no parâmetro |
        caso não encontre nenhuma categoria com o nome especificado, retorna False"""

        event_category = EventCategory.query.filter_by(name=category_name).first()

        if event_category is None:
            return False

        return event_category
    def get_category_by_name_and_event(self, category_name: str, event_id: int):
        """Retorna a categoria do evento se o nome corresponder."""

        event = self.event_repository.get_by_id(event_id)

        if not event or not event.category:
            return None

        return event.category if event.category.name == category_name else None

    def delete_category(self, event_category_id: int):
        """Deleta uma categoria de evento pelo ID, não permitindo deletar categorias padrão"""
        event_category = EventCategory.query.get(event_category_id)

        db.session.delete(event_category)
        db.session.commit()

        return event_category
