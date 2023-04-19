#Escribir un programa que muestre el sig menu:
#1.-Cuadrado 2.-Triangulo Rectangulo 3.-Circulo
#El usuario podra solo elegir una figura
#Para cada figura se debe calcular lo siguiente:
#Cuadrado. Area, Perimetro y Diagonal
#Triangulo Rectangulo. Area y Perimetro
#Circulo. Area y Perimetro

import math

print("Bienvenido")
print("Opciones disponibles")
print("1.-Cuadrado\n2.-Triangulo Rectangulo\n3.-Circulo")
opcion = int(input("Elige una opcion {1,2,3}: "))

if opcion == 1:
    print("Calculos disponibles")
    print("1.-Area\n2.-Perimetro\n3.-Diagonal")
    calculo = int(input("Elige una opcion: "))
    lado = float(input("Ingresa el valor del lado: "))

    if calculo == 1:
        area = lado * lado
        print(f"El area es: {area}")
    
    elif calculo == 2:
        perimetro = lado*4
        print(f"El perimetro es: {perimetro}")

    elif calculo == 3:
        diagonal = lado * math.sqrt(2)
        print(f"La diagonal es: {diagonal}")

elif opcion == 2:
    print("Calculos disponibles")
    print("1.-Area\n2.-Perimetro")
    calculo = int(input("Elige una opcion: "))
    base = float(input("Ingresa el valor de la base: "))
    altura = float(input("Ingresa el valor de la altura: "))

    if calculo == 1:
        area = (base * altura)/2
        print(f"El area es: {area}")
    
    elif calculo == 2:
        perimetro = math.sqrt(base**2 + altura**2)
        print(f"El perimetro es: {perimetro}")

elif opcion == 3:
    print("Calculos disponibles")
    print("1.-Area\n2.-Perimetro")
    calculo = int(input("Elige una opcion: "))
    radio = float(input("Ingresa el valor del radio: "))

    if calculo == 1:
        area = (math.pi * radio)**2
        print(f"El area es: {area}")
    
    elif calculo == 2:
        perimetro = (math.pi * 2) * radio
        print(f"El perimetro es: {perimetro}")






