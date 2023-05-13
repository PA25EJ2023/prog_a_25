from clases_de_la_Evi3 import Alumno

print("Bienvenido")
print("OPCIONES")
alumnos=[]
while True:
    print("1.Agregar alumno\n2.Mostrar info de alumno\n3.Eliminar alumno\n4.Mostrar todos los alumnos\n5.Salir")
    opcion=int(input("Elige una opcion:[1,2,3,4,5]:"))
    
    if opcion ==1:
        matricula=int(input("Ingrese Matricula:"))
        nombre=(input("Ingresa nombre:"))
        carrera=(input("Ingrese carrera:"))
        califs= []
        agr="S" 


        while agr.upper() == "S":
            calif=float(input("Ingrese calificacion:"))
            califs.append(calif)
            agr=input("¿Quieres agregar otra calificacion? S/N:")

        alumnos_info=Alumno(matricula,nombre,carrera,califs)
        alumnos.append(alumnos_info)
        

    elif opcion ==2:
        matricula=int(input("Ingresa matricula de alumno que quieres ver su informacion:"))
        for alumno in alumnos:
            if alumno.matricula == matricula:
                alumno.imprimir_info() 
                alumnos_info.calcular_promedio()

    elif opcion ==3:
        matricula=int(input("Ingrese la matricula que desee eliminar:"))
        eliminado=False
        for alumno in alumnos:
            if alumno.matricula == matricula:
                alumnos.remove(alumno)
                eliminado=True
                break
            
                


    elif opcion ==4:
        print("Alumnos")
        for alumnos_info in alumnos:
            alumnos_info.mostrar_alumnos()
            alumnos_info.calcular_promedio()

    elif opcion ==5:
        print("buen dia")
        break        

