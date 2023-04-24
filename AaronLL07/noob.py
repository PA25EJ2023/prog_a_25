import math
print("Bienvenido")
print("Opciones disponibles")
print("1. Cuadrado\n2. Triangulo\n3. Circulo")
opcion = int(input("Elige una opcion [1,2,3]: "))

if opcion == 1:
    print("Calculos disponibles: ")
    print("1. Area\n2. Perimetro\n3. Diagonal")
    calculo = int(input("Elige una opcion: "))
    lado = float(input("Ingresa el valor del lado: "))
    if calculo == 1:
        print(f"El area del cuadrado es: {lado * lado}")
    elif calculo == 2:
        print(f"El perimetro del cuadrado es: {lado * 4}")
    elif calculo == 3:
        print(f"La diagonal del cuadrado es: {lado * math.sqrt(2)}")
elif opcion == 2:
    print("Calculos disponibles: ")
    print("1. Area\n2. Perimetro")
    calculo = int(input("Elige una opcion: "))
    base = float(input("Ingresa el valor de la base: "))
    altura = float(input("Ingresa el valor de la altura: "))
    if calculo == 1:
        print(f"El area del triangulo es: {(base * altura)/2}")
    elif calculo == 2:
        print(f"El perimetro del triangulo es: {math.sqrt(base**2 + altura**2)}")
elif opcion == 3:
    print("Calculos disponibles: ")
    print("1. Area\n2. Perimetro")
    calculo = int(input("Elige una opcion: "))
    radio = float(input("Ingresa el valor de radio del circulo: "))
    if calculo == 1:
        print(f"El area del circulo es: {math.pi * radio**2}")
    elif calculo == 2:
        print(f"El perimetro del circulo es: {2 * math.pi * radio}")