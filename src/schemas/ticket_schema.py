"""Módulo que define o esquema de ingressos e o valida"""
from marshmallow import Schema, fields, validate, ValidationError

def validate_positive(value):
    """Valida se o valor é positivo"""
    if value <= 0:
        raise ValidationError("O valor deve ser positivo.")

class TicketSchema(Schema):
    """Esquema de validação para ingressos"""

    ticket_id = fields.Int(dump_only=True)
    event_id = fields.Int(required=True)
    ticket_type = fields.Str(required=True, validate=validate.Length(min=3, max=50))
    price = fields.Decimal(required=True, as_string=True, places=2, validate=validate_positive)
    total_available_quantity = fields.Int(required=False, missing=0, validate=validate.Range(min=0))
    sold_quantity = fields.Int(dump_only=True)

    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)


class TicketUpdateSchema(TicketSchema):
    """Esquema de validação para atualização de ingressos"""

    ticket_type = fields.Str(required=False, validate=validate.Length(min=3, max=50))
    price = fields.Decimal(required=False, as_string=True, places=2, validate=validate_positive)
    total_available_quantity = fields.Int(required=False, validate=validate.Range(min=0))
