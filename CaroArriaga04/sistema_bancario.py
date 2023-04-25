from cuentas import Cuenta
cuenta = []
print("Sistema bancario")
op = 4
while op == 4:
    print("\nMENU")
    print("1.Crear cuenta\n2.Mostrar informacion de cuenta\n3.Mostrar todas las cuentas\n4.Salir")
    opcion = int(input("Elige una opcion: "))
    if opcion == 1:
        num = int(input("Ingresa el numero de cuenta: "))
        nombre = input("Ingresa nombre del cliente: ")
        saldo = float(input("Ingresa el saldo inicial: "))
        cuentas_clientes = Cuenta(num,nombre,saldo)
        cuenta.append(cuentas_clientes)
    elif opcion == 2: 
        cuenta = str(input("Ingresa el nombre al que esta la cuenta de la que deseas revisar informacion: "))
        cuenta.mostrar_informacion()
    elif opcion == 3:
        print (f"El total de cuentas creadas es: {len(cuenta)}")
