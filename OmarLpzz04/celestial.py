import math
from figuras import Cuadrado,Triangulo,Circulo
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
    
    #crear un cuadrado con el lado especificado
    cuadrado = Cuadrado(lado)
    if calculo == 1:
        area = cuadrado.area()
        print(f"El area es: {area}")
    elif calculo == 2:
        perimetro = cuadrado.perimetro()
        print(f"El perimetro es: {perimetro}")
    elif calculo == 3:
        diagonal = cuadrado.diagonal()
        print(f"La diagonal es: {diagonal}")
elif opcion == 2:
    print("calculos disponibles")
    print("1.-area\n2.-perimetro")
    calculo = float(input("Elige una opcion: "))
    base = float(input("Cual es la base: "))
    altura = float(input("Cual es la altura: "))
    
    triangulo = Triangulo(base,altura)
    if calculo == 1:
        area = triangulo.area()
        print(f"el area es: {area}")
    elif calculo ==2:
        perimetro = triangulo.perimetro()
        print(f"El perimetro es: {perimetro}")
elif opcion == 3:
    print("calculos disponibles")
    print("1.-area\n2.-perimetro")
    calculo = int(input("Elige una opcion: "))
    radio = float(input("Ingresa el radio: "))

    circulo = Circulo(radio)
    if calculo == 1:
        area = circulo.area()
        print(f"el area es: {area}")
    elif calculo == 2:
        perimetro = circulo.perimetro()
        print(f"El perimetro es: {perimetro}")