class Alumno:
    def __init__(self,nombre,matricula,carrera,calificacion):
        self.nombre = nombre
        self.matricula = matricula 
        self.carrera = carrera
        self.calificacion = calificacion

    def imprimir_info(self):
        print(f'Nombre: {self.nombre}\n Matricula: {self.matricula}\n Calificaciones: {self.calificacion}\n Carrera: {self.carrera} ')

    def calcular_promedio(self):
        return sum(self.calificacion) / len(self.calificacion)
    
