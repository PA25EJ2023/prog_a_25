class Estuche_camara:
    def __init__(self,tamaño,color,marca):
        self.tamaño=tamaño
        self.color=color
        self.marca = marca
         
    
    def imprimir(self):
        print(f"El estuche es de color:{self.color},su tamao es de:{self.tamaño}, y es de la marca:{self.marca}")

class Chaqueta:
    def __init__(self,talla,color):
        self.talla=talla
        self.color=color
         
    
    def imprimir(self):
        print(f"La chaqueta es de color:{self.color},y su talla es:{self.talla}")

class Marcador:
    def __init__(self,tamaño,color,marca):
        self.tamaño=tamaño
        self.color=color
        self.marca=marca
    
    def imprimir(self):
        print(f"El marcador es de color:{self.color},es de la marca {self.marca},y su tamaño es:{self.tamaño}")

class Lapiz:
    def __init__(self,tamaño,color,marca):
        self.tamaño=tamaño
        self.color=color
        self.marca= marca
    
    def imprimir(self):
        print(f"El lapiz es de color:{self.color},es de la marca {self.marca},y su tamaño es:{self.tamaño}")

class Zapatos:
    def __init__(self,talla,color,marca):
        self.talla=talla
        self.color=color
        self.marca= marca
    
    def imprimir(self):
        print(F"Los zapatos son color:{self.color},su talla es:{self.talla},y son de la marca{self.marca}")

class Tripie:
    def __init__(self,altura,color,marca):
        self.altura=altura
        self.color=color
        self.marca= marca
    
    def imprimir(self):
        print(F"El tripie es color:{self.color},tiene una altura de:{self.altura},y es de la marca{self.marca}")

class Reloj:
    def __init__(self,largo,color,marca):
        self.largo=largo
        self.color=color
        self.marca= marca
    
    def imprimir(self):
        print(F"El reloj es color:{self.color},tiene un largo de:{self.largo},y es de la marca{self.marca}")

class Pila:
    def __init__(self,duracion,color,marca):
        self.duracion=duracion
        self.color=color
        self.marca= marca
    
    def imprimir(self):
        print(F"La pila es color:{self.color},tiene una duracion de:{self.duracion},y es de la marca{self.marca}")

class lente:
    def __init__(self,tamaño,color,marca,precio):
        self.tamaño=tamaño
        self.color=color
        self.marca= marca
        self.precio=precio
    
    def imprimir(self):
        print(F"El lente es color:{self.color},tiene un tamaño de:{self.tamaño},cuesta {self.precio}, y es de la marca{self.marca}")

class Tapalen:
    def __init__(self,tamaño,color,marca,precio):
        self.tamaño=tamaño
        self.color=color
        self.marca= marca
        self.precio=precio
    
    def imprimir(self):
        print(F"La Tapa del lente es color:{self.color},tiene un tamaño de:{self.tamaño},cuesta {self.precio}, y es de la marca{self.marca}")

class Camisa:
    def __init__(self,color,marca,precio,tipo):
        self.color = color
        self.marca = marca
        self.precio = precio
        self.tipo = tipo

    def imprimir(self):
        print(f'color:{self.color},marca:{self.marca},precio:{self.precio},tipo:{self.tipo}')

class Celular:
    def __init__(self,color,altura,ancho,tipo):
        self.color = color
        self.altura = altura
        self.ancho = ancho
        self.tipo = tipo

    def imprimir(self):
        print(f'El celular es color:{self.color},tiene la altura de :{self.altura},y un ancho:{self.ancho},y es tipo:{self.tipo}')

class Revista:
    def __init__(self,altura,ancho,nombre):
        self.altura = altura
        self.ancho = ancho
        self.nombre = nombre

    def imprimir(self):
        print(f'Nombre:{self.nombre},altura:{self.altura},ancho:{self.ancho}')

class Maletin:
    def __init__(self,color,tamaño,tipo,ancho):
        self.color = color
        self.tamaño = tamaño
        self.tipo = tipo
        self.ancho = ancho

    def imprimir(self):
        print(f'color:{self.color},tamaño:{self.tamño},tipo:{self.tipo},ancho:{self.ancho}')

class Pila_cel:
    def __init__(self,duracion,color,marca):
        self.duracion=duracion
        self.color=color
        self.marca= marca
    
    def imprimir(self):
        print(F"La pila es color:{self.color},tiene una duracion de:{self.duracion},y es de la marca{self.marca}")

class Compu:
    def __init__(self,marca,color,capacidad):
        self.marca=marca
        self.color=color
        self.capacidad= capacidad

    
    def imprimir(self):
        print(F"La compu es color:{self.color},tiene una capacidad de:{self.capacidad},y es de la marca{self.marca}")

