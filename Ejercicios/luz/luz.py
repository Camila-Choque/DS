
class Luz():
    def __init__(self):
        self.prendida = False

    def encender(self):
        self.prendida = True
        print("La luz está encendida")

    def apagar(self):
        self.prendida = False
        print("La luz está apagada")