from evidencia3_clase import *

alumnos_clase = []
while True:
    print("Ingrese una opcion: ")
    opcion = int(input(f"1.Agregar a un alumno: \n2.Mostrar info de alumno: \n3.Eliminar a un alumno: \n4.Mostrar a todos los alumnos: \n5.Salir "))
    
    #Agregar alumnos
    if opcion == 1:
        matricula = int(input("Ingrese la matricula del alumno: "))
        nombre = input("Ingrese el nombre del alumno: ")
        carrera = input("En que carrera esta el alumno? ")
        califs = []
        agregar = "S"
        while agregar.upper() == "S":
            calif = float(input("Ingrese la calificacion "))
            califs.append(calif)
            agregar = input("Deseas agregar otra calificacion? S/N: ")
        estudiante = Alumnos(matricula, nombre, carrera, califs)
        alumnos_clase.append(estudiante)

    #Mostrar info de los alumnos
    if opcion == 2:
        matricula = int(input("Ingrese la matricula del alumno: "))
        encontrado = False
        for estudiante in alumnos_clase:
            if estudiante.matricula == matricula:
                estudiante.imprimir()
                encontrado = True
                break
        if not encontrado:
            print("Alumno no encontrado.")

    # Eliminar alumnos
    if opcion == 3:
        matricula = int(input("Ingrese la matricula del alumno que deseas eliminar: "))
        encontrado = False
        for estudiante in alumnos_clase:
            if estudiante.matricula == matricula:
                alumnos_clase.remove(estudiante)
                print("Alumno eliminado correctamente.")
                encontrado = True
                break
        if not encontrado:
            print("Alumno no encontrado, porfavor volver a intentarlo.")

    # Mostrar todos los alumnos
    if opcion == 4:
        if len(alumnos_clase) == 0:
            print("No hay ningun alumno registrado, favor de intentarlo nuevamente.")
        else:
            print("Lista de todos alumnos registrados:")
            for estudiante in alumnos_clase:
                estudiante.imprimir()

    if opcion == 5:
        break

