from marshmallow import Schema, fields, validate
from marshmallow.decorators import post_load
from main.models import PartidoModel
from .cuota_schema import CuotaSchema

class PartidoSchema(Schema):
    
    id = fields.Int(dump_only = True)
    fecha = fields.DateTime(required = True)
    equipo_local = fields.Int(required = True)
    equipo_visitante = fields.Int(required = True)
    finalizado = fields.Bool(required = True)
    ganador = fields.Str(required = True)
    goles_local =  fields.Int(required = True)
    goles_visitante = fields.Int(required = True)
    partido = fields.Nested(CuotaSchema)
    
    @post_load
    def make_cuota(self, data, **kwargs):
        return PartidoModel(**data)