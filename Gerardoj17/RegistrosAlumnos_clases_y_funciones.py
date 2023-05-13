class Alumno:
    def __init__(self,matricula,nombre,carrera,calificaciones):
        self.matricula = matricula
        self.nombre = nombre
        self.carrera = carrera
        self.calificaciones = calificaciones


    def imprimir_info(self):
        print(f'Matricula:{self.matricula}')
        print(f'Nombre:{self.nombre}')
        print(f'Carrera:{self.carrera}')
        print(f'Promedio:{self.calcular_promedio()}')

    def calcular_promedio(self):
        return sum(self.calificaciones) / len(self.calificaciones)
        
   
     
alumnos = []
         
def agregar_alumno():
    matricula = input('ingresa tu matricula: ')
    nombre = input('Ingresa tu nombre: ')
    carrera = input('Ingresa tu carrera: ')
    calificaciones = []
    while True:
        calificacion = input('Ingresa solo una calificacion y presiona enter. (Deja el espacio en blanco y presiona ENTER para terminar): ')
        if not calificacion:
            break
        calificaciones.append(float(calificacion))
    alumno = Alumno(matricula, nombre, carrera, calificaciones)
    alumnos.append(alumno)



def mostrar_info():
    matricula = input('Ingresa la matricula del alumno que deseas ver la información: ')
    for alumno in alumnos:
        if alumno.matricula == matricula:
            alumno.imprimir_info()
            return
        else:
            print('Alumno no encontrado')
        

def eliminar_alumno():
    matricula = input('Ingrese la matricula del alumno que desea eliminar: ')
    for alumno in alumnos:
        if alumno.matricula == matricula:
            alumnos.remove(alumno)
            print('Alumno eliminado')
            return
        else:
            print('alumno no encontrado')
        

def mostrar_info_de_todos_alumnos():
    for alumno in alumnos:
        alumno.imprimir_info()
        print()
             
             
def iniciar_programa():
    while True:
        print('1.Agregar alumno\n2.Mostrar informacion del alumno\n3.Eliminar alumno\n4.Mostrar todos los alumnos\n5.Salir')
        opcion = int(input('Elige una opción: '))
        if opcion == 1:
            agregar_alumno()
        elif opcion == 2:
            mostrar_info()
        elif opcion == 3:
            eliminar_alumno()
        elif opcion == 4:
            mostrar_info_de_todos_alumnos()
        elif opcion == 5:
            print('Gracias por usar el programa')
            break
    

        
