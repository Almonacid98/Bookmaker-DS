from main.models import ClienteModel

class ClienteFiltros():
    
    def __init__(self, clients):
        self.__clients = clients
        self.__dict_filter = {"id": self.__filtro_por_id,
                   "nombre": self.__filtro_por_nombre,
                   "apellido": self.__filtro_por_apellido,
                   "mail": self.__filtro_por_mail
    }


    def __filtro_por_id(self, value):

        return self.__clients.filter(ClienteModel.id == int(value))
    

    def __filtro_por_nombre(self, value):

        return self.__clients.filter(ClienteModel.nombre.like('%' + value + '%'))

    
    def __filtro_por_apellido(self, value):

        return self.__clients.filter(ClienteModel.apellido.like('%' + value + '%'))


    def __filtro_por_mail(self, value):

        return self.__clients.filter(ClienteModel.mail.like('%' + value + '%'))


    def aplicar_filtro(self, key, value):
        
        return self.__dict_filter[key](value)
    