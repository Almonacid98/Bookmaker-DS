from flask_restful import Resource
from flask import request
from flask import request, jsonify
from .. import db
from main.models import EquipoModel
from main.map import EquipoSchema

equipo_schema = EquipoSchema()
class Equipo(Resource):

    def get(self, id):
        
        equipo = db.session.query(EquipoModel).get_or_404(id)
        return equipo_schema.dump(equipo)
        
    def delete(self, id):
        
        equipo = db.session.query(EquipoModel).get_or_404(id)
        db.session.delete(equipo)
        db.session.commit()
        return '', 204

    def put(self, id):
    
        equipo = db.session.query(EquipoModel).get_or_404(id)
        data = request.get_json().items()
        for key, value in data:
            setattr(equipo, key, value)
        db.session.add(equipo)
        db.session.commit()
        return equipo_schema.dump(equipo), 201

class Equipos(Resource):

    def get(self):
    
        page = 1
        per_page = 10
        equipos = db.session.query(EquipoModel)
        if request.get_json():
            filters = request.get_json().items()
            for key, value in filters:
                if key == 'page':
                    page = int(value)
                if key == 'per_page':
                    per_page = int(value)
        #clientes = clientes.paginate(page, per_page, True, 30) 

        return equipo_schema.dump(equipos.all(), many = True)
    
    def post(self): 

        equipos = equipo_schema.load(request.get_json())
        db.session.add(equipos)
        db.session.commit()
        return equipo_schema.dump(equipos), 201
        