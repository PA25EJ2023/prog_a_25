from clase_ev_3 import Alumno
import time

alumnos = []
op= 0
print("Bienvenido al programa")
while op != 5:
    print("Opciones disponibles")
    print("1.-Agregar alumno\n 2.-Mostrar info alumno\n 3.-Eliminar alumno\n 4.-Mostrar todos los alumnos\n 5.-Salir")
    op = int(input("ingresa una opcion"))

    if op == 1:
        matricula = input("Ingresa la matricula")
        nombre = input("Ingresa tu nombre")
        carrera = input("Ingresa el nombre de tu carrera")
        print("Agregando datos")
        time.sleep(3)
        calificaciones = []
        num_cali = int(input("Cuantas calificaciones tiene el alumno"))
        for i in range (num_cali):
            nota = float(input("Ingresa tu calificaion"))
            calificaciones.append(nota)
        print("Agregando estudiante..........")
        time.sleep(3)
        estudiante = Alumno (matricula, nombre, carrera, calificaciones)
        alumnos.append(estudiante)
        print("Estudiante agregado correctamente")
        time.sleep(3)
    
    elif op == 2:
        print("Mostra la informacion del alumno")
        matricula = input("Ingresa la matricula del alumno")
        for estudiant in alumnos:
            if estudiante.matricula == matricula:
                estudiante.imprimir_info()
                break
            else:
                print("Estudiante no existente")
                print("Porfavor intente de nuevo")
    
    elif op == 3:
        print("Elmininando Alumno")
        matricula =input("Ingresa la matricula del alumno que desea eliminar")
        for estudiant in alumnos:
            if estudiante.matricula == matricula:
                alumnos.remove(estudiante)
                print("Alumno eliminado correctamente")
            else:
                print("Estudiante no existente")

    







