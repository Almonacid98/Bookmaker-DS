from .. import db
from sqlalchemy.ext.hybrid import hybrid_property

class Cuota(db.Model):
    __id = db.Column('id', db.Integer, primary_key = True)
    __probabilidad_local = db.Column('probabilidad_local', db.Float)
    __probabilidad_empate = db.Column('probabilidad_empate', db.Float)
    __probabilidad_visitante = db.Column('probabilidad_visitante', db.Float)
    partido = db.relationship('Partido', back_populates = 'cuota', uselist = False)
    
    def __repr__(self):
            return f'<Cuota: {self.__id} {self.__fecha} >'

    @hybrid_property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id
    
    @id.deleter
    def id(self):
        del self.__id
    
    @hybrid_property
    def probabilidad_local(self):
        return self.__probabilidad_local

    @probabilidad_local.setter
    def probabilidad_local(self, probabilidad_local):
        self.___probabilidad_local = probabilidad_local
    
    @probabilidad_local.deleter
    def probabilidad_local(self):
        del self.__probabilidad_local

    @hybrid_property
    def probabilidad_empate(self):
        return self.__probabilidad_empate

    @probabilidad_empate.setter
    def probabilidad_empate(self, probabilidad_empate):
        self.__probabilidad_empate = probabilidad_empate

    @probabilidad_empate.deleter
    def probabilidad_empate(self):
        del self.__probabilidad_empate
    
    @hybrid_property
    def probabilidad_visitante(self):
        return self.__probabilidad_visitante

    @probabilidad_visitante.setter
    def probabilidad_visitante(self, probabilidad_visitante):
        self.__probabilidad_visitante = probabilidad_visitante
    
    @probabilidad_visitante.deleter
    def probabilidad_visitante(self):
        del self.__probabilidad_visitante