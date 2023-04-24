class CuentaBancaria:
    
    def __init__(self,numero,nombre,saldo):
        self.CuentaBancaria.numero = numero
        self.CuentaBancaria.nombre = nombre
        self.CuentaBancaria.saldo = saldo

    def info_cuenta(self,numero):
        for cuenta in cuentas:
            if cuenta.numero == numero:
                return f"Cuenta: {cuenta.numero} | Nombre: {cuenta.nombre} | Saldo: {cuenta.saldo}"
        return f"No existe una cuenta con número {numero}."
         
    
class Banco:
    
    def __init__(self):
        Banco.cuentas = []


