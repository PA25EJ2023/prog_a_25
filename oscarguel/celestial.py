import math
from figuras import Cuadrado ,Circulo, Triangulo 


print("BIENVENIDO")
print("Operaciones disponibles")
print("1.Cuadro\n2.Triangulo\n3.circulo")
opcion=int(input("Elige una opcion[1,2,3]:"))

if opcion == 1 :
    print("Calculos disponibles")
    print("1.AREA\n2.PERIMETRO\n3.DIAGONAL")
    calculo= int(input("Elige una opcion:"))

    lado = float(input("ingresa el valor de lado:"))

    #crear un cuadrado con el lado especificado  
    cuadrado= Cuadrado(lado)
    if calculo ==1:
        area= cuadrado.area() 
        print(F"El area es:{area}")

    elif calculo ==2 :
        perimetro = cuadrado.perimetro()
        print(F"El perimetro es:{perimetro}") 

    elif calculo == 3:
        diagonal= cuadrado.diagonal()
        print(F"La diadonal es:{diagonal}")

if opcion == 2: 
    print("Calculos disponibles")
    print("1.AREA\n2.PERIMETRO")
    calculo= int(input("Elige una opcion:"))

    base=float(input("ingresa la base:"))
    altura=float(input("ingresa la altura:"))
    triangulo= Triangulo(base,altura)
    if calculo== 1:
        area=triangulo.area()
        print(F"El area es:{area}")
    elif calculo == 2:
        perimetro= triangulo.perimetro()
        print(F"El perimetro es:{perimetro}")

if opcion == 3: 
    print("Calculos disponibles")
    print("1.AREA\n2.PERIMETRO")
    calculo= int(input("Elige una opcion:"))

    radio=float(input("ingresa el perimetro:"))
    
    circulo = Circulo(radio)
    if calculo== 1:
        area= circulo.area()
        print(F"El area es:{area}")
    elif calculo == 2:
        perimetro= circulo.perimetro()
        print(F"El perimetro es:{perimetro}")
