from ev3_progra import *

alumnos = []
calificaciones = []

opc= 0
while opc == 0:
    print("Menu de Opciones \n1.-Agregar alumno \n2.-Mostrar info del alumno \n3.-Eliminar alumno \n4.-Mostrar todos los alumnos \n5.-Salir")
    opc_menu=int(input("Ingrese su opcion: "))
    if opc_menu == 1:
        print("Agregar alumno")
        matricula=int(input("Ingrese la matricula del alumno: "))
        nombre = input("Ingrese el nombre del alumno: ")
        carrera= input("Ingrese la carrera a la que pertenece: ")
    
        num_cali = int(input("Ingrese el numero de calificaciones "))
        for i in range (num_cali):
            calificacion=int(input("Ingresa la calificacion: "))
            calificaciones.append(calificacion)
        alumno = Alumno (matricula,nombre,carrera,calificaciones)
        alumnos.append(alumno)
        print("***Alumno agregado***")
        alumno.imprimir_info()

    elif opc_menu == 2:
        print("Mostrar info del alumno")
        matricula =int(input("Ingrese la matricula del alumno: "))

        for alumno in alumnos:
            if alumno.matricula == matricula:
                alumno.imprimir_info()
            else:
                print("***Alumno no encontrado***")

    elif opc_menu == 3:
        print("Eliminar alumno")
        matricula= int(input("Ingrese la matricula del alumno: "))

        for alumno in alumnos:
            if alumno.matricula == matricula:
                alumnos.remove(alumno)
                print("***Alumno eliminado exitosamente***")

            else:
                print("***Alumno  no encontrado***")

    elif opc_menu == 4:
        print("Mostrar todos los alumnos")
        for alumno in alumnos:
            if len (alumnos) > 0:
                alumno.imprimir_info()
            else:
                print("***No hay alumnos***")

    opc=int(input("Desea seguir utilizando el programa? 1.-Si 2.-No "))

