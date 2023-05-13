from clase_alumno import Alumno
alumnos = []

while True:
    print("1-Agregar Alumno\n2-Mostrar informacion del alumno\n3-Eliminar alumno\n4-Mostrar todos los alumnos\n5-Salir")

    op = int(input("Ingrese opcion: "))

    if op == 1:
        matricula = int(input("Ingrese la matricula: "))
        nombre = input("Ingrese el nombre: ")
        carrera = input("Ingrese la carrera: ")
        cantidad_materias = int(input("Cuantas materias lleva el alumno: "))
        califs = []
        for i in range(cantidad_materias):
            calificacion = float(input("Calificacion: "))
            califs.append(calificacion)
                
        estudiante = Alumno(matricula, nombre, carrera, califs)
        alumnos.append(estudiante)

    
    if op == 2:
        matricula = int(input("Ingrese la matricula del alumno: "))
        for estudiante in alumnos:
            if estudiante.matricula == matricula:
                estudiante.mostrar_info()

    
    if op == 3:
            matricula = int(input("Ingresa la matricula del alumno que deseas eliminar: "))
            for estudiante in alumnos:
                if estudiante.matricula == matricula:
                    alumnos.remove(estudiante)

    
    if op == 4:
        for estudiante in alumnos:
            estudiante.mostrar_info()

    
    if op == 5:
        print("Adios")
        break

