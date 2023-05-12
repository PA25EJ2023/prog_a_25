from clase_alumno import Alumno

alumnos = []

while True:
    print("\nMenu de opciones")
    print("1.Agregar alumno\n2.Mostrar informacion del alumno\n3.Eliminar alumno\n4.Mostrar todos los alumnos\n5.Salir")
    opcion = int(input("Elige una opcion: "))
    if opcion == 1:
        matricula = input("Ingresa la matricula del alumno: ")
        nombre_alumno = input("Ingresa el nombre del alumno: ")
        carrera = input("Ingresa la carrera del alumno: ")
        calificaciones = []
        while True:
            calificacion = input("Ingresa una calificacion del alumno: ")
            calificaciones.append(float(calificacion))
            respuesta = input("Deseas ingresar otra calificacion\n1.SI\n2.NO\nRespuesta: ")
            if respuesta == "2":
                break
        alumno = Alumno(matricula,nombre_alumno,carrera,calificaciones)
        alumnos.append(alumno)
    elif opcion == 2:
        matricula = input("Ingresa la matricula del alumno: ")
        alumno_encontrado = False
        for alumno in alumnos:
            if alumno.matricula == matricula:
                alumno.imprimir_info()
                alumno_encontrado = True
        if not alumno_encontrado:
            print("Alumno no encontrado, intente nuevamente")
    elif opcion == 3:
        matricula = input("Ingresa la matricula del alumno que deseas borrar: ")
        alumno_encontrado = False
        for alumno in alumnos:
            if alumno.matricula == matricula:
                alumnos.remove(alumno)
                alumno_encontrado = True
                print("Alumno eliminado exitosamente")
        if not alumno_encontrado:
            print("Alumno no encontrado, intente nuevamente")
    elif opcion == 4:
        print("Alumnos ingresados")
        for alumno in alumnos:
            alumno.imprimir_info()
    elif opcion == 5:
        break