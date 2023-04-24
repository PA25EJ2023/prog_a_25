import math
class Cuadrado:
    def __init__(self,lado):
        self.lado=lado
        
    def area(self):
        a=self.lado*self.lado
        return a
    
    def perimetro(self):
        p=self.lado*4
        return p
    
    def diagonal(self):
        d=self.lado*math.sqrt(2)
        return d

class Triangulo:

    def __init__(self,base,altura):
        self.base =base 
        self.altura = altura

    def area(self):
        a=self.base*self.altura/2
        return a
    
    def perimetro(self):
        p=math.sqrt(self.base**2 + self.altura**2)
        return p
    
class Circulo:
    def __init__(self,radio):
        self.radio=radio

    def area(self):
        a=math.pi * self.radio **2
        return a
    
    def perimetro(self):
        p=2 * math.pi * self.radio
        return p
    



