class Alumno:
    def __init__(self, matricula, nombre, carrera, calificaciones):
        self.matricula = matricula
        self.nombre = nombre
        self.carrera = carrera
        self.calificaciones = calificaciones
    
    def mostrar_info_alumno(self):
        print(f"Matricula: {self.matricula}")
        print(f"Nombre del alumno: {self.nombre}")
        print(f"Carrera: {self.carrera}")
        print(f"El promedio del alumno es: {self.calificaciones}")


def crear_alumno():
    matricula = input("Ingrese la matricula del alumno: ")
    nombre = input("Ingrese el nombre del alumno: ")
    carrera = input("Ingrese la carrera del alumno: ")
    cantidad = int(input("Ingresa la cantidad de calificaciones que quieres ingresar: "))
    x = 1
    y = 0
    while y < cantidad:
        calificacion = int(input(f"Ingresa calificación {x}: "))
        x+=1
        y+=1
    calif.append(calificacion)
    calificaciones = sum(calificacion)/len(calificacion)
    alum = Alumno(matricula, nombre, carrera, calificaciones)
    alumnos.append(alum)
    print("alumno agregado exitosamente.")


def mostrar_info_alumno():
    matricula = input("Ingrese el número de alum: ")
    alum_encontrada = False
    for alum in alumnos:
        if alum.matricula == matricula:
            alum.mostrar_info_alumno()
            alum_encontrada = True
            break
    if not alum_encontrada:
        print("No existe una alumno con el número de matricula ingresado.")


def mostrar_alumnos():
    if len(alumnos) == 0:
        print("No hay alumnos creados.")
    else:
        print("Información de todos los alumnos:")
        for alum in alumnos:
            alum.mostrar_info_alumno()

alumnos = []
calif = []

opcion = 0 
while opcion !=4 :
    print("¡Bienvenido al sistema del alumnado!")
    print("Seleccione una opción del menú:")
    print("1. Crear Alumno")
    print("2. Mostrar información de alumno")
    print("3. Mostrar todos los alumnos")
    print("4. Salir")

    opcion = input("Ingrese el número de la opción deseada: ")

    if opcion == "1":
        crear_alumno()
    elif opcion == "2":
        mostrar_info_alumno()
        input("Presiona enter para continuar...")
    elif opcion == "3":
        mostrar_alumnos()
        input("Presiona enter para continuar...")
    elif opcion == "4":
        print("Gracias por utilizar el sistema de alumnado. ¡Hasta luego!")
        break
    else:
        print("Opción inválida. Por favor, ingrese una opción válida del menú.")
