from procesar_pago import ProcesarPago

class ServicioDeCobroTarjetaCredito(ProcesarPago):
    def __init__(self, numero_tarjeta: str, titular: str, cvv: str, vencimiento: str):
        self.numero_tarjeta = numero_tarjeta
        self.titular = titular
        self.cvv = cvv
        self.vencimiento = vencimiento

    def pagar(self, monto: float) -> None:
        print(f"Procesando pago con Tarjeta de Crédito de {self.titular} por ${monto:.2f}...")

class ServicioDeCobroPayPal(ProcesarPago):
    def __init__(self, email: str):
        self.email = email

    def pagar(self, monto: float) -> None:
        print(f"Procesando pago con PayPal para la cuenta {self.email} por ${monto:.2f}...")

class ServicioDeCobroCriptomoneda(ProcesarPago):
    def __init__(self, wallet_address: str, moneda: str):
        self.wallet_address = wallet_address
        self.moneda = moneda

    def pagar(self, monto: float) -> None:
        print(f"Procesando pago con {self.moneda} desde la wallet {self.wallet_address} por ${monto:.6f}...")
