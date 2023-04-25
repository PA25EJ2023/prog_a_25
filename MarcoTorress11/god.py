import math

class Cuadrado:
    def __init__(self,lado):
        self.lado = lado

    def area(self,):
        a = self.lado * self.lado
        return a

    def perimetro(self,):
        p = self.lado * 4
        return p

    def diagonal(self,):
        d = self.lado * math.sqrt(2)
        return d



class Triagulo:
    def __init__(self,base,altura):
        self.base = base
        self.altura = altura

    def area_trangulo(self):
        area = base * altura
        return area

    def perimetro_triangulo(self):
        perimetro = math.sqrt(base**2 + altura**2)
        return perimetro

class Circulo:
    def __init__(self,radio):
        self.radio = radio

    def area_circulo(self):
        area = math.pi * radio ** 2
        return area

    def perimetro_circulo(self):
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
