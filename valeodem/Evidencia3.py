class Alumnos:
    def __init__(self,nombre,matricula,carrera,calif):
        self.nombre = nombre
        self.matricula = matricula 
        self.carrera = carrera
        self.calif = calif

    def imprimir_info(self):
        print(f'Nombre: {self.nombre}\n Matricula: {self.matricula}\n Carrera: {self.carrera}\n Calificaciones: {self.calif}')

    def calcular_promedio(self):
        return sum(self.calif) / len(self.calif)

        