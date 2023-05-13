class Alumno:
    def __init__(self,matricula,nombre,carrera,califs):
        self.matricula = matricula
        self.nombre = nombre
        self.carrera = carrera
        self.califs = califs

    def imprimir_info(self):
        
        print(f'Matricula:{self.matricula}')
        print(f'Nombre:{self.nombre}')
        print(f'Carrera:{self.carrera}')
        print(f'Calificaciones:{self.califs}')

    def calcular_promedio(self):

        promedio=sum(self.califs)/len(self.califs)   
        print(f"Promedio:{promedio}")

    def mostrar_alumnos(self):
        print(f'Matricula:{self.matricula}')
        print(f'Nombre:{self.nombre}')
        print(f'Carrera:{self.carrera}')
        print(f'Calificaciones:{self.califs}')
