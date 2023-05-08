class Pegamento:
    def __init__(self,color,forma,altura,ancho):
        self.color = color
        self.forma = forma
        self.altura = altura
        self.ancho = ancho

    def imprimir(self):
        print(f'Color:{self.color},forma:{self.forma},altura:{self.altura},ancho:{self.ancho}')

class Pluma:
    def __init__(self,color,altura,ancho):
        self.color = color
        self.altura = altura
        self.ancho = ancho

    def imprimir(self):
        print(f'Color:{self.color},altura:{self.altura},ancho:{self.ancho}')

class Libreta:
    def __init__(self,color,tipo,altura,ancho):
        self.color = color
        self.tipo = tipo
        self.altura = altura
        self.ancho = ancho

    def imprimir(self):
       print(f'Color:{self.color},Tipo:{self.tipo},Altura:{self.altura},Ancho:{self.ancho}')

class Cuadro:
    def __init__(self,color,forma,altura,ancho):
        self.color = color
        self.forma = forma
        self.altura = altura
        self.ancho = ancho

    def imprimir(self):
        print(f'Color:,{self.color},Forma:{self.forma},Altura:{self.altura},Ancho:{self.ancho}')


class Cinta:
    def __init__(self,color,tamaño,ancho):
        self.color = color
        self.tamaño = tamaño
        self.ancho = ancho

    def imprimir(self):
        print(f'Color:{self.color},Tamaño:{self.tamaño},Ancho:{self.ancho}')
        
class Pintura_uñas:
    def __init__(self,forma,color,ancho,altura):
        self.forma = forma
        self.color = color
        self.ancho = ancho
        self.altura = altura

    def imprimir(self):
        print(f'Forma:{self.forma},Color:{self.color},Ancho:{self.ancho},Altura:{self.altura}')

class Tijera:
    def __init__(self,tipo,color,marca):
        self.tipo = tipo
        self.color = color
        self.marca = marca

    def imprimir(self):
        print(f'Tipo:{self.tipo},color:{self.color},Marca:{self.marca}')

class Telefono:
    def __init__(self,color,tipo,ancho):
        self.color = color
        self.tipo = tipo
        self.ancho = ancho

    def imprimir(self):
        print(f'color: {self.color},tipo:{self.tipo},ancho:{self.ancho}')

class Sticker:
    def __init__(self,color,forma,tamaño):
        self.color = color
        self.forma = forma
        self.tamaño = tamaño

    def imprimir(self):
        print(f'color:{self.color},forma:{self.forma},tamaño:{self.tamaño}')

class Marcador:
    def __init__(self,color,marca,tipo,tipo_punta):
        self.color = color
        self.marca = marca
        self.tipo = tipo
        self.tipo_punta = tipo_punta
    
    def imprimir(self):
        print(f'color:{self.color},marca:{self.marca},tipo:{self.tipo},tipo punta:{self.tipo_punta}')

class Labial:
    def __init__(self,color,altura,ancho):
        self.color = color
        self.altura = altura
        self.ancho = ancho
    
    def imprimir(self):
        print(f'Color:{self.color},Altura:{self.altura},Ancho:{self.ancho}')

class Espejo:
    def __init__(self):
        pass

class Telefono:
    def __init__(self):
        pass

class Poster:
    def __init__(self):
        pass

class Pinza_pelo:
    def __init__(self):
        pass    