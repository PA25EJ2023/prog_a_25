class Alumno:
    def __init__(self, matricula, nombre, carrera, califs = []):
        self.matricula = matricula
        self.nombre = nombre 
        self.carrera = carrera 
        self.califs = califs
      
    def mostrar_info(self):
        print(f"Matricula {self.matricula}, Nombre {self.nombre}, Carrera {self.carrera}, Promedio {self.calcular_promedio()}")

    
    def calcular_promedio(self):
        return sum(self.califs) / len(self.califs)