from flask_restful import Resource
from flask import request
from flask import request, jsonify
from .. import db
from main.models import ClienteModel
from main.map import ClienteSchema

cliente_schema = ClienteSchema()
class Cliente(Resource):

    def get(self, id):
        
        cliente = db.session.query(ClienteModel).get_or_404(id)
        return cliente_schema.dump(cliente)
        
    def delete(self, id):
        
        cliente = db.session.query(ClienteModel).get_or_404(id)
        db.session.delete(cliente)
        db.session.commit()
        return '', 204

    def put(self, id):
    
        cliente = db.session.query(ClienteModel).get_or_404(id)
        data = request.get_json().items()
        for key, value in data:
            setattr(cliente, key, value)
        db.session.add(cliente)
        db.session.commit()
        return cliente_schema.dump(cliente), 201

class Clientes(Resource):

    def get(self):
    
        page = 1
        per_page = 10
        clientes = db.session.query(ClienteModel)
        if request.get_json():
            filters = request.get_json().items()
            for key, value in filters:
                if key == 'page':
                    page = int(value)
                if key == 'per_page':
                    per_page = int(value)
        #clientes = clientes.paginate(page, per_page, True, 30) 

        return cliente_schema.dump(clientes.all(), many = True)
    
    def post(self): 

        cliente = cliente_schema.load(request.get_json())
        db.session.add(cliente)
        db.session.commit()
        return cliente_schema.dump(cliente), 201
        