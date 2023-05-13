class Alumno:
    def __init__(self,matricula,nombre,carrera,calificaciones): 
        self.matricula=matricula 
        self.nombre=nombre 
        self.carrera=carrera 
        self.calificaciones=calificaciones 


    def calcular_promedio(self):
        prom=sum(self.calificaciones)/len(self.calificaciones)
        return prom
        #return prom #usar len() para sacar el total 
        
    def imprimir_info(self): 
        print(f"Matricula: {self.matricula}") 
        print(f"Nombre: {self.nombre}") #AQUI HACER UNA LIST, USAR CICLO HAY UNA FUNCION Q SUMA LAS CALIFICACIONES 
        print(f"Carrera: {self.carrera}") 
        print(f"Calificaciones: {self.calificaciones}")  #print(f"Promedio: {sum(self.calificaciones)/len(self.calificaciones)}") 
        print(f"Promedio: {self.calcular_promedio()}")
