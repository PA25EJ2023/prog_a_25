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
        print(f"Calificacion(es): {self.calificaciones}") 
        #print(f"Su promedio es: {}") 
        

    def calcular_promedio(self,total_mat): 
        promedio=(self.calificaciones/self.total_mat) #len() para sacar el total 
        #print(f"Su promedio es: {}") 
        return promedio 