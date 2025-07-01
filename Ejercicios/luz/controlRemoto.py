class ControlRemoto():
    def __init__(self):
        self.comando = None


    def asignar_comando(self,comando):
        self.comando = comando

    def presionar_boton(self):
        if self.comando:
            self.comando.ejecutar()
        else:
            print("No hay comando asignado")
