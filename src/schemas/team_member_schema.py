"""Módulo que define o esquema de membros do time e o valida"""
from marshmallow import Schema, fields, validate

class TeamMemberSchema(Schema):
    """Schema para validação e serialização do TeamMember"""

    team_member_id = fields.Int(dump_only=True)
    member_name = fields.Str(required=True, validate=validate.Length(min=3, max=100))
    role = fields.Str(required= True, validate=validate.Length(min=2, max=50))
    event_id = fields.Int(required=True)
    task = fields.List(fields.Str(), required=False)

class TeamMemberUpdateSchema(Schema):
    """Schema para atualização de dados do TeamMember"""

    member_name = fields.Str(validate=validate.Length(min=1, max=100))
    event_id = fields.Int()
    tasks = fields.List(fields.Str())
    role = fields.Str(required= False)
