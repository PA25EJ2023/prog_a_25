class Repositorio:
    def __init__(self,):#lista de alumnos y los atributos lo que se hara con atributos
        pass
    def agrega_Alumno(self):
        pass
    def mostrar_Alumno(self):
        pass
    def mostrar_todos(self):
        pass
class Alumno:
    def __init__(self, nombre,matricula, carrera, calificaciones):
        self.nombre=nombre
        self.matricula=matricula
        self.carrera=carrera
        self.calificaciones=calificaciones

    def imprimir_info(self):
        print(f'El nombre del alumno es: {self.nombre}')
        print(f'La matricula del alumno es: {self.matricula}')
        print(f'La carrera del alumno es: {self.carrera}')
        print(f'Las calificaciones del alumno son: {self.calificaciones}')
    def calcular_promedio(self):

        promedio=sum(self.calificaciones)/len(self.calificaciones)
        print(f'El promedio es: {promedio}')