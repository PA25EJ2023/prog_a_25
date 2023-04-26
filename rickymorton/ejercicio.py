#escribir un programa que simule un sistema bancario. El programa debe tener el siguente menu
#1.-Crear cuenta
#2.-Mostrar info cuenta
#3.-Mostrar todas las cuentas
#4.-Salir
# para crear una ceunra solicitar numero de ceunta, nombre del cliente y saldo inicial.
import time
print("Bienvenido al sistema bancario")
op= 0
while op != 4:
    print("Opciones disponibles")
    print("1.-Crear una cuenta\n 2.-Mostrar info\n 3.-Mostrar todas las cuentas\n 4.-Salir")
    op = int(input("ingresa una opcion"))

    if op == 1:
        print("Creando cuenta..............")
        time.sleep(3)
        no_cuenta =int(input("Ingrese el numero de cuenta"))
        nombre = str(input("Ingresa tu nombre"))
        saldo_inicial = float(input("Ingresa saldo inicial"))