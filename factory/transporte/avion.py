from transporte import Transporte
#Clase concreta
class Avion(Transporte):
    def entregar(self):
        print("Entregando por avion")