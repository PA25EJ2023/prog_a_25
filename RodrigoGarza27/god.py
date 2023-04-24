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
    def area(self,base,altura):
        a = (base * altura)/2
        return a
    
    def perimetro(self,base,altura):
        p = math.sqrt(base**2 + altura**2)
        return p

class Circulo:
    def area(self,radio):
        a = math.pi * radio ** 2
        return a

    def perimetro(self,radio):
        p = 2 * math.pi * radio
        return p


print("bienvenido")
print("Opciones disponibles")
print("1.Cuadrado\n2.Triangulo\n3.Circulo")
opcion= int(input("Elige una opcion [1,2,3]"))

if opcion ==1:
    print("Calculos disponibles")
    print("1.Area\n2.Perimetro\n3.Diagonal")
    calculo= int(input("Elige una opcion"))
    
    lado = float(input("ingresa el valor del lado"))
    
    if calculo == 1:
        area= area_cuadrado(lado)
        print(f"El area es {area}")
    elif calculo == 2:
        perimetro= perimetro_cuadrado(lado)
        print(f"El perimetro es {perimetro}")
    elif calculo == 3:
        diagonal= diagonal_cuadrado(lado)
        print(f"La diagonal es {diagonal}")
        
elif opcion ==2:
    print("Calculos disponibles")
    print("1.Area\n2.Perimetro")
    calculo= int(input("Elige una opcion"))
    
    base = float(input("ingresa el valor de la base"))
    altura = float(input("Ingresa la altura"))    
    if calculo == 1:
        area=area_triangulo(base,altura)
        print(f"El area es {area}")
    elif calculo == 2:
        perimetro= perimetro_triangulo(base,altura)
        print(f"El perimetro es {perimetro}")
        
elif opcion ==3:
    print("Calculos disponibles")
    print("1.Area\n2.Perimetro")
    calculo= int(input("Elige una opcion"))
    
    radio = float(input("Ingresa el radio"))
    
    if calculo == 1:
        area=area_circulo(radio)
        print(f"El area es {area}")
    elif calculo == 2:
        perimetro=perimetro_circulo(radio)
        print(f"El perimetro es {perimetro}")
        