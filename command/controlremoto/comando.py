from abc import ABC, abstractmethod

class Comando(ABC):
    @abstractmethod
    def ejecutar(self): #define lo que el comando debe hacer (por ejemplo, prender una luz).
        pass

    @abstractmethod
    def deshacer(self):#define cómo deshacer esa acción (por ejemplo, apagar la luz si se prendió antes).
        pass