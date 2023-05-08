class Alumno:
    def __init__(self,matricula,nombre,carrera,calificaciones):
        self.matricula = matricula
        self.nombre = nombre
        self.carrera = carrera
        self.calificaciones = calificaciones
    
    def imprimir_info(self):
        print(f'Matricula: {self.matricula}\n Nombre: {self.nombre}\n Carrera: {self.carrera}\n Calificaciones = {self.calificaciones}')

    def calcular_promedio(self):
        return sum(self.calificaciones)/ len(self.calificaciones)

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
        num_cali = input("Cuantas calificaciones tiene el alumno")

