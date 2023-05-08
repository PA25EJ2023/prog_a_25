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
        print(f'color:{self.color},altura:{self.altura},ancho:{self.ancho},tipo:{self.tipo}')

class Zapato:
    def __init__(self,color,marca,talla,tipo):
        self.color = color
        self.marca = marca
        self.talla = talla
        self.tipo = tipo

    def imprimir(self):
        print(f'color:{self.color},marca:{self.marca},talla:{self.talla},tipo:{self.tipo}')

class Reloj:
    def __init__(self,marca,color,tipo,forma):
        self.marca = marca
        self.color = color
        self.tipo = tipo
        self.forma = forma

    def imprimir(self):
        print(f'marca:{self.marca},color:{self.color},tipo:{self.tipo},forma:{self.forma}')

class Tripie:
    def __init__(self,color,altura,marca):
        self.color = color
        self.altura = altura
        self.marca = marca

    def imprimir(self):
        print(f'color:{self.color},altura:{self.altura},marca:{self.marca}')

class Revista:
    def __init__(self,altura,ancho,nombre):
        self.altura = altura
        self.ancho = ancho
        self.nombre = nombre

    def imprimir(self):
        print(f'altura:{self.altura},ancho:{self.ancho},nombre:{self.nombre}') 

class Pilas:
    def __init__(self,marca,tamaño,altura,color,tipo):
        self.marca = marca
        self.tamaño = tamaño
        self.altura = altura
        self.color = color
        self.tipo = tipo

    def imprimir(self):
        print(f'marca:{self.marca},tamaño:{self.tamaño},altura:{self.altura},color:{self.color},tipo:{self.tipo}')    

class Maletin:
    def __init__(self,color,tamaño,tipo,ancho):
        self.color = color
        self.tamaño = tamaño
        self.tipo = tipo
        self.ancho = ancho

    def imprimir(self):
        print(f'color:{self.color},tamaño:{self.tamño},tipo:{self.tipo},ancho:{self.ancho}')

class Lapiz:
    def __init__(self,color,marca,altura,ancho):
        self.color = color 
        self.marca = marca
        self.altura = altura
        self.ancho = ancho

    def imprimir(self):
        print(f'color:{self.color},marca:{self.marca},altura:{self.altura},ancho:{self.ancho}') 

class Laptop:
    def __init__(self,marca,color,altura,ancho):
        self.marca = marca
        self.color = color
        self.altura = altura
        self.ancho = ancho

    def imprimir(self):
        print(f'marca:{self.marca},color:{self.color},altura:{self.altura},ancho:{self.ancho}')

class Cargador:
    def __init__(self,marca,color,tipo):
        self.marca = marca
        self.color = color
        self.tipo = tipo

    def imprimir(self):
        print(f'marca:{self.marca},color:{self.color},tipo:{self.tipo}')

class Lente_camara:
    def __init__(self,color,marca,forma):
        self.color = color
        self.marca = marca
        self.forma = forma

    def imprimir(self):
        print(f'color:{self.color},marca:{self.marca},forma:{self.forma}')

class Tapa_camara:
    def __init__(self,color,marca,forma):
       self.color = color
       self.marca = marca
       self.forma = forma

    def imprimir(self):
        print(f'color:{self.color},marca:{self.marca},forma:{self.forma}')

class Estuche_camara:
    def __init__(self,color,marca,tamaño):
        self.color = color
        self.marca = marca
        self.tamaño = tamaño

    def imprimir(self):
        print(f'color:{self.color},marca:{self.marca},tamaño:{self.tamaño}')

class Chaqueta:
    def __init__(self,marca,color,tamaño,tipo_forro):
        self.marca = marca
        self.color = color
        self.tamaño = tamaño
        self.tipo_forro = tipo_forro

    def imprimir(self):
        print(f'marca:{self.marca},color:{self.color},tamaño:{self.tamaño},tipo forro:{self.tipo_forro}') 
           

