from Registro_Alumnos import Alumno



lista=[]


def Imprimir_info():
    
    W = 0
    while W < len(lista[W].nom," ", lista[W].matri," ", lista[W].calf):
        W= W + 1

xd =0 
while xd == 0:

    print ("Bienvenido al portal escolar, elija la opción que desea ejecutar.")


    opcion= int(input("1.- Agregar Alumno \n2.- Mostrar info del alumno\n3.- Eliminar alumno\n4.- Mostrar todos los alumnos \n5.- Salir\n"))


    if opcion == 1:

        n = input("Ingrese el nombre del alumno:\n")

        m = input("Ingrese la matricula (limite 7 caracteres numericos)\n")

        c = input("Ingrese la calificación del alumno:\n")

        objeto= Alumno(n,m,c)
        lista.append(objeto)

        print("Alumno registrado exitosamente")

    elif opcion == 2:
        print("Alumnos registrados en el sistema:")
        Imprimir_info()


    elif opcion == 3:
        pass


    elif opcion == 4:
        pass


    elif opcion == 5:
        exit(print("Gracias por usar el portal escolar :)"))