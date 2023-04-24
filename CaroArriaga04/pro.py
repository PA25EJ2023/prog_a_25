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
def area_triangulo(base,altura):
    area = (base * altura) / 2
    return area
def perimetro_triangulo(base,altura):
    perimetro = math.sqrt(base**2 + altura**2)
    return perimetro
def area_circulo(radio):
    area = math.pi * radio**2
    return area
def perimetro_circulo(radio):
    perimetro = (2 * math.pi) * radio
    return perimetro

print("Bienvenido")
print("Opciones disponibles")
print("1.Cuadrdado\n2.Triangulo\n3.Circulo")
op = int(input("Elige una opcion [1,2,3]: "))
if op == 1:
    print("Calculos disponibles")
    print("1.Area\n2.Perimetro\n3.Diagonal")
    calculo = int(input("Elige una opcion: "))
    lado = float(input("Ingresa el valor de lado: "))
    if calculo == 1:
        area = area_cuadrado(lado)
        print(f"El area es {area}")
    elif calculo == 2:
        perimetro = perimetro_cuadrado(lado)
        print(f"El perimetro es {perimetro}")
    elif calculo == 3:
        diagonal = diagonal_cuadrado(lado)
        print(f"La diagonal es {diagonal}")
elif op == 2:
    print("Calculos disponibles")
    print("1.Area\n2.Perimetro")
    calculo = int(input("Elige una opcion: "))
    base = float(input("Ingresa el valor de la base"))
    altura = float(input("Ingresa el valor de la altura: "))
    if calculo == 1:
        area = area_triangulo(base,altura)
        print(f"El area es {area}")
    elif calculo == 2:
        perimetro = perimetro_triangulo(base,altura)
        print(f"El perimetro es {perimetro}")
elif op == 3:
    print("Calculos disponibles")
    print("1.Area\n2.Perimetro")
    calculo = int(input("Elige una opcion: "))
    radio = float(input("Ingresa el radio: "))
    if calculo == 1:
        area = area_circulo(radio)
        print(f"El area es {area}")
    elif calculo == 2:
        perimetro = perimetro_circulo(radio)
        print(f"El perimetro es {perimetro}")
    
