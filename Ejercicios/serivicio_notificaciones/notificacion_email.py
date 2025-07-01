from notificacion import Notificacion

class NotificacionEmail (Notificacion):
    def __init__(self,correo: str):
        self.correo = correo
    
    def enviar(self, mensaje):
        print(f"[EMAIL] Enviando a {self.correo}: {mensaje}")
        