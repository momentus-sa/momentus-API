"""Módulo que define o esquema de fluxos de caixa e o valida"""
from marshmallow import Schema, fields, validate

class CashFlowSchema(Schema):
    """Esquema de validação do fluxo de caixa"""

    cash_flow_id = fields.Int(dump_only=True)
    event_id = fields.Int(required= True)  # Pode ser None se não for obrigatório
    title = fields.Str(required=True, validate=validate.Length(min=3, max=50))
    description = fields.Str(validate=validate.Length(max=200))
    flow_type = fields.Str(required=True, validate=validate.OneOf(["earning", "expenses"]))
    value = fields.Decimal(required=True, as_string=True, places=2)
    answerable = fields.Str(required=True, validate=validate.Length(min=3, max=50))
    spent_at = fields.DateTime()
    updated_at = fields.DateTime(dump_only=True)

#analisar depois
class CashFlowUpdateSchema(CashFlowSchema):
    """Esquema de validação para atualização de fluxo de caixa"""

    event_id = fields.Int(required=False)
    title = fields.Str(required=False, validate=validate.Length(min=3, max=50))
    description = fields.Str(validate=validate.Length(max=200))
    flow_type = fields.Str(required=False, validate=validate.OneOf(["earning", "expenses"]))
    value = fields.Decimal(required=False, as_string=True, places=2)
    answerable = fields.Str(required=False, validate=validate.Length(min=3, max=50))
    spent_at = fields.DateTime(required=False)
    updated_at = fields.DateTime(dump_only=True)
