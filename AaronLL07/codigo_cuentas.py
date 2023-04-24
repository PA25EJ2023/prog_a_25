from cuentas import Cuentas
cuenta = []
op = -1

while op != 4:
    print("Bienvenidos")

    print("1.- Crear cuenta\n2.- Mostrar información de cuenta\n3.- Mostrar todas las cuentas\n4.- Salir")
    op = int(input("Seleccione una opción: "))

    if op == 1:
        num_cuenta = int(input("Ingrese su numero de cuenta: "))
        nom_cliente = input("Ingrese su nombre completo: ")
        saldo_inicial = float(input("Ingrese su saldo incial: "))
        usuario = Cuentas(num_cuenta, nom_cliente, saldo_inicial)
        cuenta = usuario


    elif op == 2:
        num_cuenta = int(input("Ingrese el numero de cuenta: "))
        cuenta.infoCuenta()
        