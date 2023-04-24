import math 

class Cuadrado:
    def __init__(self , lado):
        self.lado = lado

    def area(self):
        a= self.lado * self.lado
        return a

    def perimetro(self):
        p= self.lado* 4
        return p

    def diagonal(self):
        d= self.lado * math.sqrt(2) 
        return d

class Trinagulo:

    pass

class circulo:
    pass

def area_cuadrado(lado):
    area= lado*lado
    return area

def perimetro_cuadrado(lado):
    perimetro= lado* 4
    return perimetro

def diagonal_cuadrado(lado):
    diagonal= lado * math.sqrt(2) 
    return diagonal

def area_triangulo(base,altura):
    area=(base * altura)/2
    return area

def perimetro_triangulo(base,altura):
    perimetro= math.sqrt(base**2 + altura**2)
    return perimetro

def area_circulo(radio):
    area=math.pi * radio
    return area 

def perimetro_circulo(radio):
    perimetro= math.pi * 2 * radio 
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

    if calculo ==1:
        area= area_cuadrado(lado) 
        print(F"El area es:{area}")

    elif calculo ==2 :
        perimetro = perimetro_cuadrado(lado)
        print(F"El perimetro es:{perimetro}") 

    elif calculo == 3:
        diagonal= diagonal_cuadrado(lado)
        print(F"La diadonal es:{diagonal}")

if opcion == 2: 
    print("Calculos disponibles")
    print("1.AREA\n2.PERIMETRO")
    calculo= int(input("Elige una opcion:"))

    base=float(input("ingresa la base:"))
    altura=float(input("ingresa la altura:"))
    
    if calculo== 1:
        area=area_triangulo(base,altura)
        print(F"El area es:{area}")
    elif calculo == 2:
        perimetro= perimetro_triangulo(base,altura)
        print(F"El perimetro es:{perimetro}")

if opcion == 3: 
    print("Calculos disponibles")
    print("1.AREA\n2.PERIMETRO")
    calculo= int(input("Elige una opcion:"))

    radio=float(input("ingresa el perimetro:"))
    
    
    if calculo== 1:
        area=area_circulo(radio)
        print(F"El area es:{area}")
    elif calculo == 2:
        perimetro= perimetro_circulo(radio)
        print(F"El perimetro es:{perimetro}")
