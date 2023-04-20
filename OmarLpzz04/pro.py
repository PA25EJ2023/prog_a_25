def area_cuadrado(lado):
    area = lado * lado
    return area
    pass
def perimetro_cuadrado(lado):
    perimetro = lado*4
    return perimetro
    pass
def diagonal_cuadrado(lado):
    diagonal = lado * math.sqrt(2)
    return diagonal 
    pass

def area_circulo(radio):

    area =(math.pi*radio)**2
    pass
def perimetro_circulo(radio):
    perimetro = math.pi * 2 * radio 
    pass

def area_triangulo(base,altura):
    area = (base * altura) /2
    pass
def perimetro_triangulo(base,altura):
    perimetro= base *altura
    pass










import math 

print("BIENVENIDO")
print(f"{'*' * 10 }OPCIONES DISPONIBLES{'*' * 10 }")
print("1.-Cuadrado\n2.-Tirangulo Rectangulo\n3.-Circulo")
opcion = int(input("Elige una opcion (1,2,3)>> "))
print(f"{'-' * 10}")

if opcion == 1:
    print("calculos disponibles")
    print("1.-area\n2.-perimetro\n3.-diagonal")
    calculo = float(input("Elige una opcion: "))
    lado = int(input("Que medida tendra: "))

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
    print("calculos disponibles")
    print("1.-area\n2.-perimetro")
    calculo = float(input("Elige una opcion: "))
    base = float(input("Cual es la base: "))
    altura = float(input("Cual es la altura: "))
    
    if calculo == 1:
        area = area_triangulo(base,altura)
        print(f"el area es: {area}")
    elif calculo == 2:
        perimetro = perimetro_triangulo(base,altura) 
        print(f"El perimetro es: {perimetro}")
elif opcion == 3:
    print("calculos disponibles")
    print("1.-area\n2.-perimetro")
    calculo = int(input("Elige una opcion: "))
    radio = float(input("Ingresa el radio: "))

    if calculo == 1:
        area = area_circulo(radio)
        print(f"el area es: {area}")
    elif calculo == 2:
        perimetro = perimetro_circulo(radio)
        print(f"El perimetro es: {perimetro}")