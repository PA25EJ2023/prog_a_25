#Escribir un programa que simule un sistema bancario.
#el programa debe de tener el siguiente menu:
#1.Crear cuenta\n2.Mostrar info de cuenta\n3.Mostrar todas las cuentas\n4.Salir
#Para crear una cuenta solicitar numero de cuenta, nombre del cliente y saldo inicial

class Cuenta:
    def __init__(self,numero,nombre,saldo) :
        self.numero = numero
        self.nombre = nombre
        self.saldo = saldo

class Banco: 
    def __init__(self) :
        self.cuentas = []

    def crear_cuentas(self):
         numero = int(input("Ingrese el número de cuenta: "))
         nombre = input("Ingrese el nombre: ")
         saldo = float(input("Ingrese el saldo inicial de la cuenta: "))
         cuenta = Cuenta(numero, nombre, saldo)
         self.cuentas.append(cuenta)
         print("Su cuenta se creo")

