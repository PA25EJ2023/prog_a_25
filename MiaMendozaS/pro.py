import math 

#Escribir un programa que muestre el siguiente menu:
#1. Cuadrado
#2. Triangulo Rectangulo 
#3. Circulo
#El usuario podra elegir una sola figura 
#Pero cada figura debe arrojar los siguiente:
#Cuadrado. Perimetro, Area y Diagonal  
#Triangulo Rectangulo. Area y Perimetro 
#Circulo. Area y Perimetro 


def area_cuadrado(lado):
    area = lado * lado
    return area 

def perimetro_cuadrado(lado):
    perimetro = lado * 4
    return perimetro

def diagonal_cuadrado(lado):
    diagonal = lado * math.sqrt(2)
    return diagonal 

def area_triangulo(base, altura):
    area = (base * altura) /2
    return area

def perimetro_triangulo(base, altura):
    perimetro = math.sqrt(base**2 + altura**2)
    return perimetro 

def area_circulo(radio):
    area = math.pi * radio**2
    return area

def perimetro_circulo(radio):
    perimetro = 2 * math.pi * radio
    return perimetro 




print("Bienvenido:D")
print("Opciones disponibles:")
print("1. Cuadrado \n2. Triangulo Rectangulo. \n3. Circulo ")
opcion = int(input("Ingrese una opción [1,2,3] \n>> "))

if opcion == 1:
    print("Calculos Disponibles: ")
    print("1. Area \n2. Perimetro \n3. Diagonal ")
    calculo = int(input("Eliga una opción:  "))

    lado = float(input("Ingrese el valor de un lado: "))

    if calculo == 1:
        area = area_cuadrado(lado)
        print(f"El area es: {area}")
    elif calculo == 2:
        perimetro = perimetro_cuadrado(lado)
        print(f"El perimetro es: {perimetro}")
    elif calculo == 3:
        diagonal = diagonal_cuadrado(lado)
        print(f"La diagonal es: {diagonal}")

elif opcion == 2:
    print("Calculos disponibles: ")
    print("1. Area \n2. Perimetro")
    calculo = int(input("Eliga una opción:"))

    base = float(input("Ingrese la base: "))
    altura = float(input("Ingrese la altura:"))

    if calculo == 1:
        area = area_triangulo(base, altura)
        print(f"El area es: {area}")
    elif calculo == 2:
        perimetro = perimetro_triangulo(base, altura)
        print(f"El perimetro es: {perimetro}")

elif opcion == 3:
    print("Calculos Disponibles: ")
    print("1. Area \n2. Perimetro")
    calculo = int(input("Eliga una opción: "))

    radio = float(input("Ingrese el radio: "))

    if calculo == 1:
        area = area_circulo(radio)
        print(f"El area es: {area}")
    elif calculo == 2:
        perimetro = perimetro_circulo(radio)
        print(f"El perimetro es: {perimetro}")