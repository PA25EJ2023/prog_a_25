class Alumno:
    def __init__(self, matricula, nombre, carrera, calificaciones):
        self.matricula = matricula
        self.nombre = nombre
        self.carrera = carrera
        self.calificaciones = calificaciones

    def cal_prom(self):
        return sum(self.calificaciones) / len(self.calificaciones)

    def imprim_info(self):
        print(f"Matrícula: {self.matricula}")
        print(f"Nombre: {self.nombre}")
        print(f"Carrera: {self.carrera}")
        print(f"Calificaciones: {self.calificaciones}")
        print(f"Promedio: {self.cal_prom()}")