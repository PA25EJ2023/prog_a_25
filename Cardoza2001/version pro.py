import math
def area_cuadrado(lado):
    area = lado * lado
    return area

def perimetro_cuadrado(lado):
    perimetro = lado *4
    return perimetro

def diagonal_cuadrado(lado):
    diagonal = lado* math.sqrt(2)
    return diagonal

def area_triangulo(base,altura):
    area = (base*altura)/2
    return area

def perimetro_triangulo(base,altura):
    perimetro = math.sqrt(base**2 + altura**2)
    return perimetro

def area_circulo(radio):
    area = math.pi * radio ** 2
    return area

def perimetro_circulo(radio):
    perimetro = 2 * math.pi * radio
    return perimetro





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
        area = area_cuadrado (lado)
        print ("El area es ",area)
    elif calculo == 2:
        perimetro = perimetro_cuadrado (lado)
        print (" El perimetro es: ", perimetro)
    elif calculo == 3:
        diagonal = diagonal_cuadrado (lado)
        print (" El perimetro es: ", diagonal)

elif opcion == 2:
    print ("Calculos disponibles: ")
    print ("1-Area\n2-Perimetro")
    calculo = input("Elige una opción: ")
    base = float (input("Ingresa la base del triangulo: "))
    altura = float (input("Ingresa la altura del triangulo: "))
    if calculo == 1:
        area = area_triangulo(base,altura)
        print ("El area del triangulo es ",area)
    elif calculo == 2:
        perimetro = perimetro_triangulo(base,altura)
        print (" El perimetro del triangulo es: ", perimetro)
    
elif opcion == 3:
    print ("Calculos disponibles: ")
    print ("1-Area\n2-Perimetro")
    calculo = input("Elige una opción: ")
    radio = float (input("Ingresa el radio del circulo: ")) 
    if calculo == 1:
        area = area_circulo(radio)
        print ("El area del circulo es ",area)
    elif calculo == 2:
        perimetro = perimetro_circulo(radio)
        print (" El perimetro del circulo es: ", perimetro)   
