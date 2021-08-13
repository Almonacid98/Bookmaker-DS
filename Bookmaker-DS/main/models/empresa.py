from main import db

class Empresa(db.Model):

    __id = db.Column(db.Integer, primary_key = True)
    __nombre = db.Column(db.String(50), nullable = False)
    __escudo = db.Column(db.String(50), nullable = False)
    __pais = db.Column(db.String(50), nullable = False)

    def __init__(self):
        self.__id = id

    def __repr__(self):
        return f'<Cliente: {self.__id} {self.__mail} >'

    def set_id(self, id):
        self.__id = id


    def get_id(self):
        return self.__id

    
    def set_apellido(self, apellido):
            self.__apellido = apellido


    def get_id(self):
        return self.__apellido


    def set_id(self, nombre):
        self.__nombre = nombre


    def get_id(self):
        return self.__nombre


    def set_id(self, mail):
        self.__mail = mail


    def get_id(self):
        return self.__mail