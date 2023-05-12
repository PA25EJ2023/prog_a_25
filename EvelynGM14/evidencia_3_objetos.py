from evidencia_3_clases import Alumno

opcion = 1

lista_alumnos = []
while opcion ==1:
    respuesta = int(input("1.-Agregar Alumno\n2.-Mostrar info del alumno\n3.-Eliminar alumno\n4.-Mostrar todos los alumnos\n5.-Salir\nElija una opcion: "))
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
        print("ALUMNO AGREGADO!")

    elif respuesta == 2:
        info_alumno = int(input("Digite la matricula del alumno: "))
        if alumno.matricula == info_alumno:
            print(f"INFORMACIÓN DEL ALUMNO CON MATRICULA: {info_alumno}")
            alumno.imprimir_info()
        else:
            print("ERROR EN LA MATRICULA O NO EXISTE!")
    

    elif respuesta == 3:
        matricula = int(input("Digite la matricula del alumno que desea borrar: "))
        for alumno in lista_alumnos:
            if alumno.matricula == matricula:
                lista_alumnos.remove(alumno)
                print("ALUMNO ELIMINADO")
                break
        else:
            print("ERROR EN LA MATRICULA O NO EXISTE!")

    elif respuesta == 4:
        print("---REGISTRO DE ALUMNOS---")
        if len(lista_alumnos) > 0:
            for alumno in lista_alumnos:
                alumno.imprimir_info()
                print("*"*25)
        else:
            print("NO SE ENCONTRARON ALUMNOS REGISTRADOS!")

    elif respuesta == 5:
        break
    else:
        print("OPCIÓN INVÁLIDA!")
         

             
             
             
        
        




         
         

    