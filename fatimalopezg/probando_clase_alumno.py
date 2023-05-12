from clase_alumno import Alumno 
calificaciones=[] #crear lista vacia , calificaciones
alumnos=[] 


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
        cal=float(input("Ingrese la primera calificacion: "))
        calificaciones=[]

        while True:
                op=int(input("¿Desea ingresar otra calificacion? 1-Si 2-No: "))
                if op==1:
                    calificacion=float(input("Ingrese la calificacion: "))
                    objeto=Alumno(mat,nom,carr,calificaciones)
                    calificaciones.append(op)
                    alumnos.append(objeto)
                    print(f"Alumno {nom} agregado")

                elif op==2:
                    break 

        #calificaciones=[]
        #print(f"Su promedio es: {objeto.calcular_promedio}")

    elif opcion==2: 
        nom=input("Ingrese el nombre de quien desea obtener información: ") 
        print(f"Informacion de {nom}")
        for objeto in alumnos: 
            if objeto.nombre==nom:
                objeto.imprimir_info()
                objeto.calcular_promedio()
                #print(f"Promedio: {p}")


            else:
                print("{nom} no se encontró")

    elif opcion==3: 
        mat=int(input("Ingrese la matricula del alumno que desea eliminar: ")) 
        for objeto in alumnos: 
            if objeto.matricula==mat:
                alumnos.pop()
                print(f"Alumno {mat} borrado")
      
            
    elif opcion==4: 
        for objeto in alumnos: 
            objeto.imprimir_info() 

    elif opcion==5: 
        print("Has salido del menu") 
        break  
 
    else: 
        print("Intente nuevamente, la opcion agregada no existe") 

 
 

 

 

 

    
 


 
        
        

 

 

 