import math
from figuras import Cuadrado,Triangulo,Circulo


print("Bienvenido:D \nOpciones Disponibles: \n1. Cuadrado \n2. Triangulo Rectangulo \n3. Circulo ")
opcion = int(input("Ingrese una opción [1, 2, 3] \n>>"))

if opcion == 1:
    print("Calculos Disponibles: ")
    print("\n1. Area \n2. Perimetro \n3. Diagonal ")
    calculo = int(input("Elige una opción: \n>>"))
    
    lado = float(input("Ingrese el valor del lado: \n>>"))
    
    # crear un cuadrado con el lado especificado
    cuadrado = Cuadrado(lado)
    if calculo == 1:
        area = cuadrado.area()
        print(f"El area es: {area}")
    elif calculo == 2:
        perimetro = cuadrado.perimetro()
        print(f"El perimetro es: {perimetro}")
    elif calculo == 3:
        diagonal = cuadrado.diagonal()
        print(f"La diagonal es:{diagonal}") 


if opcion == 2:
    print("Calculos Disponibles: ")
    print("1. Area \n2. Perimetro")
    calculo = int(input("Ingrese una opción \n>>"))

    base = float(input("Ingrese la base: \n>>"))
    altura = float(input("Ingrese la altura: \n>>"))
    triangulo = Triangulo(base,altura)
    
    if calculo == 1:
        area = triangulo.area()
        print(f"El area es: {area}")
    elif calculo == 2:
        perimetro = triangulo.perimetro()
        print(f"El perimetro es: {perimetro}")


if opcion == 3:
    print("Calculos Disponibles: ")
    print("\n1. Area \n2. Perimetro ")
    calculo = int(input("Elige una opción: \n>>"))
    
    radio = float(input("Ingrese el del radio del lado: \n>>"))
    circulo = Circulo(radio)

    if calculo == 1:
        area = circulo.area()
        print(f"El area es: {area}")
    elif calculo == 2:
        perimetro = circulo.perimetro()
        print(f"El perimetro es: {perimetro}")