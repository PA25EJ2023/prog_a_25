from ClassEvidencia3 import Alumno0, Add_Alumno, imprimir_info, Mostrar_Alumnos, Alumnos, eliminar_alumno
opcion=0
while opcion !=4:

    print("********Menu********")
    print("Seleccione una opción del menu: ")
    print("1.- Agregar Alumno")
    print("2.- Mostrar información del alumno")
    print("3.- Eliminar Alumno")
    print("4.- Mostrar a todos los alumnos")
    print("5.- Salir")

    opcion = input("Ingrese la opción deseada: ")
    if opcion == "1":
        #Agregar Alumno
        Add_Alumno()

    elif opcion == "2":
        #Mostrar info del alumno
        imprimir_info()

    elif opcion == "3":
        #Eliminar alumno
        Matricula=input("Ingresa la Matricula:")
        eliminar_alumno()

        input("Presiona ENTER para continuar...")

    elif opcion == "4":
        #Mostrar todos los alumnos
        Mostrar_Alumnos()
        input("Presiona ENTER para continuar...")

    elif opcion == "5":
        print("Saliendo...")
        break
    else: 
        print("Opción Invalida. Ingrese una opción valida")