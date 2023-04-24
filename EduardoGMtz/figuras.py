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
