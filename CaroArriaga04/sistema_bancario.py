from cuentas import Cuenta
cuentas = []
print("¡Bienvenido al sistema bancario!")
while True:
    print("\nTe presentamos el siguiente menu de opciones")
    print("1.Crear una cuenta\n2.Mostrar informacion de cuenta especifica\n3.Mostrar todas las cuentas\n4.Salir")
    opcion = int(input("Elige una opcion: "))
    if opcion == 1:
        numero_cuenta = int(input("Ingresa el numero de cuenta: "))
        nombre_cliente = input("Ingresa nombre del cliente: ")
        saldo_inicial = float(input("Ingresa el saldo inicial: "))
        cuentas_clientes = Cuenta(numero_cuenta, nombre_cliente, saldo_inicial)
        cuentas.append(cuentas_clientes)
    elif opcion == 2: 
        numero_cuenta = int(input("Ingresa el numero de cuenta del que deseas la informacion: "))
        for cuentas_clientes in cuentas:
            if cuentas_clientes.numero_cuenta == numero_cuenta:
                cuentas_clientes.mostrar_informacion()
    elif opcion == 3:
        print("CUENTAS CREADAS")
        for cuentas_clientes in cuentas:
            cuentas_clientes.mostrar_cuentas()
    elif opcion == 4:
        break
