from notificacion import Notificacion

class NotificacionPush (Notificacion):
    def __init__(self,dispositivo_id: str):
        self.dispositivo_id = dispositivo_id
    
    def enviar(self, mensaje):
        print(f"[PUSH] Enviando a {self.dispositivo_id}: {mensaje}")
        