from notificacion import Notificaion

class NotificacionEmail (Notificaion):
    def __init__(self,correo: str):
        self.correo = correo
    
    def enviar ():
        print("Enviando notificaion al correo {self.correo}")
        