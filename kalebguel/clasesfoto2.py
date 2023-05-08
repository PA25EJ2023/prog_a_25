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

class Zapatos:
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
        
            