from notificacion import Notificaion

class NotificacionSMS (Notificaion):
    def __init__(self,telefono: int):
        self.telefono = telefono
    
    def enviar ():
        print("Enviando notificaion al numero {self.telefono}")
        