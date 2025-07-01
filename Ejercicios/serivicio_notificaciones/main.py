from notificacion_factory import NotificacionFactory

tipo = input("Tipo de notificación (email/sms/push): ")
destino = input("Destino (correo, número o ID de dispositivo): ")
mensaje = input("Mensaje a enviar: ")

notificacion = NotificacionFactory.crear_notificacion(tipo, destino)
notificacion.enviar(mensaje)
