class Cuenta:
    def __init__(self, numero_cuenta, nombre_cliente, saldo):
        self.numero_cuenta = numero_cuenta
        self.nombre_cliente = nombre_cliente
        self.saldo = saldo
 
    def mostrar_info(self):
        print(f"{'*'*20}")
        print(f"Número de cuenta: {self.numero_cuenta}\nNombre del cliente: {self.nombre_cliente}\nSaldo: {self.saldo}")
        print(f"{'*'*20}")
    
    def mostrar_cuentas(self):
        print(f"\nEl numero de cuenta: {self.numero_cuenta}")
        print(f"El nombre del cliente: {self.nombre_cliente}")
        print(f"El saldo inicial: {self.saldo_inicial}")