print ("Bienvenido al sistema bancario")
print("1-Crear una cuenta nueva \n2-Mostrar información de una cuenta existente \n3-Mostrar todas las cuentas existentes \n4-Salir")

opcion = int(input("¿Que acción desea realizar [1,2,3,4]?\n"))

while opcion != 4:

    if opcion == 1:
        pass
    elif opcion == 2:
        pass
    elif opcion == 3:
        pass

    if opcion > 4:
        print ("Por favor ingrese una opción valida")
        print("1-Crear una cuenta nueva \n2-Mostrar información de una cuenta existente \n3-Mostrar todas las cuentas existentes \n4-Salir")
        opcion = int(input("¿Que acción desea realizar [1,2,3,4]?\n"))
    
print ("Gracias por usar nuestra aplicación, que tenga un buen día")    