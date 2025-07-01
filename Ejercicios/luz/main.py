# Suponiendo que ya tenés una clase Luz y comandos EncenderLuzCommand, ApagarLuzCommand

from luz import Luz
from controlRemoto import ControlRemoto
from encenderLuzCommand import EncenderLuzCommand
from apagarLuzCommand import ApagarLuzCommand


luz = Luz()
control = ControlRemoto()

encender = EncenderLuzCommand(luz)
apagar = ApagarLuzCommand(luz)

control.asignar_comando(encender)
control.presionar_boton()  # La luz está encendida

control.asignar_comando(apagar)
control.presionar_boton()  # La luz está apagada
