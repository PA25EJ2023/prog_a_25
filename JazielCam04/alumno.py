class Alumno:
    def __init__(self, matricula, nombre, carrera, calificaciones):
        self.matricula = matricula
        self.nombre = nombre
        self.carrera = carrera
        self.calificaciones = calificaciones

    def info(self):
        promedio = self.calcular_promedio()
        print("Tu matrícula:", self.matricula)
        print("Tu nombre:", self.nombre)
        print("Esta es tu carrera:", self.carrera)
        print("Estas son tus calificaciones:", self.calificaciones)
        print("Promedio:", promedio)

    def calcular_promedio(self):
        total_calificaciones = sum(self.calificaciones)
        promedio = total_calificaciones / len(self.calificaciones)
        return promedio
    
alumnos = []

def agregar_alumno():
    matricula = input("Dime la matricula del estudiante: ")
    nombre = input("Dime el nombre del estudiante: ")
    carrera = input("Dime el nombre de la carrera del estudiante: ")
    
    calificaciones = []
    can = int(input("Dime el numero de calificaciones: "))
    for i in range(can):
        calificaciones = float(input("Dime la calificacion: ".format(i+1)))
        calificaciones.append(calificaciones)
    alumno = Alumno(matricula, nombre, carrera, calificaciones)
    alumnos.append(alumno)
    print("Alumno agregado con exito.")

def eliminar_alumno():
    matricula = input("Dame la matricula de que alumno deseas eliminar: ")
    alum_enc = False
    for alumno in alumnos:
        if alumno.matricula == matricula:
            alumnos.remove(alumno)
            alum_enc = True
            break
    if alum_enc:
        print("Fue eliminado...")
    else:
        print("No coincide la matricula con ningun alumno")

def mostrar_info_alumno():
    matricula = input("Dime la matricula del alumno: ")
    alum_enc = False
    for alumno in alumnos:
        if alumno.matricula == matricula:
            alumno.info()
            alum_enc = True
            break
    if not alum_enc:
        print("No se encontró un alumno con esa matrícula. ")
