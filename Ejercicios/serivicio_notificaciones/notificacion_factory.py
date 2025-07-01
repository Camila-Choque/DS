from notificacion_email import NotificacionEmail
from notificacion_sms import NotificacionSMS
from notificacion_push import NotificacionPush

class NotificacionFactory:
    @staticmethod
    def crear_notificacion(tipo: str, destino: str):
        tipo = tipo.lower()

        if tipo == "email":
            return NotificacionEmail(destino)
        elif tipo == "sms":
            return NotificacionSMS(destino)
        elif tipo == "push":
            return NotificacionPush(destino)
        else:
            raise ValueError(f"Tipo de notificación no válido: {tipo}")
