import math

#CLASES
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

class Triangulo:
    def __init__(self,base,altura): #self representa el objeto(triangulo) y después los atributos
        self.base=base 
        self.altura=altura

    def area(self): 
        area = (self.base * self.altura) /2 #area es variable y base y altura atributos
        return area
        
    def perimetro(self):
        perimetro = math.sqrt( self.base **2 + self.altura **2 )
        return perimetro

class Circulo:
    def __init__(self,radio):
        self.radio=radio

    def area(self):
        area = math.pi * self.radio **2
        return area

    def perimetro(self):
        perimetro = math.pi * 2 * self.radio 
        return perimetro

print("Bienvenido")
print ("Opciones disponibles")
print ("1.Cuadrado\n2.Triangulo rectangulo\n3.Circulo")
opcion=int(input("Elige una opcion [1,2,3]"))  

if opcion == 1:
    print("Calculos disponibles")
    print("1.Area\n2.Perimetro\n3.Diagonal")
    calculo = int(input("Elige una opcion"))

    lado = float(input("Ingresa el valor del lado"))
    
    #crear un cuadrado con el lado especificado
    cuadrado=Cuadrado(lado)  #objeto que se llama cuadrado, es una creacion de objetos
    if calculo == 1:
        area = cuadrado.area()       
        print(f"El area es {area}")

    elif calculo == 2:
        perimetro = cuadrado.perimetro()
        print(f"El perimetro es {perimetro}")

    elif calculo == 3:
        diagonal = cuadrado.diagonal()
        print(f"La diagonal es {diagonal}")

elif opcion == 2:
    print("Calculos disponibles")
    print("1.-Area\n2.Perimetro")
    calculo = int(input("Elige una opcion"))

    base = float(input("Ingresa la base"))
    altura = float(input("Ingresa la altura"))
    
    triangulo=Triangulo(base,altura)
    if calculo == 1:
        area = triangulo.area()
        print(f"El area es {area}")
    elif calculo == 2:
        perimetro = triangulo.perimetro()
        print(f"El perimetro es {perimetro}")

elif opcion == 3:
    print("Calculos disponibles")
    print("1.-Area\n2.Perimetro")
    calculo = int(input("Elige una opcion"))

    radio = float(input("Ingresa el radio"))
    circulo=Circulo(radio)
    if calculo == 1:
        area = circulo.area()
        print(f"El area es {area}")
    elif calculo == 2:
        perimetro = circulo.perimetro()
        print(f"El perimetro es {perimetro}")