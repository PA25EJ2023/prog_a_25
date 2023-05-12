from evidencia_3_clases import Alumno

opcion = 1

lista_alumnos = []
while opcion ==1:
    print("-"*30)
    print("             MENÚ             ")
    print("-"*30)
    print("1.-Agregar Alumno\n2.-Mostrar info del alumno\n3.-Eliminar alumno\n4.-Mostrar todos los alumnos\n5.-Salir")
    print("-"*30)
    respuesta = int(input("Elija una opcion: "))
    if respuesta == 1:
        calificaciones = []
        matricula = int(input("Digite su matricula: "))
        nombre = input("Escriba su nombre: ")
        carrera = input("Escriba su carrera: ")
        no_calif = int(input("Digite la cantidad de calificaciones: "))
        for i in range(no_calif):
                calificacion = float(input(f"Digite una calificación: "))
                calificaciones.append(calificacion)
        alumno = Alumno(matricula,nombre,carrera,calificaciones)
        lista_alumnos.append(alumno)
        print("")
        print("ALUMNO AGREGADO!")
        print("")

    elif respuesta == 2:
        info_alumno = int(input("Digite la matricula del alumno: "))
        if alumno.matricula == info_alumno:
            print("*"*40)
            print(f"INFORMACIÓN DEL ALUMNO CON MATRICULA: {info_alumno}")
            alumno.imprimir_info()
            print("*"*40)
        else:
            print("")
            print("ERROR EN LA MATRICULA O NO EXISTE!")
            print("")
    

    elif respuesta == 3:
        matricula = int(input("Digite la matricula del alumno que desea borrar: "))
        for alumno in lista_alumnos:
            if alumno.matricula == matricula:
                lista_alumnos.remove(alumno)
                print("*"*25)
                print("ALUMNO ELIMINADO")
                print("*"*25)
                break
        else:
            print("")
            print("ERROR EN LA MATRICULA O NO EXISTE!")
            print("")

    elif respuesta == 4:
        if len(lista_alumnos) > 0:
            print("")
            print("-"*41)
            print("            REGISTRO DE ALUMNOS            ")
            print("-"*41)
            for alumno in lista_alumnos:
                alumno.imprimir_info()
                print("*"*40)
            print("-"*40)
            print("")
        else:
            print("")
            print("NO SE ENCONTRARON ALUMNOS REGISTRADOS!")
            print("")

    elif respuesta == 5:
        break
    else:
        print("")
        print("OPCIÓN INVÁLIDA!")
        print("")
         

             
             
             
        
        




         
         

    