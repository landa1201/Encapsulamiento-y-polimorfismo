class CarteraCripto:
    def __init__(self, usuario: str, saldo_btc: float = 0.0):
        self.__usuario = usuario
        self.__saldo_btc = saldo_btc

    def consultar_saldo(self):
        return self.__saldo_btc

    def comprar_btc(self, monto_usd: float, precio_actual_btc: float):
        if monto_usd <= 0 or precio_actual_btc <= 0:
            print("El monto o el precio deben ser mayores a cero.")
            return

        btc_comprado = monto_usd / precio_actual_btc
        self.__saldo_btc += btc_comprado
        print(f"Compraste {btc_comprado:.6f} BTC. Saldo actual: {self.__saldo_btc:.6f} BTC.")

    def vender_btc(self, monto_btc: float, precio_actual_btc: float):
        if monto_btc <= 0 or precio_actual_btc <= 0:
            print("El monto o el precio deben ser mayores a cero.")
            return

        if monto_btc > self.__saldo_btc:
            print("No tienes suficiente BTC para vender.")
            return

        usd_recibido = monto_btc * precio_actual_btc
        self.__saldo_btc -= monto_btc
        print(f"Vendiste {monto_btc:.6f} BTC. Recibes {usd_recibido:.2f} USD. Saldo restante: {self.__saldo_btc:.6f} BTC.")

cartera = CarteraCripto("Usuario1", 0.5)

print(f"Saldo inicial: {cartera.consultar_saldo():.6f} BTC\n")

cartera.comprar_btc(1000, 50000)  

print(f"Saldo después de compra: {cartera.consultar_saldo():.6f} BTC\n")

cartera.vender_btc(0.20, 52000)  
print(f"Saldo después de venta: {cartera.consultar_saldo():.6f} BTC")
