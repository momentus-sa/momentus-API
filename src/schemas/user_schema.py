"""Módulo que define o esquema de usuários e o valida"""
from marshmallow import Schema, fields, validate

#Con(c/s)ertar essas validações
class UserSchema(Schema):
    """Esquema de validação do usuário"""
    user_id = fields.Int(dump_only = True)
    name = fields.Str(required=True, validate=validate.Length(min=3, max=50))
    email = fields.Email(required=True)
    password = fields.Str(load_only=True, required=True, validate=validate.Length(min=8))
    user_type = fields.Str(validate=validate.OneOf(["manager", "client"]), required=True)
    birth_date = fields.Date(required=True)
    profile_image_url = fields.Str(max=255)

class UserUpdateSchema(Schema):
    """Esquema de validação para atualização de usuário"""
    user_id = fields.Int(dump_only=True)
    name = fields.Str(validate=validate.Length(min=3, max=50))
    email = fields.Email()
    password = fields.Str(load_only=True, validate=validate.Length(min=8))
    user_type = fields.Str(validate=validate.OneOf(["manager", "client"]))
    birth_date = fields.Date()
    profile_image_url = fields.Str(validate=validate.Length(max=255))