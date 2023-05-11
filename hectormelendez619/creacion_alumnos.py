from clases_alumnos import Alumno
alumnos = []

while True:
    print("Ingrese una opción:")
    print("1.- Agregar Alumno")
    print("2.- Mostrar informacion del alumno")
    print("3.- Eliminar alumno")
    print("4.- Mostrar todos los alumnos")
    print("5.- Salir")

    opcion = int(input())

    if opcion == 1:
        matricula = input("Ingrese la matrícula del alumno: ")
        nombre = input("Ingrese el nombre del alumno: ")
        carrera = input("Ingrese la carrera del alumno: ")
        calificaciones = input("Ingrese las calificaciones del alumno separadas por coma: ")
        calificaciones = [float(c) for c in calificaciones.split(",")]

        alumno = Alumno(matricula, nombre, carrera, calificaciones)
        alumnos.append(alumno)
        print("Alumno ingresado")

    elif opcion == 2:
        matricula = input("Ingrese la matrícula del alumno: ")

        for alumno in alumnos:
            if alumno.matricula == matricula:
                alumno.imprim_info()
                break
        else:
            print("No se encontro el alumno intente de nuevo")

    elif opcion == 3:
        matricula = input("Ingrese la matrícula del alumno: ")

        for alumno in alumnos:
            if alumno.matricula == matricula:
                alumnos.remove(alumno)
                print("Alumno eliminado.")
                break
        else:
            print("No se encontro el alumno intente de nuevo")

    elif opcion == 4:
        if len(alumnos) == 0:
            print("Alumnos no ingresados")
        else:
            for alumno in alumnos:
                alumno.imprim_info()

    elif opcion == 5:
        print("Hasta la proxima:)")
        break

    else:
        print("Opción no valida, Intente de nuevo")