class Banco:

    cuenta = []

    def __init__(self,numero,nombre,saldo):
        self.numero = numero
        self.nombre = nombre
        self.saldo = saldo

    op = input("Que opcion desea realizar 1.Crear Cuenta\n2.Consultar Cuenta\n3.Crear Cuentas Consultadas\n4.Salir")
    
    if op == 1:
        nombre = input("Ingrese su nombre")
        numero = input(str("Ingrese su numero de usuario"))
        saldo = input(str("Ingrese su saldo"))


