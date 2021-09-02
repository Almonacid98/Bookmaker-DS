from marshmallow import Schema, fields, validate
from marshmallow.decorators import post_load
from main.models import EquipoModel


class EquipoSchema(Schema):

    id = fields.Int(dump_only = True)
    nombre = fields.Str(required = True)
    escudo = fields.Str(required = True)
    pais = fields.Str(required = True)
    puntaje = fields.Int(required = True)


    @post_load
    def make_equipo(self, data, **kwargs):
        return EquipoModel(**data)
