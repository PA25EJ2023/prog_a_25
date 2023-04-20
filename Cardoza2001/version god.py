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
    def area_triangulo(base,altura):
        A = (base*altura)/2
        return A

    def perimetro_triangulo(base,altura):
        P = math.sqrt(base**2 + altura**2)
        return P

class Circulo:
    def area_circulo(radio):
        A = math.pi * radio ** 2
        return A

    def perimetro_circulo(radio):
        P = 2 * math.pi * radio
        return P 












print ("Bienvenido")
print ("Opciones disponibles")
print ("1-Cuadrado\n2-Triangulo\n3-Circulo")
opcion = input("Elige una opción [1,2,3]:  ")
if opcion == 1:
    print ("Calculos disponibles: ")
    print ("1-Area\n2-Perimetro\n3-Diagonal")
    calculo = input("Elige una opción: ")
    lado = float (input("Ingresa el lado del cuadrado:"))
    if calculo == 1:
        A = area_cuadrado (lado)
        print ("El A es ",A)
    elif calculo == 2:
        P = perimetro_cuadrado (lado)
        print (" El P es: ", P)
    elif calculo == 3:
        D = diagonal_cuadrado (lado)
        print (" El P es: ", D)

elif opcion == 2:
    print ("Calculos disponibles: ")
    print ("1-Area\n2-Perimetro")
    calculo = input("Elige una opción: ")
    base = float (input("Ingresa la base del triangulo: "))
    altura = float (input("Ingresa la altura del triangulo: "))
    if calculo == 1:
        A = area_triangulo(base,altura)
        print ("El A del triangulo es ",A)
    elif calculo == 2:
        P = perimetro_triangulo(base,altura)
        print (" El P del triangulo es: ", P)
    
elif opcion == 3:
    print ("Calculos disponibles: ")
    print ("1-Area\n2-Perimetro")
    calculo = input("Elige una opción: ")
    radio = float (input("Ingresa el radio del circulo: ")) 
    if calculo == 1:
        A = area_circulo(radio)
        print ("El A del circulo es ",A)
    elif calculo == 2:
        P = perimetro_circulo(radio)
        print (" El P del circulo es: ", P)   
