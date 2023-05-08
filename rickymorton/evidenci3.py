from clase_ev_3 import Alumno
import time

alumnos = []

print("Bienvenido al programa")
op= 0
while op != 5:
    print("Opciones disponibles")
    print("1.-Agregar alumno\n 2.-Mostrar info alumno\n 3.-Eliminar alumno\n 4.-Mostrar todos los alumnos\n 5.-Salir")
    op = int(input("ingresa una opcion"))

    if op == 1:
        matricula = input("Ingresa la matricula")
        nombre = input("Ingresa tu nombre")
        carrera = input("Ingresa el nombre de tu carrera")
        calificaciones = []
        num_cali = int(input("Cuantas calificaciones tiene el alumno"))
        for i in range (num_cali):
            nota = int(input("Ingresa tu calificaion"))
            calificaciones.append(nota)
        print("Agregando estudiante..........")
        time.sleep(3)
        estudiante = Alumno(matricula,nombre,carrera,calificaciones)
        alumnos.append(estudiante)




