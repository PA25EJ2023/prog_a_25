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