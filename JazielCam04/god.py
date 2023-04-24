import math

class Cuadrado:

    def __init__(self,lado):
        self.lado = lado

    def area(self):
        a = self.lado * self.lado
        print(f"El area es {a}")
        return a

    def perimetro(self):
        p = self.lado * 4
        print(f"El perimetro es {p}")
        return p

    def diagonal(self):
        d = self.lado * math.sqrt(2)
        print(f"El diagonal es {d}")
        return d

class Triangulo:
    def abs(self):
        a = (base * altura) / 2
        print(f"El area es {a}")
        return a

    def perimetro(self):
        p = math.sqrt(base**2 + altura**2)
        print(f"El perimetro es {p}")
        return p

class Circulo:
    def area_circulo(self):
        a = math.pi * radio ** 2
        print(f"El area es {a}")
        return a

    def perimetro_circulo(self):
        p = 2 * math.pi * radio
        print(f"El perimetro es {p}")
        return p





 





print("Bienvenidos")
print("Opciones disponibles")
print("1. Cuadrado\n2 2. Triangulo\n2 3. Circulo")
opcion = int(input("Elige una opcion [1,2,3]"))

if opcion == 1:
    print("Calculos disponibles: ")
    print("1. Area\n2 2. Perimetro\n2 3. Diagonal")
    calculo = int(input("Elige una opcion: "))

    lado = float(input("Ingresa el valor del lado"))

    if calculo == 1:
        cuadrado()
    elif calculo == 2:
        perimetro = p
    elif calculo == 3:
        diagonal = d
elif opcion == 2:
    print("Calculos disponibles")
    print("1. Area\n2 2. Perimetro")
    calculo = int(input("Elige la opcion"))

    base = float(input("Ingresa la base"))
    altura = float(input("Ingresa la altura"))

    if calculo == 1:
        area = a
    elif calculo == 2:
        perimetro = p
elif opcion == 3:
    print("Calculos disponibles")
    print("1. Area\n2 2. Perimetro")
    calculo = int(input("Elige la opcion"))

    radio = float(input("Ingresa la radio"))

    if calculo == 1:
        area = a
    elif calculo == 2:
        perimetro = p