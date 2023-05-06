class Pluma:
    def __init__(self, color, tamano, marca):
        self.color = color
        self.tamano = tamano
        self.marca = marca 
    def imprimir(self):
        print(f"Pluma- Color: {self.color}, Tamaño: {self.tamano}, Marca: {self.marca}")
        
class Marcador:
    def __init__(self, color):
        self.color = color 


    def imprimir(self):
        print(f"Marcadores- Color: {self.color}")
        
class Tijera:
    def __init__(self, color, marca):
        self.color = color
        self.marca = marca 

    def imprimir(self):
        print(f"Tijeras- Color: {self.color}, Marca: {self.marca}") 

class Labial:
    def __init__(self, color):
        self.color = color 

    def imprimir(self):
        print(f"Labial- Color: {self.color}")


class Esmalte:
    def __init__(self, color):
        self.color = color 

    def imprimir(self):
        print(f"Esmalte- Color: {self.color} ")


class Espejo:
    def __init__(self, forma, color):
        self.forma = forma 
        self.color = color 

    def imprimir(self):
        print(f"Espejo- Forma: {self.forma}, Color: {self.color}")


class Libreta:
    def __init__(self, color, num_hojas):
        self.color = color
        self.num_hojas = num_hojas

    def imprimir(self):
        print(f"Libreta- Color:{self.color}, Numero de Hojas:{self.num_hojas}")


class Telefono:
    def __init__(self, color, tipo):
        self.color = color 
        self.tipo = tipo 
        
    def imprimir(self):
        print(f"Telefono- Color: {self.color}, Tipo: {self.tipo}")

class Cinta:
    def __init__(self, color, longitud):
        self.color = color 
        self.longitud = longitud 

    def imprimir(self):
        print(f"Cintas- Color: {self.color}, Longitud: {self.longitud}")


class Cuenta:
    def __init__(self, color):
        self.color = color 

    def imprimir(self):
        print(f"Color: {self.color}")


class Sticker:
    def __init__(self, forma, color):
        self.forma = forma
        self.color = color 

    def imprimir(self):
        print(f"Stickers- Forma: {self.forma}, Color: {self.color}")

class Pinza:
    def __init__(self, color, tamano):
        self.color = color 
        self.tamano = tamano 

    def imprimir(self):
        print(f"Pinzas para el pelo- Color: {self.color}, Tamaño: {self.tamano}")

class Pegamento:
    def __init__(self,tipo,marca):
        self.tipo = tipo
        self.marca = marca 

    def imprimir(self):
        print(f"Pegamento- Tipo: {self.tipo}, Marca: {self.marca}")


class Postal:
    def __init__(self, tamano, imagen):
        self.tamano = tamano 
        self.imagen = imagen 

    def imprimir(self):
        print(f"Imagen- Tamaño: {self.tamano}, Imagen: {self.imagen}")

class Estuche:
    def __init__(self,color,forma ):
        self.color = color
        self.forma = forma
        
    def imprimir(self):
        print(f"Estuche- Color: {self.color}, forma: {self.forma}" )

class Regla:
    def __init__(self,color,forma ):
        self.color = color
        self.forma = forma
        
class Marco:
    def __init__(self, tamano, color, forma, imagen):
        self.tamano = tamano 
        self.color = color 
        self.forma = forma 
        self.imagen = imagen

    def imprimir(self):
        print(f"Marco Para Fotos- Tamaño: {self.tamano}, Color: {self.color}, Forma: {self.forma}, Imagen: {self.imagen}") 
