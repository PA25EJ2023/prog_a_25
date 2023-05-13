from Evidencia3 import Alumnos

alumnos = []

while True:
    print("Menu")
    print(f'1.- Agregar Alumno\n 2.- Mostrar info del alumno\n 3.- Eliminar alumno\n 4.- Mostrar todos los alumnos\n 5.- Salir')

    opcion = int(input("Seleccione una opción del menu: "))

    if opcion == 1:
        matricula = input("Ingrese la matricula del alumno: ")
        nombre = input("Ingrese el nombre del alumno: ")
        carrera = input("Ingrese la carrera del alumno: ")
        calificaciones = []

        for i in range(3):
            calificacion = float(input(f"Ingrese la calificación {i+1}: "))
            calificaciones.append(calificacion)

        alumno = Alumnos(matricula, nombre, carrera, calificaciones)
        alumnos.append(alumno)
        print("Alumno agregado correctamente")

    elif opcion == 2:
        matricula = input("Ingrese la matricula del alumno: ")
        encontrado = False

        for alumno in alumnos:
            if alumno.matricula == matricula:
                alumno.imprimir_info()
                encontrado = True

        if not encontrado:
            print("No se encontró al alumno con esa matrícula")

    elif opcion == 3:
        matricula = input("Ingrese la matricula del alumno: ")
        eliminado = False

        for alumno in alumnos:
            if alumno.matricula == matricula:
                alumnos.remove(alumno)
                eliminado = True
                print("Alumno eliminado correctamente")

        if not eliminado:
            print("No se encontró al alumno con esa matrícula")

    elif opcion == 4:
        for alumno in alumnos:
            alumno.imprimir_info()

    elif opcion == 5:
        print("¡Hasta luego!")
        break

    else:
        print("Opción inválida. Intente de nuevo.")
