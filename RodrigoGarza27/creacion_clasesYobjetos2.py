class Alumno:
    def __init__(self, matricula, nombre, carrera, calificaciones):
        self.matricula = matricula
        self.nombre = nombre
        self.carrera = carrera
        self.calificaciones = calificaciones

    def imprimir_info(self):
        print("Matrícula: ", self.matricula)
        print("Nombre: ", self.nombre)
        print("Carrera: ", self.carrera)
        print("Calificaciones: ", self.calificaciones)
        print("Promedio: ", self.calcular_promedio())

    def calcular_promedio(self):
        if len(self.calificaciones) > 0:
            return sum(self.calificaciones) / len(self.calificaciones)
        else:
            return 0.0

alumnos = []

while True:
    print("1.- Agregar Alumno")
    print("2.- Mostrar info del alumno")
    print("3.- Eliminar alumno")
    print("4.- Mostrar todos los alumnos")
    print("5.- Salir")

    opcion = input("Ingrese una opción (1-5): ")

    if opcion == "1":
        print("Ingrese la información del alumno:")
        matricula = input("Matrícula: ")
        nombre = input("Nombre: ")
        carrera = input("Carrera: ")
        calificaciones = input("Calificaciones (separadas por comas): ")
        calificaciones = [float(c) for c in calificaciones.split(",")]
        alumno = Alumno(matricula, nombre, carrera, calificaciones)
        alumnos.append(alumno)
        print("Alumno agregado correctamente")

    elif opcion == "2":
        matricula = input("Ingrese la matrícula del alumno: ")
        encontrado = False
        for alumno in alumnos:
            if alumno.matricula == matricula:
                alumno.imprimir_info()
                encontrado = True
                break
        if not encontrado:
            print("Alumno no encontrado")

    elif opcion == "3":
        matricula = input("Ingrese la matrícula del alumno a eliminar: ")
        eliminado = False
        for i, alumno in enumerate(alumnos):
            if alumno.matricula == matricula:
                del alumnos[i]
                eliminado = True
                break
        if eliminado:
            print("Alumno eliminado")
        else:
            print("No se encontro alumno")

    elif opcion == "4":
        print("Lista de alumnos:")
        for alumno in alumnos:
            alumno.imprimir_info()

    elif opcion == "5":
        print("Saliendo...")
        break

    else:
        print("Verifique su respuesta")
