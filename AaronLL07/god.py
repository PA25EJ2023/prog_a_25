import math

# Clase de cuadrado
class Cuadrado:
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        a = self.lado * self.lado
        return a

    def perimetro(self):
        p = self.lado * 4
        return p

    def diagonal(self):
        d = self.lado * math.sqrt(2)
        return d

# Clase de triangulo
class Triangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def area(self):
        a = (self.base * self.altura)/2
        return a
    
    def perimetro(self):
        perimetro = math.sqrt(self.base**2 + self.altura**2)
        return perimetro

# Clase de circulo
class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        area = math.pi * self.radio**2
        return area

    def perimetro(self):
        perimetro = 2 * math.pi * self.radio
        return perimetro 

print("Bienvenido")
print("Opciones disponibles")
print("1. Cuadrado\n2. Triangulo\n3. Circulo")
opcion = int(input("Elige una opcion [1,2,3]: "))

if opcion == 1:
    print("Calculos disponibles: ")
    print("1. Area\n2. Perimetro\n3. Diagonal")
    calculo = int(input("Elige una opcion: "))

    lado = float(input("Ingresa el valor del lado: "))

    #crear un cuadrado con el lado especificado
    cuadrado = Cuadrado(lado)
    if calculo == 1:
        print(f"El area del cuadrado es: {cuadrado.area()}")
    elif calculo == 2:
        print(f"El perimetro del cuadrado es: {cuadrado.perimetro()}")
    elif calculo == 3:
        print(f"La diagonal del cuadrado es: {cuadrado.diagonal()}")
elif opcion == 2:
    print("Calculos disponibles: ")
    print("1. Area\n2. Perimetro")
    calculo = int(input("Elige una opcion: "))
    base = float(input("Ingresa el valor de la base: "))
    altura = float(input("Ingresa el valor de la altura: "))

    #crear un triangulo como objeto con los lados especificados
    triangulo = Triangulo(base, altura)
    if calculo == 1:
        print(f"El area del triangulo es: {triangulo.area()}")
    elif calculo == 2:
        print(f"El perimetro del triangulo es: {triangulo.perimetro()}")
elif opcion == 3:
    print("Calculos disponibles: ")
    print("1. Area\n2. Perimetro")
    calculo = int(input("Elige una opcion: "))
    radio = float(input("Ingresa el valor de radio del circulo: "))

    #crear un circulo como objeto con el dato especificado
    circulo = Circulo(radio)
    if calculo == 1:
        print(f"El area del circulo es: {circulo.area()}")
    elif calculo == 2:
        print(f"El perimetro del circulo es: {circulo.perimetro()}")