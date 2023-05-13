from Alumnos import Alumno

lista =[]

#Metodo para registrar alumnos
def Registro ():

    nomb = input("Ingrese el nombre del alumno: ")

    matri = input("Ingrese la matricula (limite 7 caracteres numericos): ")

    carr = input("Ingrese la carrera del alumno: ")

    calf = float(input("Ingrese la calificación del alumno: "))

    dude= Alumno(nomb,matri,carr,calf)
    lista.append(dude)

#Metodo para mostrar todos los datos del alumno incluyendo su promedio 
def Imprimir_info():
        
    for dude in lista:
        print("Nombre: {}, Matricula: {},Carrera: {}, Calificación: {}".format(dude.nomb,dude.matri,dude.carr,dude.calf))
      
        
#Metodo para calcular el promedio
def calcular_promedio ():

    promedio = sum(dude.calf for dude in lista)/ len(lista)

    print ("El promedio general de todos los alumnos es: {:.2f}".format(promedio))

#Metodo para borrar a un alumno en especifico
def Eliminar_alumno ():
    matricula = input("Para buscar un alumno en especifico ingresa su matricula (Solo 7 caracteres numericos): ")

    for f, dude in enumerate(lista):
        if dude.matri == matricula:
            del lista[f]
            print ("Datos de alumno eliminados con exito")
            return
        print ("No se encontró a ningun alumno con esa matricula")
        

#Metodo para buscar a un alumno en especifico
def Buscar_Alumno ():
    matricula = input("Para buscar un alumno en especifico ingresa su matricula (Solo 7 caracteres numericos) ")
    for dude in lista:
        if dude.matri == matricula:
            print("Nombre: {}, Matricula: {},Carrera: {}, Calificación: {}".format(dude.nomb,dude.matri,dude.carr,dude.calf))
            return
        print ("No se encontró a ningun alumno con esa matricula")
            

xd =0 
while xd == 0:

    print ("Bienvenido al portal escolar, elija la opción que desea ejecutar.")


    opcion= int(input("1.- Agregar Alumno \n2.- Mostrar info del alumno\n3.- Eliminar alumno\n4.- Mostrar todos los alumnos \n5.- Salir\n\nIngresa una opción: "))


    if opcion == 1:

        Registro()

        print("Alumno registrado exitosamente")

    elif opcion == 2:
        Buscar_Alumno ()


    elif opcion == 3:
        Eliminar_alumno()
        
 
    elif opcion == 4:
        
        #metodos solicitados
        Imprimir_info()

        calcular_promedio()


        
    elif opcion == 5:
        exit(print("Gracias por usar el portal escolar :)"))


    else:
        print ("Opción invalida eliga una opción valida")