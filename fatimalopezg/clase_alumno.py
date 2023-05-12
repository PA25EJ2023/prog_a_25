class Alumno:
    def __init__(self,matricula,nombre,carrera,calificaciones): 
        self.matricula=matricula 
        self.nombre=nombre 
        self.carrera=carrera 
        self.calificaciones=calificaciones 
        
        
    def imprimir_info(self): 
        print(f"Matricula: {self.matricula}") 
        print(f"Nombre: {self.nombre}") #AQUI HACER UNA LIST, USAR CICLO HAY UNA FUNCION Q SUMA LAS CALIFICACIONES 
        print(f"Carrera: {self.carrera}") 
        print(f"Promedio: {calcular_promedio()}")  #print(f"Promedio: {sum(self.calificaciones)/len(self.calificaciones)}") 

        

    def calcular_promedio(self):
        prom=sum(self.calificaciones)/len(self.calificaciones) #usar len() para sacar el total 
        #print(f"Promedio final: {}") 
        return prom