import math

def area_cuadrado(lado):
    area = lado * lado
    print(f"El area es {area}")
    return area

def perimetro_cuadrado(lado):
    perimetro = lado * 4
    print(f"El perimetro es {perimetro}")
    return perimetro

def diagonal_cuadrado(lado):
    diagonal = lado * math.sqrt(2)
    print(f"El diagonal es {diagonal}")
    return diagonal 

def area_triangulo(base,altura):
    area = (base * altura) / 2
    print(f"El area es {area}")
    return area

def perimetro_triangulo(base,altura):
    perimetro = math.sqrt(base**2 + altura**2)
    print(f"El perimetro es {perimetro}")
    return perimetro

def area_circulo(radio):
    area = math.pi * radio ** 2
    print(f"El area es {area}")
    return area

def perimetro_circulo(radio):
    perimetro = 2 * math.pi * radio
    print(f"El perimetro es {perimetro}")
    return perimetro


print("Bienvenidos")
print("Opciones disponibles")
print("1. Cuadrado\n2 2. Triangulo\n2 3. Circulo")
opcion = int(input("Elige una opcion [1,2,3]"))

if opcion == 1:
    print("Calculos disponibles: ")
    print("1. Area\n2 2. Perimetro\n2 3. Diagonal")
    calculo = int(input("Elige una opcion: "))

    lado = float(input("Ingresa el valor del lado"))

    if calculo == 1:
        area = area_cuadrado(lado)
    elif calculo == 2:
        perimetro = perimetro_cuadrado
    elif calculo == 3:
        diagonal = diagonal_cuadrado
elif opcion == 2:
    print("Calculos disponibles")
    print("1. Area\n2 2. Perimetro")
    calculo = int(input("Elige la opcion"))

    base = float(input("Ingresa la base"))
    altura = float(input("Ingresa la altura"))

    if calculo == 1:
        area = area_triangulo
    elif calculo == 2:
        perimetro = perimetro_triangulo
elif opcion == 3:
    print("Calculos disponibles")
    print("1. Area\n2 2. Perimetro")
    calculo = int(input("Elige la opcion"))

    radio = float(input("Ingresa la radio"))

    if calculo == 1:
        area = area_circulo
    elif calculo == 2:
        perimetro = perimetro_circulo