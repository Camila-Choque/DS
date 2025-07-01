from abc import ABC, abstractmethod
class Notificacion(ABC):
    @abstractmethod
    def enviar(self,notificacion):
        pass 
