from marshmallow import Schema, fields, validate
from marshmallow.decorators import post_load
from main.models import ApuestaModel

class ApuestaSchema(Schema):

    id = fields.Int(dump_only = True)
    fecha = fields.DateTime(required = True)
    monto = fields.Float(required = True)
    equipo_ganador = fields.Int(required = True)

    @post_load
    def make_apuesta(self, data, **kwargs):
        return ApuestaModel(**data)