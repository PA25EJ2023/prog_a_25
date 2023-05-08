from clasesev3 import Alumno,Repositorio

op=1
lista_alumnos=[]
calificaciones=[]
while op!=5:     
    print('***MENU***')
    print('1. Agregar Alumno')
    print('2. Mostrar informacion de alumno')
    print('3. Eliminar Alumno')
    print('4. Mostrar todos los alumnos')
    print('5. Salir')
    op=int(input('Que desea hacer?'))

    if op==1:
        nombre=input('Nombre del Alumno: ')
        matricula=int(input('Matricula del Alumno: '))
        carrera=input("Carrera del Alumno: ")
        calificacion=100
        while calificacion!=0:
            calificacion=int(input("calificaciones del alumno: (0 cuando ya no haya mas)"))
            if calificacion!=0:
                calificaciones.append(calificacion)
        alumnon=Alumno(nombre,matricula,carrera,calificaciones)
        lista_alumnos.append(alumnon)
        calificaciones=[]
    elif op==2:
        alumnon.imprimir_info()
        alumnon.calcular_promedio()
    elif op==3:
        borrar=int(input(f'Cual es la matricula del alumno que desea borrar'))
        if borrar==matricula:
            pass        
    elif op==4:
        if len(lista_alumnos) == 0:
            print("No hay alumnos ")
        else:
            print("Información de todas las cuentas:")
            for alumnon in lista_alumnos:
                    alumnon.imprimir_info()
                    promedio=alumnon.calcular_promedio()
