import math

class Cuadrado:
    def __init__(self,lado):
        self.lado= lado
    def area (self):
        A = self.lado * self.lado
        return A
    def perimetro (self):
        P = self.lado *4
        return P
    def diagonal (self):
        D = self.lado* math.sqrt(2)
        return D

class Triangulo:
    def __init__(self,base,altura):
        self.base=base
        self.altura=altura

    def area (self):
        A = (self.base*self.altura)/2
        return A

    def perimetro (self):
        P = math.sqrt(self.base**2 + self.altura**2)
        return P

class Circulo:
    def __init__(self,radio):
        self.radio=radio

    def area (self):
        A = math.pi * self.radio ** 2
        return A

    def perimetro (self):
        P = 2 * math.pi * self.radio
        return P 
