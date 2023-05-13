from clase_alumno import Alumno

print("Bienvenido")

print("Opciones")

alumnos=[]

while True:
    print("1.Agregar alumno\n2.Mostrar info de alumno\n3.Eliminar alumno\n4.Mostrar todos los alumnos\n5.Salir")
    opcion=int(input("Elige una opcion:[1,2,3,4,5]:"))
    if opcion ==1:
        matricula=int(input("Ingresa una matricula:"))
        nombre=(input("Ingresa un nombre:"))
        carrera=(input("Ingrese carrera:"))
         
        califs= []
        agregar="S"

        while agregar.upper() == "S":
            calif=float(input("Ingrese calificacion:"))
            califs.append(calif)
            agregar=input("¿Quieres agregar otra calificacion? S/N:")
        alumnos_info=Alumno(matricula,nombre,carrera,califs)
        alumnos.append(alumnos_info)


    elif opcion ==2:#mostrar informacion de alumno
        print("Mostar informacion de la matricula")
        matricula=int(input("Matricula:"))
        for alumno in alumnos:
            if alumno.matricula == matricula:
                print("*"*50)
                alumno.imprimir_info()
                alumnos_info.calcular_promedio()
                print("*"*50)

    elif opcion ==3:#eliminar alumno
        print("Eliminar alumno ingresando matricula")
        matricula=int(input("Matricula:"))
        eliminado=False
        for alumno in alumnos:
            if alumno.matricula == matricula:
                alumnos.remove(alumno)
                eliminado=True
                break

    elif opcion ==4:#mostrar todos los alumnos
        print("Informacion Alumnos")
        for alumnos_info in alumnos:
            alumnos_info.mostrar_alumnos()
            alumnos_info.calcular_promedio()
            print("*"*50)

    elif opcion ==5:
        break 