import math
from figuras import Cuadrado,Circulo, Triangulo

print("Bienvenidos")
print("Opciones disponibles")
print("1.Cuadrado\n2.Triangulo\n3.Circulo")
opcion = int(input("Elige una opcion [1,2,3]"))

if opcion == 1:
    print("Calculos disponibles")
    print("1.Area\n2.Perimetro\n3.Diagonal")
    calculo = int(input("Elige una opcion"))

    lado = float(input("ingresa el valor del lado"))

    #crar un cuadrado con el lado especificado
    cuadrado = Cuadrado(lado) 
    if calculo == 1 :
        area = cuadrado.area()
        print(f"El area es: {area}")
    elif calculo == 2:
        perimetro = cuadrado.perimetro(lado)
        print(f"El perimetro es: {perimetro}")
    elif calculo == 3 :
        diagonal = cuadrado.diagonal(lado)
        print(f"La diagonal es: {diagonal}")
elif opcion == 2:
     print("Calculos disponibles")
     print("1.Area\n2.Perimetro")
     calculo = int(input("Elige una opcion"))

     base = float(input("ingresa la base"))
     altura = float(input("ingresa la altura"))

     triangulo = Triangulo(base,altura)
     if calculo == 1 :
        area = triangulo.area()
        print(f"El area es: {area}")
     elif calculo == 2:
        perimetro = triangulo.perimetro()
        print(f"El perimetro es: {perimetro}")
elif opcion == 3:
     print("Calculos disponibles")
     print("1.Area\n2.Perimetro")
     calculo = int(input("Elige una opcion"))
     radio = float(input("ingresa el radio"))

     circulo = Circulo(radio)
     if calculo == 1 :
        area = circulo.area()
        print(f"El area es: {area}")
     elif calculo == 2:
        perimetro = circulo.perimetro()
        print(f"El perimetro es: {perimetro}")