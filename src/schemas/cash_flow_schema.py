"""Módulo que define o esquema de fluxos de caixa e o valida"""
from marshmallow import Schema, fields, validate

class CashFlowSchema(Schema):
    """Esquema de validação do fluxo de caixa"""

    cash_flow_id = fields.Int(dump_only=True)
    event_id = fields.Int(required= True)
    title = fields.Str(required=True, validate=validate.Length(min=3, max=50))
    description = fields.Str(validate=validate.Length(max=200))
    flow_type = fields.Str(required=True, validate=validate.OneOf(["earning", "expense"]))
    value = fields.Decimal(required=True, as_string=True, places=2)
    answerable = fields.Str(required=True, validate=validate.Length(min=3, max=50))
    spent_at = fields.DateTime()
    created_at = fields.DateTime(dump_only= True)
    updated_at = fields.DateTime(dump_only=True)

#analisar depois
class CashFlowUpdateSchema(CashFlowSchema):
    """Esquema de validação para atualização de fluxo de caixa"""

    event_id = fields.Int(dump_ony=True)
    title = fields.Str(required=False, validate=validate.Length(min=3, max=50))
    description = fields.Str(validate=validate.Length(max=200))
    flow_type = fields.Str(required=False, validate=validate.OneOf(["earning", "expense"]))
    value = fields.Decimal(required=False, as_string=True, places=2)
    answerable = fields.Str(required=False, validate=validate.Length(min=3, max=50))
    spent_at = fields.DateTime(format="%Y-%m-%dT%H:%M:%S", required = False)
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)
