import math

###############################################################
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

##############################################################
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

# ##############################################################
class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        area = math.pi * self.radio ** 2
        return area

    def perimetro(self):
        perimetro = math.pi * 2 * self.radio 
        return perimetro 

print("BIENVENIDO")
print("Operaciones disponibles")
print("1.Cuadro\n2.Triangulo\n3.circulo")
opcion=int(input("Elige una opcion[1,2,3]:"))

if opcion == 1 :
    print("Calculos disponibles")
    print("1.AREA\n2.PERIMETRO\n3.DIAGONAL")
    calculo= int(input("Elige una opcion:"))

    lado = float(input("ingresa el valor de lado:"))

    #crear un cuadrado con el lado especificado  
    cuadrado= Cuadrado(lado)
    if calculo ==1:
        area= cuadrado.area() 
        print(F"El area es:{area}")

    elif calculo ==2 :
        perimetro = cuadrado.perimetro()
        print(F"El perimetro es:{perimetro}") 

    elif calculo == 3:
        diagonal= cuadrado.diagonal()
        print(F"La diadonal es:{diagonal}")

if opcion == 2: 
    print("Calculos disponibles")
    print("1.AREA\n2.PERIMETRO")
    calculo= int(input("Elige una opcion:"))

    base=float(input("ingresa la base:"))
    altura=float(input("ingresa la altura:"))
    triangulo= Triangulo(base,altura)
    if calculo== 1:
        area=triangulo.area()
        print(F"El area es:{area}")
    elif calculo == 2:
        perimetro= triangulo.perimetro()
        print(F"El perimetro es:{perimetro}")

if opcion == 3: 
    print("Calculos disponibles")
    print("1.AREA\n2.PERIMETRO")
    calculo= int(input("Elige una opcion:"))

    radio=float(input("ingresa el perimetro:"))
    
    circulo = Circulo(radio)
    if calculo== 1:
        area= circulo.area()
        print(F"El area es:{area}")
    elif calculo == 2:
        perimetro= circulo.perimetro()
        print(F"El perimetro es:{perimetro}")
