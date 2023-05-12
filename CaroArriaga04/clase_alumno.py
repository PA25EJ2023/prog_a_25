class Alumno:
    def __init__(self,matricula,nombre,carrera,calificaciones):
        self.matricula = matricula
        self.nombre = nombre
        self.carrera = carrera
        self.calificaciones = calificaciones
        
    def imprimir_info(self):
        print("\nAlumno")
        print(f"Matricula del alumno: {self.matricula}")
        print(f"Nombre del alumno: {self.nombre}")
        print(f"Carrera: {self.carrera}")
        print(f"Promedio del alumno: {self.calcular_promedio()}")
        
    def calcular_promedio(self):
        return sum(self.calificaciones) / len(self.calificaciones)