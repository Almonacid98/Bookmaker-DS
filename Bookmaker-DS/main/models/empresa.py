from main import db

class Empresa(db.Model):
    __tablename__ = "empresas" 
    __id = db.Column('id', db.Integer, primary_key = True)
    __razon_social = db.Column('razon_social', db.String(100), nullable = False)
    __mail = db.Column('email', db.String(100), nullable = False)

    def __repr__(self):
        return f'<Cliente: {self.__id} {self.__mail} >'

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id
    
    @id.deleter
    def id(self):
        del self.__id

    @property
    def razon_social(self):
        return self.__razon_social

    @razon_social.setter
    def razon_social(self, razon_social):
        self.__razon_social = razon_social
    
    @razon_social.deleter
    def razon_social(self):
        del self.__razon_social

      
    @property
    def mail(self):
        return self.__mail

    @mail.setter
    def mail(self, mail):
        self.__mail = mail
    
    @mail.deleter
    def mail(self):
        del self.__mail