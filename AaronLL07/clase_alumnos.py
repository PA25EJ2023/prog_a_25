# clase de Alumno}
class Alumno:

    def __init__(self, matricula, nombre, carrera, califs=[]):
        self.matricula = matricula
        self.nombre = nombre
        self.carrera = carrera
        self.califs = califs

    def info_alum(self):
        print(21*"*")
        print(f"Matrícula: {self.matricula}\nNombre: {self.nombre}\nCarrera: {self.carrera}\nPromedio: {self.calcular_promedio()}")

    def calcular_promedio(self):
        sub_prom = sum(self.califs)
        prom_fin = (sub_prom/len(self.califs))
        return prom_fin
        
class Repositorio:
    pass