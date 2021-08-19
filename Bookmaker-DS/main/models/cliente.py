from main import db

class Cliente(db.Model):
    
    id = db.Column(db.Integer, primary_key = True)
    apellido = db.Column(db.String(50), nullable = False)
    nombre = db.Column(db.String(50), nullable = False)
    mail = db.Column(db.String(120), nullable = False)

    def __repr__(self):
        return f'<Cliente: {self.__id} {self.__mail} >'

    def to_json(self):
        cliente_json = {
            'id' : self.id,
            'apellido' : str(self.apellido),
            'nombre' : self.nombre,
            'mail' : self.mail
        }
        return cliente_json

    @staticmethod

    def from_json(cliente_json):
        id = cliente_json.get('id')
        apellido = cliente_json.get('apellido')
        nombre = cliente_json.get('nombre')
        mail = cliente_json.get('mail')
        return Cliente(id = id,
                        apellido = apellido,
                        nombre = nombre, 
                        mail = mail,
                        )