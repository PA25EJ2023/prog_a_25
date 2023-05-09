from evidencia_3_clases import Alumno

opcion = 1

lista_alumnos = []
while opcion ==1:
    respuesta = int(input("1.-Agregar Alumno\n2.-Mostrar info del alumno\n3.-Eliminar alumno\n4.-Mostrar todos los alumnos\n5.-Salir\nElija una opcion: "))
    if respuesta == 1:
        calificaciones = []
        nombre = input("Escriba su nombre: ")
        matricula = int(input("Digite su matricula: "))
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
        if info_alumno >0:
            for info_alumno in lista_alumnos:
                print(f"INFORMACIÓN DE LA MATRÍCULA: {info_alumno}")
                info_alumno.imprimir_info()
        else:
            print("LA MATRICULA NO EXISTE!")
    

    elif respuesta == 3:
        borrar = int(input("Digite la matricula del alumno que desea borrar: "))
        if borrar in lista_alumnos:
            lista_alumnos.remove("borrar")
            print("ALUMNO ELIMINADO")
        else:
            print("ERROR EN LA MATRICULA!")

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
         

             
             
             
        
        




         
         

    