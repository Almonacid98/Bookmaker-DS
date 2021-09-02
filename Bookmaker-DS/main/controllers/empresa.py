from flask_restful import Resource
from flask import request
from flask import request, jsonify
from .. import db
from main.models import EmpresaModel
from main.map import EmpresaSchema

empresa_schema = EmpresaSchema()
class Empresa(Resource):

    def get(self, id):
        
        empresa = db.session.query(EmpresaModel).get_or_404(id)
        return empresa_schema.dump(empresa)
        
    def delete(self, id):
        
        empresa = db.session.query(EmpresaModel).get_or_404(id)
        db.session.delete(empresa)
        db.session.commit()
        return '', 204

    def put(self, id):
    
        empresa = db.session.query(EmpresaModel).get_or_404(id)
        data = request.get_json().items()
        for key, value in data:
            setattr(empresa, key, value)
        db.session.add(empresa)
        db.session.commit()
        return empresa_schema.dump(empresa), 201

class Empresas(Resource):

    def get(self):
    
        page = 1
        per_page = 10
        empresas = db.session.query(EmpresaModel)
        if request.get_json():
            filters = request.get_json().items()
            for key, value in filters:
                if key == 'page':
                    page = int(value)
                if key == 'per_page':
                    per_page = int(value)
        #clientes = clientes.paginate(page, per_page, True, 30) 

        return empresa_schema.dump(empresas.all(), many = True)
    
    def post(self): 

        empresas = empresa_schema.load(request.get_json())
        db.session.add(empresas)
        db.session.commit()
        return empresa_schema.dump(empresas), 201
        