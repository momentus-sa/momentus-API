from marshmallow import Schema, fields, validate
from datetime import datetime

class EventSchema(Schema):
    """Esquema de validação para eventos"""

    event_id = fields.Int(dump_only=True)
    name = fields.Str(required=True, validate=validate.Length(min=3, max=100))
    description = fields.Str(validate=validate.Length(max=200))
    location = fields.Str(validate=validate.Length(max=100))
    event_picture_url = fields.Str(validate=validate.Length(max=255))
    event_date = fields.DateTime(required=True)
    registration_link = fields.Str(validate=validate.Length(max=255))
    budget = fields.Decimal(as_string=True, validate=validate.Range(min=0))
    active = fields.Bool(default=True)
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)

    # Relacionamento com o criador do evento
    event_creator_id = fields.UUID(required=True)
    event_creator = fields.Nested('UserSchema', dump_only=True)

    # Relacionamento com CashFlow, Ticket e Activity
    cash_flows = fields.List(fields.Nested('CashFlowSchema', dump_only=True))
    tickets = fields.List(fields.Nested('TicketSchema', dump_only=True))
    activities = fields.List(fields.Nested('ActivitySchema', dump_only=True))

    #Relacionamento com categoria de evento
    event_category_id = fields.Int(required=False)
    category = fields.Nested('EventCategorySchema', dump_only=True)

class EventUpdateSchema(EventSchema):
    """Esquema de validação para atualização de eventos"""

    event_id = fields.Int(dump_only=True)
    event_category_id = fields.Int(allow_none=True)
    name = fields.Str(validate=validate.Length(min=3, max=50))
    description = fields.Str(validate=validate.Length(max=200))
    location = fields.Str(validate=validate.Length(max=100))
    event_picture_url = fields.Str(validate=validate.Length(max=255))
    event_date = fields.DateTime()
    budget = fields.Decimal(as_string=True, validate=validate.Range(min=0))
    active = fields.Bool()
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)

    # Relacionamento com o criador do evento
    event_creator_id = fields.UUID(dump_only=True)
    event_creator = fields.Nested('UserSchema', dump_only=True)

    # Relacionamento com CashFlow, Ticket e Activity
    cash_flows = fields.List(fields.Nested('CashFlowSchema', dump_only=True))
    tickets = fields.List(fields.Nested('TicketSchema', dump_only=True))
    activities = fields.List(fields.Nested('ActivitySchema', dump_only=True))
