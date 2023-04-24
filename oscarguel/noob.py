import math 
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
        area= lado * lado 
        print(F"El area es:{area}") 
    elif calculo ==2 :
        perimetro = lado*4
        print(F"El perimetro es:{perimetro}") 
    elif calculo == 3:
        diagonal= lado * math.sqrt(2) 
        print(F"La diadonal es:{diagonal}")

if opcion == 2: 
    print("Calculos disponibles")
    print("1.AREA\n2.PERIMETRO")
    calculo= int(input("Elige una opcion:"))

    base=float(input("ingresa la base:"))
    altura=float(input("ingresa la altura:"))
    
    if calculo== 1:
        area=(base * altura)/2
        print(F"El area es:{area}")
    elif calculo == 2:
        perimetro= math.sqrt(base**2 + altura**2)
        print(F"El perimetro es:{perimetro}")

if opcion == 3: 
    print("Calculos disponibles")
    print("1.AREA\n2.PERIMETRO")
    calculo= int(input("Elige una opcion:"))

    radio=float(input("ingresa el perimetro:"))
    
    
    if calculo== 1:
        area=math.pi * radio
        print(F"El area es:{area}")
    elif calculo == 2:
        perimetro= 2 * math.pi * radio 
        print(F"El perimetro es:{perimetro}")
