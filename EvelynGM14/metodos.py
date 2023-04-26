#Escribir un programa que simule un sistema bancario.
#El programa debe tener el siguiente menu: 
#1.- Crear cuenta
#2.- Mostrar informacion de cuenta
#3.- Mostrar todas las cuentas
#4.- Salir
#para crear una cuenta solicitar numero de cuenta, nombre del cliente y saldo inicial.


class Cuenta:
    def __init__(self,numeroCta,nombre,saldo):
        self.numeroCta = numeroCta
        self.nombre = nombre
        self.saldo = saldo

    def MostrarCta(self):
        mostrar = self.numeroCta,self.nombre,self.saldo
        return mostrar

    def TotalCuentas(self):
        totalCuentas = []
        return totalCuentas




   
