from abc import ABC, abstractmethod
#Fabrica pero no sabe que va a feabricar todavia, fabrica abstracta
class TransporteFactory(ABC):
    @abstractmethod
    def crear(self):
        pass