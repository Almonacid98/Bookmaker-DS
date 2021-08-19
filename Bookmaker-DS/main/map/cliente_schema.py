from marshmallow import Schema, fields, validate

class ClienteSchema(Schema):
    id = fields.Int(dump_only = True)
    apellido = fields.Str(required = True)
    nombre = fields.Str(required = True)
    mail = fields.Str(required = True, validate = validate.Email())

    def make_cliente(self, data, **kwargs):
        self.
