class Alumno:
    def __init__(self, matricula, nombre, carrera, calificaciones):
        self.matricula = matricula
        self.nombre = nombre
        self.carrera = carrera
        self.calificaciones = calificaciones
        


    def info_alumno(self):
        print("Número de matricula: ", self.matricula)
        print("Nombre del alumno: ", self.nombre)
        print("Carrera: ", self.carrera)
        print("Sus calificaciones son las siguientes: ", self.calificaciones)
        print("Su promedio es de: ", self.promedio())

    def promedio(self):
        if len(self.calificaciones) > 0:
            return sum(self.calificaciones) / len(self.calificaciones)
        else:
            return 0




def agg_alumno():
    matricula = int(input("A continuación, ingrese el número de matricula del alumno: "))
    nombre = input("Ingrese el nombre del alumno: ")
    nombre = nombre.upper()
    carrera = input("Ingrese las siglas de la carrera que estudia el alumno: ")
    carrera = carrera.upper()
    calificaciones = int(input("¿Con cuántas calificaciones cuenta el alumno?"))
    calificaciones_alumno = []
    for i in range (1, calificaciones + 1):
        calificacion = input(f"Ingrese la calificación número {i}: ")
        calificaciones_alumno.append(float (calificacion))
    estudiante = Alumno(matricula, nombre, carrera, calificaciones_alumno,)
    alumnos.append(estudiante)
    print("")
    print("El alumno ha sido agregado exitosamente.")


def most_info_alumno():
    matricula = int(input("Ingrese el número de matricula del alumno que desea buscar: "))
    print("")
    alumno_encontrado = False
    for estudiante in alumnos:
        if estudiante.matricula == matricula:
            estudiante.info_alumno()
            alumno_encontrado = True
            break
    if not alumno_encontrado:
        print("")
        print("No existe alumno con el numero de matricula ingresado.")


def eliminar_alumno():
    matricula = int(input("Por favor, ingrese la matricula correspondiente al alumno que desea eliminar: "))
    print("")
    alumno_eliminado = False
    for estudiante in alumnos:
        if estudiante.matricula == matricula:
            alumnos.remove(estudiante)
            alumno_eliminado = True
            print("")
            print("El alumno ha sido eliminado de forma exitosa.")
            break

    if not alumno_eliminado:
        print("")
        print("Lo sentimos, no se ha encontrado ningún alumno con la matricula ingresada anteriormente.")

def most_todos_alumnos():
    if len(alumnos) > 0:
        for estudiante in alumnos:
            estudiante.info_alumno()
        
    else:
        print("Lo sentimos, no se han encontrado alumnos registrados.")
        
alumnos = []
