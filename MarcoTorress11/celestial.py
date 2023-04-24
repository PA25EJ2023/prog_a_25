import math
from figuras import Cuadrado,Triagulo,Circulo

print("Bienvenido")
print("Opciones disponibles:")
print("1.Cuadrado\n2.Triangulo\n3.Circulo")
opcion = int(input("Selecciona la opcion: "))
if opcion == 1:
    print("Calculos disponibles:")
    print("1.Area\n2.Perimetro\n3.Diagonal")
    calculo = int(input("Elige una opcion: "))

    lado = float(input("Ingresa el valor del lado: "))

#crear un cuadrado con el lado específico
    cuadrado = Cuadrado(lado)
    if calculo == 1:
        area = cuadrado.area()
        print(f"El are es {area}")
    elif calculo == 2:
        perimetro = cuadrado.perimetro()
        print(f"El area es {perimetro}")
    elif calculo == 3:
        diagonal = cuadrado.diagonal()
        print(f"La diagonal es: {diagonal}")
elif opcion == 2:
    print("Calculos disponibles:")
    print("1.Area\n2.Perimetro")
    calculo = int(input("Elige una opcion: "))

    base = float(input("Ingresa el valor de la base: "))
    altura = float(input("Ingresa el valor de la altura: "))

    triangulo = Triagulo(base,altura)
    if calculo == 1:
        area = triangulo.area_trangulo()
        print(f"El area es: {area}")
    elif calculo == 2:
        perimetro = triangulo.perimetro_triangulo()
        print(f"El perimetro es: {perimetro}")
elif opcion == 3:
    print("Calculos disponibles:")
    print("1.Area\n2.Perimetro")
    calculo = int(input("Elige una opcion: "))

    radio = float(input("Ingresa el valor del radio: "))

    circulo = Circulo(radio)
    if calculo == 1:
        area = circulo.area_circulo()
        print(f"El are es {area}")
    elif calculo == 2:
        perimetro = circulo.perimetro_circulo()
        print(f"El permietro es {perimetro}")
