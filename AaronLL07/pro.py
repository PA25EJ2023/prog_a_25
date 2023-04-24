import math

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
    area = (base * altura)/2
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

print("Bienvenido")
print("Opciones disponibles")
print("1. Cuadrado\n2. Triangulo\n3. Circulo")
opcion = int(input("Elige una opcion [1,2,3]: "))

if opcion == 1:
    print("Calculos disponibles: ")
    print("1. Area\n2. Perimetro\n3. Diagonal")
    calculo = int(input("Elige una opcion: "))
    lado = float(input("Ingresa el valor del lado: "))
    if calculo == 1:
        print(f"El area del cuadrado es: {area_cuadrado(lado)}")
    elif calculo == 2:
        print(f"El perimetro del cuadrado es: {perimetro_cuadrado(lado)}")
    elif calculo == 3:
        print(f"La diagonal del cuadrado es: {diagonal_cuadrado(lado)}")
elif opcion == 2:
    print("Calculos disponibles: ")
    print("1. Area\n2. Perimetro")
    calculo = int(input("Elige una opcion: "))
    base = float(input("Ingresa el valor de la base: "))
    altura = float(input("Ingresa el valor de la altura: "))
    if calculo == 1:
        print(f"El area del triangulo es: {area_triangulo(base, altura)}")
    elif calculo == 2:
        print(f"El perimetro del triangulo es: {perimetro_triangulo(base, altura)}")
elif opcion == 3:
    print("Calculos disponibles: ")
    print("1. Area\n2. Perimetro")
    calculo = int(input("Elige una opcion: "))
    radio = float(input("Ingresa el valor de radio del circulo: "))
    if calculo == 1:
        print(f"El area del circulo es: {area_circulo(radio)}")
    elif calculo == 2:
        print(f"El perimetro del circulo es: {perimetro_circulo(radio)}")