class ControlRemoto:
    def __init__(self):
        self.comando_actual = None #no tiene ningun comando asignado

    def asignar_comando(self, comando):
        self.comando_actual = comando #permite asignarle un comando

    def presionar_boton(self):
        if self.comando_actual: #simula presionar un botón para ejecutar una acción.
            self.comando_actual.ejecutar() #Si hay un comando asignado, llama a su método ejecutar().
        else:
            print("No hay ningún comando ejecutándose") #si no hay ninguno muestra el mensaje

    def presionar_boton_deshacer(self):
        if self.comando_actual: #Simula presionar un botón de "deshacer".
            self.comando_actual.deshacer() #Llama al método deshacer() del comando actual
        else:
            print("No hay ningún comando deshaciendo")

    #ACTUA COMO INVOKER 