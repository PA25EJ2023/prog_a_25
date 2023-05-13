class Alumnos:
    def __init__(self, matricula, nombre, carrera, califs):
        self.matricula = matricula
        self.nombre = nombre
        self.carrera = carrera
        self.califs = califs
    
    def imprimir(self):
        print(21*"*")
        print(f"Matricula: {self.matricula}\nNombre: {self.nombre}\nCarrera: {self.carrera}\nCalificaciones: {self.califs}\nPromedio: {self.calcular_promedio()}")

    def calcular_promedio(self):
        promedio = sum(self.califs) / len(self.califs)
        return round(promedio, 2)
