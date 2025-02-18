from marshmallow import Schema, fields

class EventSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    description = fields.Str()
    date = fields.DateTime(required=True)
    location = fields.Str(required=True)
    created_by = fields.Int(dump_only=True)  
