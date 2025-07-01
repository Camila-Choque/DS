from notificacion import Notificacion

class NotificacionSMS (Notificacion):
    def __init__(self,telefono: str):
        self.telefono = telefono
    
    def enviar(self, mensaje):
        print(f"[TELEFONO] Enviando al numero {self.telefono}: {mensaje}")
        
        