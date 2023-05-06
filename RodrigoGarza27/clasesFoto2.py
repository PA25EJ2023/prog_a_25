class Camisa:
    def __init__(self, color, material):
        self.color = color
        self.material = material

    def imprimir(self):
        print(f"Camisas- Color:{self.color}, Material:{self.material}")


class Laptop:
    def __init__(self, marca, color):
        self.marca = marca
        self.color = color 

    def imprimir(self):
        print(f"Laptop- Marca:{self.marca}, Color:{self.color}")


class Reloj:
    def __init__(self,color, tipo):
        self.color = color 
        self.tipo = tipo 

    def imprimir(self):
        print(f"Reloj- Color{self.color}, Tipo:{self.tipo}")


class Lente:
    def __init__(self, color, marca):
        self.color = color 
        self.marca = marca

    def imprimir(self):
        print(f"Lente de Camara- Color:{self.color}, Marca:{self.marca}")


class Revista:
    def __init__(self, titulo):
        self.titulo = titulo  

    def imprimir(self):
        print(f"Revista - Titulo:{self.titulo}")


class Maletin:
    def __init__(self, color):
        self.color = color  

    def imprimir(self):
        print(f"Maletin- Color:{self.color}")


class Cargador:
    def __init__(self, color, marca):
        self.color = color 
        self.marca = marca 
        
    def imprimir(self):
        print(f"Cargador de camara: Color:{self.color}, Marca:{self.marca}, Precio:{self.precio}, Cargador para camara:{self.tipo_camara}")


class Pluma:
    def __init__(self,color): 
        self.color = color 

    def imprimir(self):
        print(f"Pluma- Color:{self.color}")


class Lapiz:
    def __init__(self,color): 
        self.color = color 

    def imprimir(self):
        print(f"Lapiz- Color:{self.color}")


class Zapato:
    def __init__(self,color, talla): 
        self.color = color 
        self.talla = talla 

    def imprimir(self):
        print(f"Zapatos- Color:{self.color}, Talla:{self.talla}")


class Telefono:
    def __init__(self, color, tipo):
        self.color = color 
        self.tipo = tipo

    def imprimir(self):
        print(f"Telefono- Color:{self.color}, Tipo:{self.tipo}")


class Tripode:
    def __init__(self, color, tamano):
        self.color = color 
        self.tamano = tamano 

    def imprimir(self):
        print(f"Tripode- Color:{self.color}, Tamaño:{self.tamano}")
