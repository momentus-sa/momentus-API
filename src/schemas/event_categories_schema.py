"""Módulo que define o esquema de categorias de eventos e o valida"""
from marshmallow import Schema, fields, validate, pre_load

#Con(c/s)ertar essas validações
class EventCategorySchema(Schema):
    """Esquema de validação do usuário"""
    id = fields.Int(dump_only = True)
    name = fields.Str(required=True, validate=validate.Length(min=3, max=50))
    is_default = fields.Bool(default=True)
