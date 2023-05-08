from evidencia_3_clases import Alumno,Repositorio

opcion = 1
lista_alumnos = []

while opcion == 1:
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

    elif respuesta == 2:
        alumno = int(input("Digite la matricula del alumno: "))
        for alumno in lista_alumnos:
            alumno.imprimir_info()

    elif respuesta == 3:
         borrar = int(input("Digite la matricula del alumno que desea borrar: "))
         for borrar in lista_alumnos:
            lista_alumnos.remove(borrar)
             
             
             
        
        




         
         

    