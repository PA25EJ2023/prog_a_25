import math

print ("Bienvenido")
print ("Opciones disponibles")
print ("1-Cuadrado\n2-Triangulo\n3-Circulo")
opcion = int(input("Elige una opción [1,2,3]:\n "))
if opcion == 1:
    print ("Calculos disponibles: ")
    print ("1-Area\n2-Perimetro\n3-Diagonal")
    calculo = int(input("Elige una opción:\n"))
    lado = float (input("Ingresa el lado del cuadrado:\n"))
    if calculo == 1:
        area = lado * lado
        print ("El area es ",area)
    elif calculo == 2:
        perimetro = lado *4
        print (" El perimetro es: ", perimetro)
    elif calculo == 3:
        diagonal = lado* math.sqrt(2)

elif opcion == 2:
    print ("Calculos disponibles: ")
    print ("1-Area\n2-Perimetro")
    calculo = int(input("Elige una opción:\n"))
    base = float (input("Ingresa la base del triangulo:\n"))
    altura = float (input("Ingresa la altura del triangulo:\n"))
    if calculo == 1:
        area = (base*altura)/2
        print ("El area del triangulo es ",area)
    elif calculo == 2:
        perimetro = math.sqrt(base**2 + altura**2)
        print (" El perimetro del triangulo es: ", perimetro)
    
elif opcion == 3:
    print ("Calculos disponibles: ")
    print ("1-Area\n2-Perimetro")
    calculo = int(input("Elige una opción:\n"))
    radio = float (input("Ingresa el radio del circulo:\n")) 
    if calculo == 1:
        area = math.pi * radio ** 2
        print ("El area del circulo es ",area)
    elif calculo == 2:
        perimetro = 2 * math.pi * radio
        print (" El perimetro del circulo es: ", perimetro)   



        
    