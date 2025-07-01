from servicio_de_cobro import (
    ServicioDeCobroTarjetaCredito,
    ServicioDeCobroPayPal,
    ServicioDeCobroCriptomoneda
)
from tienda_online import TiendaOnline

if __name__ == "__main__":
    tarjeta = ServicioDeCobroTarjetaCredito("1234-5678-9876-5432", "Mariela C. Z. Choque", "123", "12/26")
    tienda1 = TiendaOnline(tarjeta)
    tienda1.realizar_pago(1500.00)

    paypal = ServicioDeCobroPayPal("usuario@paypal.com")
    tienda2 = TiendaOnline(paypal)
    tienda2.realizar_pago(200.50)

    cripto = ServicioDeCobroCriptomoneda("1A2b3C4d5E6f7G8h9I0j", "Bitcoin")
    tienda3 = TiendaOnline(cripto)
    tienda3.realizar_pago(0.005)
