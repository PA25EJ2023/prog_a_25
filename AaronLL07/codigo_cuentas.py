from cuentas import Cuenta
cuentas = []
op = -1

print("Bienvenido")
while op != 4:
    print("1.- Crear cuenta\n2.- Mostrar información de cuenta\n3.- Mostrar todas las cuentas\n4.- Salir")
    op = int(input("Seleccione una opción: "))

    if op == 1:
        num_cuenta = int(input("Ingrese su numero de cuenta: "))
        nom_cliente = input("Ingrese su nombre completo: ")
        saldo_inicial = float(input("Ingrese su saldo incial: "))
        usuarios = Cuenta(num_cuenta, nom_cliente, saldo_inicial)
        cuentas.append(usuarios)

    elif op == 2:
        num_cuenta = int(input("Ingresa el numero de cuenta para poder mostrar la información: "))
        for usuarios in cuentas:
            if usuarios.num_cuenta == num_cuenta:
                usuarios.info_cuenta()
    
    elif op == 3:
        print("Total de usuarios creados: ")
        for usuarios in cuentas:
            usuarios.total_cuentas()
    
    elif op == 4:
        # Finaliza programa
        print("¡Hasta pronto!")