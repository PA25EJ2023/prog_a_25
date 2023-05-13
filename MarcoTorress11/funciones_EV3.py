#FUNCIONA
class Alumno:
    def __init__(self, mat, nombre, carrera, promedio):
        self.mat = mat
        self.nombre = nombre
        self.carrera = carrera
        self.promedio = promedio
    
    def mostrar_info_alumno(self):    
        print(f"Matricula: {self.mat}")
        print(f"Nombre del alumno: {self.nombre}")
        print(f"Carrera: {self.carrera}")
        print (f"El promedio del alumno es de: {self.promedio}")
    
    def eliminar_alumno(self, lista_alumnos):
        for i, alum in enumerate(lista_alumnos):
            if alum.mat == self.mat:
                del lista_alumnos[i]
                break

def crear_alumno():
    matricula = input("Ingrese la matricula del alumno: ")
    nombre = input("Ingrese el nombre del alumno: ")
    carrera = input("Ingrese la carrera del alumno: ")
    cantidad = int((input("Ingresa la cantidad de calificaciones que quieres ingresar: ")))
    for i in range(1,cantidad + 1):
        calificacion = int(input(f"Ingresa calificación {i}: "))
        calificaciones.append(calificacion)
        prom = sacar_promedio()
    alum = Alumno(matricula, nombre, carrera, prom)
    alumnos.append(alum)
    print("Alumno creado exitosamente!")

def sacar_promedio():
    promedio = sum(calificaciones)/len(calificaciones)
    return promedio


def mostrar_info_del_alumno():
    mat = input("Ingrese la matricula del alumno: ")
    alumno_encontrada = False
    for alum in alumnos:
        if alum.mat == mat:
            alum.mostrar_info_alumno()
            alumno_encontrada = True
            break
    if not alumno_encontrada:
        print("No existe un alumno con la matricula ingresada")

def eliminar_alumno():
    mat = input("Ingrese la matricula del alumno que desea eliminar: ")
    alumno_encontrado = False
    for alum in alumnos:
        if alum.mat == mat:
            alum.eliminar_alumno(alumnos)
            alumno_encontrado = True
            print("Alumno eliminado exitosamente!")
            break
    if not alumno_encontrado:
        print("No existe un alumno con la matricula ingresada")

def mostrar_alumnos():
    if len(alumnos) == 0:
        print("No hay alumnos registrados.")
    else:
        print("Información de todos los alumnos:")
        for alum in alumnos:
            alum.mostrar_info_alumno()

calificaciones = []
alumnos = []