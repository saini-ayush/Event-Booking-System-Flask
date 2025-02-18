from marshmallow import Schema, fields

class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    password = fields.Str(required=True)
