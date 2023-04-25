class CuentaBancaria:
    
    cuentas = [] 
    
    def __init__(self, numero_cuenta, cliente, saldo):
        self.numero_cuenta = numero_cuenta
        self.cliente = cliente
        self.saldo = saldo
        CuentaBancaria.cuentas.append(self)
        
    def crear_cuenta():
        numero_cuenta = input("Ingrese el número de cuenta: ")
        cliente = input("Ingrese el nombre del cliente: ")
        saldo = float(input("Ingrese el saldo inicial: "))
        
        CuentaBancaria(numero_cuenta, cliente, saldo)
        print("Cuenta creada exitosamente")
    
    def mostrar_info_cuenta():
        numero_cuenta = input("Ingrese el número de cuenta: ")
        for cuenta in CuentaBancaria.cuentas:
            if cuenta.numero_cuenta == numero_cuenta:
                print("Número de cuenta:", cuenta.numero_cuenta)
                print("Nombre del cliente:", cuenta.cliente)
                print("Saldo:", cuenta.saldo)
                return
        print("No se encontró la cuenta")
    
    def mostrar_todas_cuentas():
        for cuenta in CuentaBancaria.cuentas:
            print("Número de cuenta:", cuenta.numero_cuenta)
            print("Nombre del cliente:", cuenta.cliente)
            print("Saldo:", cuenta.saldo)
            
    def salir():
        print("Gracias por utilizar nuestro servicio")
        
    
while True:
    print("\nBienvenido al sistema bancario.")
    print("Menú: ")
    print("1. Crear cuenta.")
    print("2. Mostrar información de cuenta.")
    print("3. Mostrar todas las cuentas.")
    print("4. Salir.")
    
    opcion = input("Ingrese el número de opción: ")
    
    if opcion == "1":
        CuentaBancaria.crear_cuenta()
    elif opcion == "2":
        CuentaBancaria.mostrar_info_cuenta()
    elif opcion == "3":
        CuentaBancaria.mostrar_todas_cuentas()
    elif opcion == "4":
        CuentaBancaria.salir()
    else:
        print("Opción inválida")