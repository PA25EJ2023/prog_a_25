import math


print("Bienvenido")
print("Opciones disponibles: ")
print("1.-Cuadrado\n2.-Triangulo\n3.-Circulo")
opcion = int(input("Elige una opción [1, 2, 3]: "))

if opcion == 1:
    print("Calculos disponbles:")
    print("1.-Area\n2.-Perimetro\n3.-Diagonal")
    calculo = int(input("Elige una opción: "))

    lado = float(input("Ingresa el valor del lado: "))

    if calculo == 1:
        area = lado * lado
        print(f"El Area es: {area}")
    elif calculo == 2:
        perimetro = lado * 4
        print(f"El perimetro es: {perimetro}")
    elif calculo == 3:
        diagonal = lado * math.sqrt (2)
        print(f"La diagonal es: {diagonal}")

elif opcion == 2:
    print("Calcuos disponibles:")
    print("1.-Area\n2.-Perimetro")
    calculo = int(input("Elige una opción: "))

    base = float(input("Ingresa la base"))
    altura = float(input("Ingresa la altura: "))

    if calculo == 1:
        area = (base * altura) / 2
        print(f"El area es: {area}")
    elif calculo == 2:
        perimetro = math.sqrt( base**2 + altura**2 )
        print(f"El perimetro es: {perimetro}")

elif opcion == 3:
    print("Calcuos disponibles:")
    print("1.-Area\n2.-Perimetro")
    calculo = int(input("Elige una opción: "))

    radio = float(input("Ingresa el radio: "))
    
    if calculo == 1:
        area = math.pi * radio ** 2
        print(f"El area es: {area}")
    elif calculo == 2:
        perimetro = 2 * math.pi * radio
        print(f"El perimetro es: {perimetro}")