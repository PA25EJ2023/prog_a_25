
class Alumno:
    def __init__(self,matricula,nombre,carrera,calificaciones):
        self.matricula = matricula
        self.nombre = nombre
        self.carrera = carrera
        self.calificaciones = calificaciones
        

    def imprimir_info(self):
        print(f"Matricula: {self.matricula}\nNombre: {self.nombre}\nCarrera: {self.carrera}\nPromedio: {self.calcular_promedio()} ")

    def calcular_promedio(self):
        promedio = 0
        for calificacion in self.calificaciones:
            promedio += calificacion
            promedio/=len(self.calificaciones)
            return promedio
        

class Repositorio:

    def Eliminar_alumno(self):
        pass
        
    


