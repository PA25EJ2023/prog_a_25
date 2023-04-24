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
        area = lado * lado
        print(f"El area es: {area}")
    elif calculo == 2:
        perimetro = lado * 4
        print(f"El perimetro es: {perimetro}")
    elif calculo == 3:
        diagonal = lado * math.sqrt(2)
        print(f"La diagonal es: {diagonal}")

elif opcion == 2:
    print("Calculos disponibles: ")
    print("1. Area \n2. Perimetro")
    calculo = int(input("Eliga una opción:"))

    base = float(input("Ingrese la base: "))
    altura = float(input("Ingrese la altura:"))

    if calculo == 1:
        area = (base * altura) /2
        print(f"El area es: {area}")
    elif calculo == 2:
        perimetro = math.sqrt(base**2 + altura**2)
        print(f"El perimetro es: {perimetro}")

elif opcion == 3:
    print("Calculos Disponibles: ")
    print("1. Area \n2. Perimetro")
    calculo = int(input("Eliga una opción: "))

    radio = float(input("Ingrese el radio: "))

    if calculo == 1:
        area = math.pi * radio**2
        print(f"El area es: {area}")
    elif calculo == 2:
        perimetro = 2 * math.pi * radio
        print(f"El perimetro es: {perimetro}")
      

