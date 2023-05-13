from Evidencia3 import Alumnos

alumnos = []

while True:
    print("Menu")
    print(f'1.- Agregar Alumno\n 2.- Mostrar info del alumno\n 3.- Eliminar alumno\n 4.- Mostrar todos los alumnos\n 5.- Salir')

if opcion == 1:
    opcion = int(input("Seleccione una opción del menu: "))

    matricula = input("Ingrese la matrícula: ")
    nombre = input("Ingrese el nombre: ")
    carrera = input("Ingrese la carrera: ")
    calificaciones = []
    n = int(input("¿Cuántas calificaciones quiere ingresar? "))
    for i in range(n):
        calificacion = float(input(f"Ingrese la calificación {i+1}: "))
        calificaciones.append(calificacion)
    alumno = Alumnos(matricula, nombre, carrera, calificaciones)
    alumnos.append(alumno)
    print("Alumno agregado")

    matricula = input("Ingrese la matrícula: ")
    encontrado = False
    for alumno in alumnos:
        if alumno.matricula == matricula:
            alumno.imprimir_info()
            encontrado = True
            break
    if not encontrado:
        print("No se encontró ningún alumno.")

if opcion == 2:
    matricula = input("Ingrese la matrícula: ")
    encontrado = False
    for alumno in alumnos:
        if alumno.matricula == matricula:
            alumno.imprimir_info()
            encontrado = True
            break
    if not encontrado:
        print("No se encontró ningún alumno")

if opcion == 3:
    matricula = input("Ingrese la matrícula del alumno a eliminar: ")
    eliminado = False
    for i, alumno in enumerate(alumnos):
        if alumno.matricula == matricula:
            del alumnos[i]
            eliminado = True
            print("Alumno eliminado")
            break
    if not eliminado:
        print("No se encontró ningún alumno")

if opcion == 4:
     if len(alumnos) > 0:
        for alumno in alumnos:
            alumno.imprimir_info()
            
        else:
            print("No hay alumnos registrados.")

if opcion == 5:
    while True:
        print("Menu")
        print(f'1.- Agregar Alumno\n 2.- Mostrar info del alumno\n 3.- Eliminar alumno\n 4.- Mostrar todos los alumnos\n 5.- Salir')
    
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            agregar_alumno()
        elif opcion == "2":
           mostrar_info()
        elif opcion == "3":
            eliminar_alumno()
        elif opcion == "4":
            mostrar_todos()

