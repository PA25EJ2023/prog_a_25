from clase_alumno import Alumno 
alumnos=[] #crear lista vacia , calificaciones y alumnos

print("-- MENU DE OPCIONES FACPYA --") 
while True: 
    print("1. Agregar alumno") 
    print("2. Mostrar info del alumno") 
    print("3. Eliminar alumno") 
    print("4. Mostrar todos los alumnos") 
    print("5. Salir") 
    opcion=int(input("Bienvenido(a) ¿qué opcion desea realizar? ")) 
    
    if opcion==1: 
        mat=int(input("Ingrese la matricula del alumno: ")) #CREAR UN ALUMNO Y DE AHI MANDAR LAS CALIFICACIONES PARA LA LISTA 
        nom=input("Ingrese el nombre del alumno: ") 
        carr=input("Ingrese la carrera: ") 
        calificaciones=[]

        while True:
                cal=float(input("Ingrese la calificacion: "))
                calificaciones.append(cal)
                op=int(input("¿Desea ingresar otra calificacion? 1-Si 2-No: "))
                if op==1:
                    pass
                elif op==2:
                    break 
      
        objeto=Alumno(mat,nom,carr,calificaciones)
        alumnos.append(objeto)
        print(f"Alumno {nom} agregado")
        calificaciones=[] 
        #print(f"Su promedio es: {objeto.calcular_promedio}")

    elif opcion==2: 
        nom=input("Ingrese el nombre de quien desea obtener información: ") 
        print(f"Informacion de {nom}")
        for objeto in alumnos: 
            if objeto.nombre==nom:
                objeto.imprimir_info()
                
            else:
                print("{nom} no se encontró")

    elif opcion==3: 
        mat=int(input("Ingrese la matricula del alumno que desea eliminar: ")) 
        for i in range(len(objeto)): 
            if objeto.matricula==mat:
                a=alumnos.pop(i) #eliminar el objeto de la lista 
                print(f"Alumno {a.matricula} eliminado")
                break  #para salir del ciclo for
        else:
            print(f"No se encontró un alumno con la matrícula {mat}")
      
    elif opcion==4: 
        for objeto in alumnos: 
            objeto.imprimir_info() 

    elif opcion==5: 
        print("Has salido del menu") 
        break  
 
    else: 
        print("Intente nuevamente, la opcion agregada no existe") 

 
 

 


 

    
 


 
        
        

 

 

 