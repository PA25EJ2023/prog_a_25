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



print ("Bienvenido")
print ("Opciones disponibles")
print ("1-Cuadrado\n2-Triangulo\n3-Circulo")
opcion = int(input("Elige una opción [1,2,3]:  "))
if opcion == 1:
    print ("Calculos disponibles: ")
    print ("1-Area\n2-Perimetro\n3-Diagonal")
    calculo = int(input("Elige una opción: "))
    lado = float (input("Ingresa el lado del cuadrado:"))

    #crear un cuadrado con el lado especificado
    cuadrado=Cuadrado(lado)
    if calculo == 1:
        A = cuadrado.area()
        print ("El area del cuadrado es ",A)
    elif calculo == 2:
        P = cuadrado.perimetro()
        print (" El perimetro del cuadrado es: ", P)
    elif calculo == 3:
        D = cuadrado.diagonal()
        print (" la diagonal del cuadrado es: ", D)

elif opcion == 2:
    print ("Calculos disponibles: ")
    print ("1-Area\n2-Perimetro")
    calculo = int(input("Elige una opción: "))
    base = float (input("Ingresa la base del triangulo: "))
    altura = float (input("Ingresa la altura del triangulo: "))
    triangulo=Triangulo(base,altura)
    if calculo == 1:
        A = triangulo.area() 
        print ("El A del triangulo es ",A)
    elif calculo == 2:
        P = triangulo.perimetro()
        print (" El P del triangulo es: ", P)
    
elif opcion == 3:
    print ("Calculos disponibles: ")
    print ("1-Area\n2-Perimetro")
    calculo = int(input("Elige una opción: "))
    radio = float (input("Ingresa el radio del circulo: ")) 
    circulo= Circulo(radio)
    if calculo == 1:
        A = circulo.area()
        print ("El A del circulo es ",A)
    elif calculo == 2:
        P = circulo.perimetro
        print (" El P del circulo es: ", P)   
