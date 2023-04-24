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

    def diagonal(self):
        d = self.lado * math.sqrt(2)
        return d

class Triangulo:
    def __init__(self,base,altura):
        self.base = base
        self.altura = altura

    def area(self):
        area = (self.base * self.altura) / 2
        return area

    def perimetro(self):
        perimetro = math.sqrt(self.base **2 + self.altura **2)
        return perimetro

class Circulo:
    def __init__(self,radio):
        self.radio = radio

    def area(self):
        area = math.pi * self.radio **2
        return area

    def perimetro(self):
        perimetro = 2 * math.pi * self.radio
        return perimetro