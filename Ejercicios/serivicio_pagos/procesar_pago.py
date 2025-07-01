from abc import ABC, abstractmethod

class ProcesarPago(ABC):
    @abstractmethod
    def pagar(self, monto: float) -> None:
        pass
