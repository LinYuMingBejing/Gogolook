from marshmallow import Schema, fields


class TaskSchema(Schema):
    name = fields.String(required=True)
    status = fields.Boolean(required=True)