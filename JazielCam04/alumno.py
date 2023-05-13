class Alumno:
    def __init__(self, matricula, nombre, carrera, calificaciones):
        self.matricula = matricula
        self.nombre = nombre
        self.carrera = carrera
        self.calificaciones = calificaciones

    def imprimir_info(self):
        promedio = self.calcular_promedio()
        print("Matrícula:", self.matricula)
        print("Nombre:", self.nombre)
        print("Carrera:", self.carrera)
        print("Calificaciones:", self.calificaciones)
        print("Promedio:", promedio)

    def calcular_promedio(self):
        total_calificaciones = sum(self.calificaciones)
        promedio = total_calificaciones / len(self.calificaciones)
        return promedio
    