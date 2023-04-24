#escribir un programa que simule un sistema bancario.
#el programa debe tener el siguiente menu:

#crear cuenta
#mostrar info de cuenta
#salir

#para crear una cuenta solicitar numero de cuenta, nombre del cliente y saldo inicial
from clase_sm import Cuenta


 
def crear_cuenta():
    numero_cuenta = input("Ingrese el número de cuenta: ")
    nombre_cliente = input("Ingrese el nombre del cliente: ")
    saldo = float(input("Ingrese el saldo inicial: "))
    cuenta = Cuenta(numero_cuenta, nombre_cliente, saldo)
    return cuenta
 

def mostrar_info_cuenta(cuenta):
    cuenta.mostrar_info()
 
 
def menu():
    lista_cuentas = []
    cuenta = None
    while True:
        print(f"{'-'*10}BIENVENIDO AL Sistema Bancario{'-'*10}")
        print(f"{'-'*10}ELIJA UNA OPCION{'-'*10}")
        print("1. Crear cuenta\n2. Mostrar info de cuenta\n3. Mostrar todas las cuentas\n4. Salir ")
        opcion = int(input("Seleccione una opción: "))
        if opcion == 1:
            cuenta = crear_cuenta()
            lista_cuentas.append(cuenta)
        
        elif opcion == 2:
            if cuenta is not None:
                mostrar_info_cuenta(cuenta)
            else:
                print("No hay cuenta creada")
        elif opcion == 3:
            print(lista_cuentas)
        elif opcion == 4:
            break
 
 
menu()
