#FUNCIONA
import funciones_EV3

opcion = 0 
while opcion !=3 :
    print("¡Bienvenido al sistema del alumnado!")
    print("Seleccione una opción del menú:")
    print("1. Crear Alumno")
    print("2. Mostrar información de alumno")
    print("3. Eliminar alumno")
    print("4. Mostrar todos los alumnos")
    print("5. Salir")

    opcion = input("Ingrese el número de la opción deseada: ")

    if opcion == "1":
        funciones_EV3.calificaciones.clear()
        funciones_EV3.crear_alumno()
    elif opcion == "2":
        funciones_EV3.mostrar_info_del_alumno()
        input("Presiona enter para continuar...")
    elif opcion == "3":
        funciones_EV3.eliminar_alumno()
        input("Presiona enter para continuar...")
    elif opcion == "4":
        funciones_EV3.mostrar_alumnos()
        input("Presiona enter para continuar...")
    elif opcion == "5":
        print("Gracias por utilizar el sistema de alumnado. ¡Hasta luego!")
        break
    else:
        print("Opción inválida. Por favor, ingrese una opción válida del menú.")
