import math

class Cuadrado:
    def __init__(self,lado):
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
    def __init__(self,base,altura):
       self.base = base
       self.altura = altura

    def area_triangulo():
        area = base * altura
        return area

    def perimetro_triangulo():
        perimetro = math.sqrt(base**2 + altura**2)
        return perimetro

  
class Circulo:
    def __init__(self,radio):
        self.radio = radio

    def area(self):
        area = math.pi * self.radio **2
        return area

    def perimetro(self):
        perimetro = math.pi * self



print("Bienvenido")
print("Opciones disponibles: ")
print("1.-Cuadrado\n2.-Triangulo\n3.-Circulo")
opcion = int(input("Elige una opción [1, 2, 3]: "))

if opcion == 1:
    print("Calculos disponbles:")
    print("1.-Area\n2.-Perimetro\n3.-Diagonal")
    calculo = int(input("Elige una opción: "))

    lado = float(input("Ingresa el valor del lado: "))
    cuadrado = Cuadrado(lado)

    if calculo == 1:
        area = cuadrado.area()
        print(f"El Area es: {area}")
    elif calculo == 2:
        perimetro = cuadrado.perimetro()
        print(f"El perimetro es: {perimetro}")
    elif calculo == 3:
        diagonal = cuadrado.diagonal()
        print(f"La diagonal es: {diagonal}")

elif opcion == 2:
    print("Calcuos disponibles:")
    print("1.-Area\n2.-Perimetro")
    calculo = int(input("Elige una opción: "))

    base = float(input("Ingresa la base"))
    altura = float(input("Ingresa la altura: "))
    triangulo = Triangulo(base,altura)
    if calculo == 1:
        area = triangulo.area_triangulo()
        print(f"El area es: {area}")
    elif calculo == 2:
        perimetro = triangulo.perimetro_triangulo()
        print(f"El perimetro es: {perimetro}")

elif opcion == 3:
    print("Calcuos disponibles:")
    print("1.-Area\n2.-Perimetro")
    calculo = int(input("Elige una opción: "))

    radio = float(input("Ingresa el radio: "))
    circulo = Circulo(radio)
    if calculo == 1:
        area = circulo.area()
        print(f"El area es: {area}")
    elif calculo == 2:
        perimetro = circulo.perimetro()
        print(f"El perimetro es: {perimetro}")