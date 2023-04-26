class Cuenta:
    def __init__(self,numero_cuenta,nombre_cliente,saldo_inicial):
        self.numero_cuenta = numero_cuenta
        self.nombre_cliente = nombre_cliente
        self.saldo_inicial = saldo_inicial
    def mostrar_informacion(self):
        print (f"La informacion de la cuenta numero {self.numero_cuenta} es: \nNombre del cliente: {self.nombre_cliente}\nSaldo inicial: {self.saldo_inicial}")
    def mostrar_cuentas(self):
        print(f"\nEl numero de cuenta: {self.numero_cuenta}")
        print(f"El nombre del cliente: {self.nombre_cliente}")
        print(f"El saldo inicial: {self.saldo_inicial}")