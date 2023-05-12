class Alumno:
    def __init__(self,matricula,nombre,carrera,calificaciones):
        self.matricula = matricula
        self.nombre = nombre
        self.carrera = carrera
        self.calificaciones = calificaciones
    
    def imprimir_info(self):
        promedio = self.calcular_promedio()
        print(f'Matricula: {self.matricula}\n Nombre: {self.nombre}\n Carrera: {self.carrera}\n Calificaciones = {self.calificaciones}\n Promedio: {promedio}')

    def calcular_promedio(self):
        return sum(self.calificaciones)/ len(self.calificaciones)