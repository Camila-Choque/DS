from interruptor import Interruptor

class EncenderLuzCommand(Interruptor):
    def __init__(self,luz):
        self.luz = luz 
    
    def ejecutar(self):
        self.luz.encender() 


