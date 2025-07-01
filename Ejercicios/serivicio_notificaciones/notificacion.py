from abc import ABC, abstractmethod
class Notificaion(ABC):
    @abstractmethod
    def envia(self,notificaion):
        pass 
