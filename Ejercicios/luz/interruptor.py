from abc import ABC, abstractmethod

class Interruptor(ABC):
    @abstractmethod
    def ejecutar(self):
        pass