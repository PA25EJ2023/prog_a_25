import math 

class Cuadrado:

    def __innit__(self,lado):
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

    def __innit__(self,base,altura):
        self.base = base
        self.altura = altura 
    
    def area_triangulo(self):
        a = (self.base * self.altura) /2
        return a
    
    def perimetro_triangulo(self):
        p = math.sqrt(self.base**2 + self.altura**2)
        return p 
    
class Circulo: 

    def __innit__(self,radio):
        self.radio = radio

    def area_circulo(self):
        a = math.pi * self.radio**2
        return a
    
    def perimetro_circulo(self):
        p = 2 * math.pi * self.radio 
        return p 




print("Bienvenido:D")
print("Opciones disponibles:")
print("1. Cuadrado \n2. Triangulo Rectangulo. \n3. Circulo ")
opcion = int(input("Ingrese una opción [1,2,3] \n>> "))

if opcion == 1:
    print("Calculos Disponibles: ")
    print("1. Area \n2. Perimetro \n3. Diagonal ")
    calculo = int(input("Eliga una opción:  "))

    lado = float(input("Ingrese el valor de un lado: "))

    if calculo == 1:
        area = area_cuadrado(lado)
        print(f"El area es: {area}")
    elif calculo == 2:
        perimetro = perimetro_cuadrado(lado)
        print(f"El perimetro es: {perimetro}")
    elif calculo == 3:
        diagonal = diagonal_cuadrado(lado)
        print(f"La diagonal es: {diagonal}")

elif opcion == 2:
    print("Calculos disponibles: ")
    print("1. Area \n2. Perimetro")
    calculo = int(input("Eliga una opción:"))

    base = float(input("Ingrese la base: "))
    altura = float(input("Ingrese la altura:"))

    if calculo == 1:
        area = area_triangulo(base, altura)
        print(f"El area es: {area}")
    elif calculo == 2:
        perimetro = perimetro_triangulo(base, altura)
        print(f"El perimetro es: {perimetro}")

elif opcion == 3:
    print("Calculos Disponibles: ")
    print("1. Area \n2. Perimetro")
    calculo = int(input("Eliga una opción: "))

    radio = float(input("Ingrese el radio: "))

    if calculo == 1:
        area = area_circulo(radio)
        print(f"El area es: {area}")
    elif calculo == 2:
        perimetro = perimetro_circulo(radio)
        print(f"El perimetro es: {perimetro}")
