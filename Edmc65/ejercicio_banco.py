class CuentaBancaria:
    def __init__(self, numero_cuenta, nombre_cliente, dato_bancario):
        self.numero_cuenta = numero_cuenta
        self.nombre_cliente = nombre_cliente
        self.dato_bancario = dato_bancario

    def mostrar_info_cuenta(self):
        print("Número de cuenta: ", self.numero_cuenta)
        print("Nombre del cliente: ", self.nombre_cliente)
        print("Dato bancario: ", self.dato_bancario)


def crear_cuenta():
    numero_cuenta = input("Ingrese el número de cuenta: ")
    nombre_cliente = input("Ingrese el nombre del cliente: ")
    dato_bancario = input("Ingrese el saldo incial: ")
    cuenta = CuentaBancaria(numero_cuenta, nombre_cliente, dato_bancario)
    cuentas.append(cuenta)
    print("Cuenta creada exitosamente")


def mostrar_info_cuenta():
    numero_cuenta = input("Ingrese el número de cuenta: ")
    cuenta_encontrada = False
    for cuenta in cuentas:
        if cuenta.numero_cuenta == numero_cuenta:
            cuenta.mostrar_info_cuenta()
            cuenta_encontrada = True
            break
    if not cuenta_encontrada:
        print("Cuenta inexistente")


def mostrar_todas_cuentas():
    if len(cuentas) == 0:
        print("No hay cuentas creadas")
    else:
        print("Información de todas las cuentas:")
        for cuenta in cuentas:
            cuenta.mostrar_info_cuenta()

cuentas = []

opcion = 0 
while opcion !=4 :
    print("**********Menu**********")
    print("Seleccione una opción del menú:")
    print("1.- Crear cuenta")
    print("2.- Mostrar información de cuenta")
    print("3.- Mostrar todas las cuentas")
    print("4.- Salir")

    opcion = input("Ingrese la opción deseada: ")

    if opcion == "1":
        crear_cuenta()
    elif opcion == "2":
        mostrar_info_cuenta()
        input("Presiona enter para continuar...\n")
    elif opcion == "3":
        mostrar_todas_cuentas()
        input("Presiona enter para continuar...\n")
    elif opcion == "4":
        print("Saliendo...")
        break
    else:
        print("Opción inválida. Por favor, ingrese una opción válida del menú.")