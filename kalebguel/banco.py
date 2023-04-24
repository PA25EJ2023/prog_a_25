class Crearcuenta:
    pass

class Infodecuenta:
    pass

class Mostrarcuenta:
    pass
print("Bienvenido")
print("Opciones disponibles")

while opcion !=5:
    print("1.Crear cuenta\n2.Mostrar info de cuenta\n3.Mostrar todas las cuentas\n4.Salir")
    opcion=int(input("Elige una opcion: [1,2,3]"))
    if opcion==1:#Crear cuenta
        nombre=input("Ingresa nombre:")
        numero=int(input("Numero de cuenta:"))
        saldo=float(input("Saldo inicial:"))
    
    elif opcion==2:#Mostrar info de cuenta
        cuenta=input("Info de cuenta:")

    elif opcion ==3:#Mostrar todas las cuentas
