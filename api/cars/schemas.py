from marshmallow import Schema, fields


# Defining marshmallow Schema for the cars Table for datatype validation
class CarSchema(Schema):
    id=fields.Integer()
    object_id=fields.String()
    year=fields.Integer()
    make = fields.String()
    model= fields.String()
    category= fields.String()
    created_at= fields.DateTime()
    updated_at= fields.DateTime()
    owner_id= fields.Integer()