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
        calificacion = float(input("Dime la calificacion: {}".format(i+1)))
        calificaciones.append(calificacion)
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
        print("No coincide la matricula con ningun estudiante")

def mostrar_info_alumno():
    matricula = input("Dime la matricula del estudiante: ")
    alum_enc = False
    for alumno in alumnos:
        if alumno.matricula == matricula:
            alumno.info()
            alum_enc = True
            break
    if not alum_enc:
        print("No se encontró un alumno con esa estudiante. ")

def mostrar_todos_alumnos():
    if len(alumnos) == 0:
        print("Aun no hay alumnos registrados")
    else:
        for alumno in alumnos:
            alumno.info()
            print()

resp = -1

while resp != 6:
    print("1. Agregar un estudiante\n 2. Mostrar informacion del estudiante\n 3. Eliminar algun estudiante\n 4. Mostrar a todos los estudiantes\n 5. Salir del programa")
    resp = int(input("Elige una respuesta en base al menu: "))

    if resp == 1:
        agregar_alumno()
    elif resp == 2:
        mostrar_info_alumno()
    elif resp == 3:
        eliminar_alumno()
    elif resp == 4:
        mostrar_todos_alumnos()
    elif resp == 5:
        print("Que tenga excelente dia :)")
print("Que tenga excelente dia :)")