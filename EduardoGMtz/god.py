import math

class Cuadrado:
    def __init__(self.lado):
        self.lado = lado

    def area(self):
        a = self.lado * self.lado
        return a

    def perimetro(self):
        p = self.lado * 4
        return p

    def diagonal(self,lado):
        d = self.lado * math.sqrt(2)
        return d


class Triangulo:
    def area(base,altura):
        area = (base * altura) / 2
        return area

    def perimetro(base,altura):
        perimetro = math.sqrt( base**2 + altura**2 )
        return perimetro


class Circulo:
    def area(radio):
        area = math.pi * radio ** 2
        return area

    def perimetro(radio):
        perimetro = 2 * math.pi * radio
        return perimetro




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
        area = area_cuadrado(lado)
        print(f"El Area es: {area}")
    elif calculo == 2:
        perimetro = perimetro_cuadrado(lado)
        print(f"El perimetro es: {perimetro}")
    elif calculo == 3:
        diagonal = diagonal_cuadrado(lado)
        print(f"La diagonal es: {diagonal}")

elif opcion == 2:
    print("Calcuos disponibles:")
    print("1.-Area\n2.-Perimetro")
    calculo = int(input("Elige una opción: "))

    base = float(input("Ingresa la base"))
    altura = float(input("Ingresa la altura: "))

    if calculo == 1:
        area = area_triangulo(base,altura)
        print(f"El area es: {area}")
    elif calculo == 2:
        perimetro = perimetro_triangulo(base,altura)
        print(f"El perimetro es: {perimetro}")

elif opcion == 3:
    print("Calcuos disponibles:")
    print("1.-Area\n2.-Perimetro")
    calculo = int(input("Elige una opción: "))

    radio = float(input("Ingresa el radio: "))
    
    if calculo == 1:
        area = area_circulo(radio)
        print(f"El area es: {area}")
    elif calculo == 2:
        perimetro = perimetro_circulo(radio)
        print(f"El perimetro es: {perimetro}")