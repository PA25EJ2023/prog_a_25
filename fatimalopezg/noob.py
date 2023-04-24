#Escribir un programa que muestre el siguiente menu:
#1. Cuadrado
#2. Triangulo rectangulo
#3. Circulo
#el usuario solo puede elegir una figura
#Para cada figura se debe calcular lo sig:
#Cuadrado= Area, Perimetro y Diagonal
#Triangulo rectabgulo= Area y Perimetro
#Circulo= Area y Perimetro
# niveles: noob (normal), pro (funciones), god (clases)

import math
print("Bienvenido")
print ("Opciones disponibles")
print ("1.Cuadrado\n2.Triangulo rectangulo\n3.Circulo")
opcion=int(input("Elige una opcion [1,2,3]"))

if opcion==1:
    print("Calculos disponibles")
    print("1.Area\n2.Perimetro\n3.Diagonal")
    calculo=int(input("Elige una opcion: "))

    lado=float(input("Ingresa el valor del lado "))
    if calculo==1:
        area=lado*lado
        print(f"El area es: {area}")

    elif calculo==2:
        perimetro=lado * 4
        print(f"El perimetro es: {perimetro}")
    
    elif calculo==3:
        diagonal=lado * math.sqrt(2) 
        print(f"La diagonal es: {diagonal}")

elif opcion==2:
    print("Calculos disponibles")
    print("1.Area\n2.Perimetro")
    calculo=int(input("Elige una opcion: "))

    base=float(input("Ingresa la base "))
    altura=float(input("Ingresa la altura "))
    if calculo==1:
        area=(base*altura)/2
        print(f"El area es: {area}")

    elif calculo==2:
        perimetro=math.sqrt(base**2 + altura**2)
        print(f"El perimetro es: {perimetro}")

elif opcion==3:
    print("Calculos disponibles")
    print("1.Area\n2.Perimetro")
    calculo=int(input("Elige una opcion: "))

    radio=float(input("Ingresa el radio "))
    if calculo==1:
        area=math.pi * radio ** 2
        print(f"El area es {area}")
    
    elif calculo==2:
        perimetro=2 * math.pi * radio
        print(f"El perimetro es {perimetro}")