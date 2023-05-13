import evidencia3

while True:

    print("")
    print("A continuación, elija una de las siguientes opciones: ")
    print("")
    print("1. Agregar alumno")
    print("2. Mostrar información de un alumno")
    print("3. Eliminar alumno")
    print("4. Mostrar todos los alumnos")
    print("5. Salir")
    print("")

    opcion = int(input("Por favor, ingresa a continuación la opción deseada:  "))
    print("")
    print("")



    if opcion == 1:
        evidencia3.agg_alumno()
            
    elif opcion == 2:
        evidencia3.most_info_alumno()

    elif opcion == 3:
        evidencia3.eliminar_alumno()

    elif opcion == 4:
        evidencia3.most_todos_alumnos()
        

    elif opcion == 5:
        print("Muchas gracias por usar este sistema. ¡Hasta pronto!")
        break
    else:
            print("Lo sentimos, ha ingresado una opción no presentada en el menú.")
            print("")
            print("Por favor, ingrese una opción del menú presentado.")

    print("")

