class Alumno:
    def __init__(self,matricula,nombre,carrera,calificaciones):
        self.matricula = matricula
        self.nombre = nombre
        self.carrera = carrera
        self.calificaciones = calificaciones


    def imprimir_info(self): 
        print(f"Matricula: {self.matricula} \n Nombre: {self.nombre} \n Carrera {self.carrera} \nCalificaciones: {self.calificaciones}")

    def calcular_promedio(self):
        print("El promedio final es:")



