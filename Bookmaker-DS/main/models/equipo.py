from main import db
from sqlalchemy.ext.hybrid import hybrid_property

class Equipo(db.Model):
    __tablename__ = "equipos"
    __id = db.Column('id', db.Integer, primary_key = True)
    __nombre = db.Column('nombre', db.String(50), nullable = False)
    __escudo = db.Column('escudo', db.String(50), nullable = False)
    __pais = db.Column('pais', db.String(50), nullable = False)
    __puntaje = db.Column('puntaje', db.Float, nullable = False)

    def __repr__(self):
        return f'<Cliente: {self.__id} {self.__nombre} {self.__escudo}  {self.__pais} {self.__puntaje}>'

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
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre
    
    @nombre.deleter
    def nombre(self):
        del self.__nombre
    
    @hybrid_property
    def escudo(self):
        return self.__escudo

    @escudo.setter
    def escudo(self, escudo):
        self.__escudo = escudo
    
    @escudo.deleter
    def escudo(self):
        del self.__escudo
    
    @hybrid_property
    def pais(self):
        return self.__pais

    @pais.setter
    def pais(self, pais):
        self.__pais = pais
    
    @pais.deleter
    def pais(self):
        del self.__pais

    @hybrid_property
    def puntaje(self):
        return self.__puntaje

    @puntaje.setter
    def puntaje(self, puntaje):
        self.__puntaje = puntaje
    
    @puntaje.deleter
    def puntaje(self):
        del self.__puntaje