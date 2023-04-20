import math

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
        area = lado * lado
        print(f"El are es {area}")
    elif calculo == 2:
        perimetro = lado * 4
        print(f"El area es {perimetro}")
    elif calculo == 3:
        diagonal = lado * math.sqrt(2)
        print(f"La diagonal es: {diagonal}")
elif opcion == 2:
    print("Calculos disponibles:")
    print("1.Area\n2.Perimetro")
    calculo = int(input("Elige una opcion: "))

    base = float(input("Ingresa el valor de la base: "))
    altura = float(input("Ingresa el valor de la altura: "))

    if calculo == 1:
        area = base * altura
        print(f"El area es: {area}")
    elif calculo == 2:
        perimetro = math.sqrt(base**2 + altura**2)
        print(f"El perimetro es: {perimetro}")
elif opcion == 3:
    print("Calculos disponibles:")
    print("1.Area\n2.Perimetro")
    calculo = int(input("Elige una opcion: "))

    radio = float(input("Ingresa el valor del radio: "))

    if calculo == 1:
        area = math.pi * radio ** 2
        print(f"El are es {area}")
    elif calculo == 2:
        perimetro = 2 * math.pi * radio
        print(f"El permietro es {perimetro}")
