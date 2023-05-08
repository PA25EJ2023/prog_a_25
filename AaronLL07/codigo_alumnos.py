from clase_alumnos import Alumno

alumnos = []

op = -1
print("¡Bienvenido!")
while op != 5:
    print(14*"*", "MENU", 14*"*")
    print("1.- Agregar alumno\n2.- Mostrar información del alumno\n3.- Eliminar alumno\n Mostrar todos los alumnos\n5.- Salir")
    op = int(input("Indique una opcion: "))
    # 
    if op == 1:
        califs = []
        matricula = int(input("Ingrese la matricula del alumno: "))
        nombre = input("Ingrese el nombre del alumno: ")
        carrera = input("Ingrese la carrera del alumno: ")
        ag_mas = "S"
        while ag_mas.upper() == "S": # Este ciclo es para pedir las calificaciones e ir agregandolas a la lista
            cal = float(input("Ingrese la calificación: "))
            califs.append(cal)
            ag_mas = input("Desea agregar una calificación más (S/N): ")
        # Se crea un Alumno y se le agregan todos los datos
        estudiante = Alumno(matricula, nombre, carrera, califs)
        alumnos.append(estudiante)
    
    elif op == 2:
        matricula = int(input("Ingrese la matrícula del alumno para mostrar su información: "))
        for estudiante in alumnos:
            if estudiante.matricula == matricula:
                estudiante.info_alum()

    elif op == 3:
        pass