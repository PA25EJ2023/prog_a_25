from clase_alumno import Alumno 
calificaciones=[] #crear lista vacia 
alumnos=[] 

 
print(" -- MENU DE OPCIONES FACPYA --") 
while True: 
    print("1. Agregar alumno") 
    print("2. Mostrar info del alumno") 
    print("3. Eliminar alumno: ") 
    print("4. Mostrar todos los alumnos: ") 
    print("5. Salir") 
    opcion=int(input("Bienvenido(a) ¿qué opcion desea realizar? ")) 
    if opcion==1: 
        mat=int(input("Ingrese la matricula del alumno: ")) #CREAR UN ALUMNO Y DE AHI MANDAR LAS CALIFICACIONES PARA LA LISTA 
        nom=input("Ingrese el nombre del alumno: ") 
        carr=input("Ingrese la carrera: ") 
        cal=int(input("Ingrese la calificacion: "))  
        #while True:  
            #calificaciones.append(objeto) 
            
        objeto=Alumno(mat,nom,carr,cal) #calificaciones.append(objeto) 
        alumnos.append(objeto) 

    elif opcion==2: 
        nom=input("Ingrese el nombre de quien desea obtener información: ") 
        for objeto in alumnos: 
            if objeto.nombre==nom: 
                objeto.imprimir_info() 

 


 
        
        

 

 

 