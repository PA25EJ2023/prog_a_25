
class Alumno:
    def __init__(self,matricula,nombre,carrera,calificaciones):
        self.matricula = matricula
        self.nombre = nombre
        self.carrera = carrera
        self.calificaciones = calificaciones
        

    def imprimir_info(self):
        print(f"Matricula: {self.matricula}\nNombre: {self.nombre}\nCarrera: {self.carrera}\nPromedio: {self.calcular_promedio()} ")

    def calcular_promedio(self):
        suma_calif = 0
        for calificacion in self.calificaciones:
            suma_calif += calificacion
        promedio = suma_calif / len(self.calificaciones)
        return promedio
        
    


