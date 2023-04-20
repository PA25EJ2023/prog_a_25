import math

def area_cuadrado():
    area = lado * lado
    return area

def perimetro_cuadrado():
    perimetro = lado * 4
    return perimetro

def diagonal_cuadrado():
    diagonal = lado * math.sqrt(2)
    return diagonal

def area_trangulo():
    area = base * altura
    return area

def perimetro_triangulo():
    perimetro = math.sqrt(base**2 + altura**2)
    return perimetro

def area_circulo():
    area = math.pi * radio ** 2
    return area

def perimetro_circulo():
    perimetro = 2 * math.pi * radio
    return perimetro


print("Bienvenido")
print("Opciones disponibles:")
print("1.Cuadrado\n2.Triangulo\n3.Circulo")
opcion = int(input("Selecciona la opcion: "))
if opcion == 1:
    print("Calculos disponibles:")
    print("1.Area\n2.Perimetro\n3.Diagonal")
    calculo = int(input("Elige una opcion: "))

    lado = float(input("Ingresa el valor del lado: "))

    if calculo == 1:
        area = area_cuadrado(lado)
        print(f"El are es {area}")
    elif calculo == 2:
        perimetro = perimetro_cuadrado(lado)
        print(f"El area es {perimetro}")
    elif calculo == 3:
        diagonal = diagonal_cuadrado(lado)
        print(f"La diagonal es: {diagonal}")
elif opcion == 2:
    print("Calculos disponibles:")
    print("1.Area\n2.Perimetro")
    calculo = int(input("Elige una opcion: "))

    base = float(input("Ingresa el valor de la base: "))
    altura = float(input("Ingresa el valor de la altura: "))

    if calculo == 1:
        area = area_trangulo(base,altura)
        print(f"El area es: {area}")
    elif calculo == 2:
        perimetro = perimetro_triangulo(base,altura)
        print(f"El perimetro es: {perimetro}")
elif opcion == 3:
    print("Calculos disponibles:")
    print("1.Area\n2.Perimetro")
    calculo = int(input("Elige una opcion: "))

    radio = float(input("Ingresa el valor del radio: "))

    if calculo == 1:
        area = area_circulo(radio)
        print(f"El are es {area}")
    elif calculo == 2:
        perimetro = perimetro_circulo(radio)
        print(f"El permietro es {perimetro}")
