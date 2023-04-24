import math

from figuras import Circulo,Cuadrado,Triangulo

print("Bienvenido")
print("Opciones disponibles")
print("1.cuadrado\n 2.Triangulo\n 3.Circulo")
opcion = int(input("Elige una opcion [1,2,3]"))

if opcion == 1: 
    print("Calculo disponible")
    print("1.Area\n 2.Perimetro\n 3.Diagonal")
    calculo = int(input("Elige una opcion"))

    lado = float(input("Ingresa el valor del lado"))

    #crear un cuadrado con el lado especificado
    cuadrado = Cuadrado(lado)
    if calculo == 1:
        area = cuadrado.area()
        print(f'El area es {area}')
    elif calculo == 2:
        perimetro = cuadrado.perimetro()
        print(f'El perimetro es {perimetro}')
    elif calculo == 3:
        diagonal = cuadrado.diagonal()
        print(f'La diagonal es {diagonal}')
elif opcion == 2:
    print("Calculo disponible")
    print("1.Area\n 2.Perimetro")
    calculo = int(input("Elige una opcion"))

    base = float(input("Ingresa la base"))
    altura = float(input("Ingresa la altura"))

    triangulo = Triangulo(base,altura)
    if calculo == 1:
        area = triangulo.area()
        print(f'El area es {area}')
    elif calculo == 2:
        perimetro = triangulo.perimetro()
        print(f'El perimetro es {perimetro}')
elif opcion == 3:
    print("Calculo disponible")
    print("1.Area\n 2.Perimetro")
    calculo = int(input("Elige una opcion"))

    radio = float(input("Ingresa el radio"))

    circulo = Circulo(radio)
    if calculo == 1:
        area = circulo.area()
        print(f'El area es {area}')
    elif calculo == 2:
        perimetro = circulo.perimetro()
        print(f'El perimetro es {perimetro}')



