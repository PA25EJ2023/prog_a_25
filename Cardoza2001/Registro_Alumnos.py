
class Alumno:

        
    def __init__(self):
        self.Datos_Alumno= []
    
    def RegAlumno (self):
             
       A= self.Datos_Alumno 
       
        
       print ("Ingrese el nombre del alumno:")

       nombre= int(input())

       A.append(nombre)

       print ("Ingrese la matricula del alumno:")

       matricula= int(input())

       A.append(matricula)

       print ("Ingrese la calificacion del alumno:")

       self.calificación= int(input())

       A.append(self.calificacion)

       return A
