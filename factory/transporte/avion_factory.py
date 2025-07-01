from transporte_factory import TransporteFactory
from avion import Avion
#crea aviones
class AvionFactory(TransporteFactory):
    def crear(self):    
        return Avion()