from flask_restful import Resource
from flask import request
from flask import request, jsonify
from main.services import PartidoService


class Apuesta(Resource):

    def get(self):
        service = PartidoService()
        return service.obtener_partidos_no_finalizados