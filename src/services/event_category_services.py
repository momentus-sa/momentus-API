"""""Módulo para gerenciar os serviços de categorias de evento"""""
from marshmallow import ValidationError
from src.schemas.event_categories_schema import EventCategorySchema
from src.models.event_category import EventCategory
from src.repositories.event_category_repository import EventCategoryRepository

class EventCategoryServices():
    """Classe que encapsula a lógica de negócios relacionada a categoria de eventos."""
    def __init__(self):
        self.event_category_repository = EventCategoryRepository()
        self.category_schema = EventCategorySchema()

    #nao permitir que o usuário crie categorias default

    def create_category(self, data:dict)->EventCategory:
        """Valida a lógica de criação de usuário"""
        try:
            event_category_data = self.category_schema.load(data)

        except ValidationError as e:
            raise ValueError(f"Erro de validação: {e.messages}") from e

        category_name = event_category_data["name"]
        self._validate_unique_default_category(category_name)

        return self.event_category_repository.create(**event_category_data).to_dict()


    def _validate_unique_default_category(self, category_name):
        """Verifica se não existe outra categoria com o mesmo nome marcada como padrão"""
        existing_category = self.event_category_repository.get_category_by_name(category_name)

        if existing_category and existing_category.is_default:
            raise ValueError(f"Já existe uma categoria padrão com o nome '{category_name}'.")

    def get_all_categories(self):
        """Retorna todas as categorias de evento"""
        event_categories = EventCategory.query.all()

        if not event_categories:
            raise ValueError("Nenhuma categoria de evento encontrada")

        return [event_category.to_dict() for event_category in event_categories]

    def get_all_default_categories(self):
        """Retorna todas as categorias padrão ou falso se não encontrar nenhuma"""

        event_categories = self.event_category_repository.get_all_default_categories()

        if event_categories is False:
            return False

        return [event_category.to_dict() for event_category in event_categories]

    def get_category_by_name(self, name:str)->EventCategory:
        """Retorna uma categoria que possua o nome especificado no parâmetro |
        caso não encontre nenhuma categoria com o nome especificado, retorna False"""

        event_category = self.event_category_repository.get_category_by_name(name)

        if event_category is False:
            return False

        return event_category.to_dict()
