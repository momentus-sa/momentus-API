"""Módulo que define o esquema de atividades e sua validação"""
from marshmallow import Schema, fields, validate

class ActivitySchema(Schema):
    """Esquema de validação para atividades"""

    event_id = fields.Int(required=True)
    activity_id = fields.Int(dump_only=True)
    name = fields.Str(required=True, validate=validate.Length(min=3, max=100))
    description = fields.Str(required=False, validate=validate.Length(max=500))
    activity_time = fields.DateTime(required=True)

    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)


class ActivityUpdateSchema(ActivitySchema):
    """Esquema de validação para atualização de atividades"""

    event_id = fields.Int(required=True, dump_only= True)
    activity_id = fields.Int(dump_only=True)
    name = fields.Str(required=False, validate=validate.Length(min=3, max=100))
    description = fields.Str(required=False, validate=validate.Length(max=500))
    activity_time = fields.DateTime(required=False)

    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)
