from interruptor import Interruptor

class ApagarLuzCommand(Interruptor):
    def __init__(self,luz):
        self.luz = luz 
    
    def ejecutar(self):
        self.luz.apagar() 


