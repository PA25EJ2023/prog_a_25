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
        print("A continuación ingrese las calificaciones para calcular el promedio")
        t=int(input("Ingrese el total de materias: "))  
        total=0
        i=1
        while i<=t:
            calificaciones=float(input("Ingrese la calificacion: "))
            total+=calificaciones#contador
            i+=1
            promedio=total/t
            
            if t:
                print("opcion no valida")
                                #calificaciones.append(objeto) 
            objeto=Alumno(mat,nom,carr,calificaciones) #calificaciones.append(objeto) 
            alumnos.append(objeto) 

    elif opcion==2: 
        nom=input("Ingrese el nombre de quien desea obtener información: ") 
        print(f"Informacion del alumno {nom}")
        for objeto in alumnos: 
            if objeto.nombre==nom: 
                objeto.imprimir_info() 

    #elif opcion==3: 
        #mat=int(input("Ingrese la matricula del alumno que desea eliminar: ")) 
        #if matricula==mat: 
            #objeto.remove()==Alumno(mat)
      
            
    elif opcion==4: 
        for objeto in alumnos: 
            objeto.imprimir_info() 

    elif opcion==5: 
        print("Has salido del menu") 
        break  
 
    else: 
        print("Intente nuevamente, la opcion agregada no existe") 

 
 

 

 

 

    
 


 
        
        

 

 

 