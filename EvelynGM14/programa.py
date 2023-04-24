#Escribir un programa que simule un sistema bancario.
#El programa debe tener el siguiente menu: 
#1.- Crear cuenta
#2.- Mostrar informacion de cuenta
#3.- Mostrar todas las cuentas
#4.- Salir
#para crear una cuenta solicitar numero de cuenta, nombre del cliente y saldo inicial.

from metodos import Cuenta


cuentas = []
print("bienvenido al banco")
print("1.-Crear cuenta\n2.-Mostrar información de cuenta\n3.-Mostrar todas las cuentas\n4.-Salir")
opcion = int(input("Elija una opcion: "))

if opcion == 1:
    numeroCta = int(input("Digite su numero de cuenta: "))
    nombre = input("Ingrese su nombre: ")
    saldo = float(input("Digite el saldo inicial: "))
    
    objeto = Cuenta(numeroCta,nombre,saldo)

elif opcion == 2:
    print ("Digite su numero de cuenta: ")
    mos = objeto.MostrarCta()
    print (mostrar)


    

