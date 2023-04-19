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
        d= self.lado * math.sqrt(2)
        return d
class Triangulo:
    def __init__(self,base,altura):
        self.base=base
        self.altura=altura

    def area(self):
        a= (self.base*self.altura)/2
        return a
    def perimetro(self):
        p = math.sqrt(self.base**2+self.altura**2)
        return p
class Circulo:
    def __init__(self,radio):
        self.radio=radio

    def area(self):
        a= math.pi*self.radio**2
        return a
    def perimetro(self):
        p = math.pi*2*self.radio
        return p


print("Bienvenido al Programa")
print("Opciones disponibles")
print("1.Cuadrado\n2.Triangulo Rectangulo\n3.Circulo")
opcion=int(input("Elige una opcion[1,2,3]: "))

if opcion == 1:
    print("Calculos disponibles")
    print("1.Area\n2.Perimetro\n3.Diagonal")
    calculo=int(input("Que calculo desea: "))

    lado=float(input("Ingrese el valor del lado: "))
    if calculo==1:
        area=Cuadrado(lado).area
        print(f'El area es {area}')
    elif calculo==2:
        perimetro= Cuadrado(lado).perimetro
        print(f'El perimetro es {perimetro}')
    elif calculo==3:
        diagonal=Cuadrado(lado).diagonal
        print(f'El diagonal es {diagonal}')
elif opcion == 2:
    print("Calculos disponibles")
    print("1.Area\n2.Perimetro")
    calculo=int(input("Que calculo desea:"))

    base=float(input("Ingresa la base: "))
    altura=float(input("Ingresa la altura: "))
    if calculo==1:
        area= Triangulo(base,altura).area
        print(f'El area es: {area}')
    elif calculo==2:
        perimetro = Triangulo(base,altura).perimetro
        print(f'El perimetro es {perimetro}')
elif opcion == 3:
    print("Calculos disponibles")
    print("1.Area\n2.Perimetro")
    calculo=int(input("Que calculo desea:"))

    radio=float(input("Ingrese el radio: "))
    if calculo==1:
        area= Circulo(radio).area
        print(f'El area es: {area}')
    elif calculo==2:
        perimetro = Circulo(radio).perimetro
        print(f'El perimetro es {perimetro}')

