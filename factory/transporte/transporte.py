from abc import ABC, abstractmethod
#Interfaz para todos los medios de transporte
class Transporte(ABC):
    @abstractmethod
    def entregar(self):
        pass
