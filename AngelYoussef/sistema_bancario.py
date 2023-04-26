class Banco:
    cuentas = []

    def crear_cuenta(self):
        cuenta = {}
        num_cuenta = input("Ingrese el número de cuenta: ")
        nombre = input("Ingrese el nombre del cliente: ")
        saldo = float(input("Ingrese el saldo inicial: "))
        cuenta['num_cuenta'] = num_cuenta
        cuenta['nombre'] = nombre
        cuenta['saldo'] = saldo
        self.cuentas.append(cuenta)
        print("¡Cuenta creada exitosamente!\n")
    
    def mostrar_cuenta(self):
        num_cuenta = input("Ingrese el número de cuenta: ")
        for cuenta in self.cuentas:
            if cuenta['num_cuenta'] == num_cuenta:
                print("Número de Cuenta:", cuenta['num_cuenta'])
                print("Nombre del Cliente:", cuenta['nombre'])
                print("Saldo Actual:", cuenta['saldo'], "\n")
                break
        else:
            print("Cuenta no encontrada\n")
    
    def mostrar_todas_cuentas(self):
        if len(self.cuentas) == 0:
            print("Aún no se han creado cuentas\n")
        else:
            print("¡Todas las cuentas registradas!\n")
            for cuenta in self.cuentas:
                print("Número de Cuenta:", cuenta["num_cuenta"])
                print("Nombre del Cliente:", cuenta["nombre"])
                print("Saldo Actual:", cuenta["saldo"], "\n")
    
    def menu(self):
        while True:
            print("*****MENU*****")
            print("1. Crear cuenta")
            print("2. Mostrar información de cuenta")
            print("3. Mostrar todas las cuentas")
            print("4. Salir\n")
            opcion = input("Ingrese una opción (1-4): ")
            print("")
            if opcion == "1":
                self.crear_cuenta()
            elif opcion == "2":
                self.mostrar_cuenta()
            elif opcion == "3":
                self.mostrar_todas_cuentas()
            elif opcion == "4":
                print("¡Hasta pronto!")
                break
            else:
                print("Opción no válida, intente de nuevo\n")

