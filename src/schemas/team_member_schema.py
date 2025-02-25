"""Módulo que define o esquema de membros do time e o valida"""
from marshmallow import Schema, fields, validate

class TeamMemberSchema(Schema):
    """Schema para validação e serialização do TeamMember"""

    id = fields.Int(dump_only=True)
    person_name = fields.Str(required=True, validate=validate.Length(min=3, max=100))
    event_id = fields.Int(required=True)
    roles = fields.List(fields.Str(), required=True)

class TeamMemberUpdateSchema(Schema):
    """Schema para atualização de dados do TeamMember"""

    person_name = fields.Str(validate=validate.Length(min=1, max=100))
    event_id = fields.Int()
    roles = fields.List(fields.Str())
