"""Módulo que define o esquema de tarefas de membros e o valida"""
from marshmallow import Schema, fields, validate

class TaskSchema(Schema):
    """Esquema de validação para roles"""

    task_id = fields.Int(dump_only=True)
    name = fields.Str(required=True, validate=validate.Length(min=3, max=50))
    description = fields.Str(required=True, validate=validate.Length(min=5, max=200))
    event_id = fields.Int(required=True)
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)

class TaskUpdateSchema(TaskSchema):
    """Esquema de validação para atualização de roles"""

    name = fields.Str(required=False, validate=validate.Length(min=3, max=50))
    description = fields.Str(required=False, validate=validate.Length(min=5, max=200))
    event_id = fields.Int(required=False)
