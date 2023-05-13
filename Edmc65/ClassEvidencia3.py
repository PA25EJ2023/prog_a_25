class Alumno0:
    def __init__(self, Matricula, Nombre, Carrera,Promedio):
        self.Matricula = Matricula
        self.Nombre = Nombre
        self.Carrera = Carrera
        self.Promedio= Promedio

    def imprimir_info(self):
        print("Matricula del alumno: ", self.Matricula)
        print("Nombre del alumno: ", self.Nombre)
        print("Carrera cursante: ", self.Carrera)
        print("Promedio del alumno:", self.Promedio)


def Add_Alumno():
    Matricula = input("Ingrese la matricula: ")
    Nombre = input("Ingrese el nombre del alumno: ")
    Carrera = input("Carrera cursante: ")
    Materias= int(input("Materias cursadas: "))

    #CALCULAR PROMEDIO
    total_calf=0
    i=1
    while i <= Materias:
        Calf=float(input("Calificación por materia: "))
        total_calf += Calf
        i+=1
    Promedio = total_calf / Materias
    ######
    Alumno = Alumno0(Matricula, Nombre, Carrera, Promedio)
    Alumnos.append(Alumno)
    print("Alumno añadido correctamente")


def imprimir_info():
    Matricula = input("Ingrese la matricula el alumno: ")
    Alumno_encontrado = False
    for Alumno in Alumnos:
        if Alumno.Matricula == Matricula:
            Alumno.imprimir_info()
            Alumno_encontrado = True
            break
    if not Alumno_encontrado:
        print("Alumno inexistente")

def Mostrar_Alumnos():
    if len(Alumnos) == 0:
        print("Alumnos no disponibles")
    else:
        print("Información de todos los alumnos:")
        for Alumno in Alumnos:
            Alumno.imprimir_info()

Alumnos = []

def eliminar_alumno(Matricula, Alumnos):
    if Matricula in Alumnos:
        Alumnos.append("")
        print(f"El alumno con matrícula {Matricula} ha sido eliminado.")
    else:
        print(f"No se encontró ningún alumno con matrícula {Matricula}.")
