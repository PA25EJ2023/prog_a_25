# Clase de Cuenta
class Cuenta:

    def __init__(self, num_cuenta, nom_cliente, saldo_inicial):
        self.num_cuenta = num_cuenta
        self.nom_cliente = nom_cliente
        self.saldo_inicial = saldo_inicial

    def info_cuenta(self):
        print(21*"*")
        print(f"Numero de cuenta: {self.num_cuenta}\nNombre: {self.nom_cliente}\nSaldo: {self.saldo_inicial}")
        print(21*"*")
        
    def total_cuentas(self):
        print(21*"*")
        print(f"Numero de cuenta: {self.num_cuenta}\nNombre: {self.nom_cliente}\nSaldo: {self.saldo_inicial}")
