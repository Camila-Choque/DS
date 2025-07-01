from procesar_pago import ProcesarPago
#Cliente
class TiendaOnline:
    def __init__(self, servicio_cobro: ProcesarPago):
        self.servicio_cobro = servicio_cobro

    def realizar_pago(self, monto: float):
        self.servicio_cobro.pagar(monto)
