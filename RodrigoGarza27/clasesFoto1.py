class Pluma:
    def __init__(self, color, tamano, marca,precio):
        self.color = color
        self.tamano = tamano
        self.marca = marca
        self.precio = precio 

    def imprimir(self):
        print(f"Pluma- Color: {self.color}, Tamaño: {self.tamano}, Marca: {self.marca}, Precio: {self.precio}")
        
class Marcador:
    def __init__(self, color, tamano, marca,precio):
        self.color = color 
        self.tamano = tamano
        self.marca = marca 
        self.precio = precio

    def imprimir(self):
        print(f"Marcadores- Color: {self.color}, Tamaño: {self.tamano}, Marca: {self.marca}, Precio: {self.precio}")
        
class Tijera:
    def __init__(self, color, tamano, marca,precio):
        self.color = color 
        self.tamano = tamano
        self.marca = marca 
        self.precio = precio

    def imprimir(self):
        print(f"Tijeras- Color: {self.color}, Tamaño: {self.tamano}, Marca: {self.marca}, Precio: {self.precio}") 

class Libreta:
    def __init__(self, color, num_hojas, marca, precio):
        self.color = color
        self.num_hojas = num_hojas
        self.marca = marca 
        self.precio = precio

    def imprimir(self):
        print(f"Libreta- Color:{self.color}, Numero de Hojas:{self.num_hojas}, Marca: {self.marca}, Precio: {self.precio}")

class Espejo:
    def __init__(self, forma, color,tamano,precio):
        self.forma = forma 
        self.color = color 
        self.tamano = tamano
        self.precio = precio

    def imprimir(self):
        print(f"Espejo- Forma: {self.forma}, Color: {self.color}, Tamaño: {self.tamano}, Precio: {self.precio}")

class Estuche:
    def __init__(self,color,forma,tamano,precio ):
        self.color = color
        self.forma = forma
        self.tamano = tamano
        self.precio = precio
        
    def imprimir(self):
        print(f"Estuche- Color: {self.color}, Forma: {self.forma}, Tamaño: {self.tamano}, Precio: {self.precio}")

class Regla:
    def __init__(self,color,forma,tamano,precio ):
        self.color = color
        self.forma = forma
        self.tamano = tamano
        self.precio = precio

    def imprimir(self):
        print(f"Regla- Color: {self.color}, Forma: {self.forma}, Tamaño: {self.tamano}, Precio: {self.precio}")

class Pegamento:
    def __init__(self,tipo,marca,tamano,precio):
        self.tipo = tipo
        self.marca = marca 
        self.tamano = tamano
        self.precio = precio

    def imprimir(self):
        print(f"Pegamento- Tipo: {self.tipo}, Marca: {self.marca}, Tamaño: {self.tamano}, Precio: {self.precio}")

class Esmalte:
    def __init__(self, color,precio,marca,tipo):
        self.color = color
        self.precio = precio
        self.marca = marca
        self.tipo = tipo

    def imprimir(self):
        print(f"Esmalte- Color: {self.color}, Precio: {self.precio}, Marca: {self.marca}, Tipo: {self.tipo}")

class Labial:
    def __init__(self, color,forma,tamano,precio):
        self.color = color 
        self.forma = forma
        self.tamano = tamano
        self.precio = precio

    def imprimir(self):
        print(f"Labial- Color: {self.color}, Forma: {self.forma}, Tamaño: {self.tamano}, Precio: {self.precio}")

class Cuenta:
    def __init__(self, color,tipo,marca,tamano):
        self.color = color 
        self.tipo = tipo
        self.marca = marca 
        self.tamano = tamano
    def imprimir(self):
        print(f"Color: {self.color}, Tipo: {self.tipo}, Marca: {self.marca}, Tamaño: {self.tamano}")

class Cinta:
    def __init__(self, color, longitud, marca, precio):
        self.color = color 
        self.longitud = longitud 
        self.marca = marca 
        self.precio = precio
    def imprimir(self):
        print(f"Cintas- Color: {self.color}, Longitud: {self.longitud}, Marca: {self.marca}, Precio: {self.precio}")

class Telefono:
    def __init__(self, color, tipo,tamano,precio):
        self.color = color 
        self.tipo = tipo 
        self.tamano = tamano
        self.precio = precio
    def imprimir(self):
        print(f"Telefono- Color: {self.color}, Tipo: {self.tipo}, Tamaño: {self.tamano}, Precio: {self.precio}")

class Sticker:
    def __init__(self, forma, color,tamano,precio):
        self.forma = forma
        self.color = color 
        self.tamano = tamano
        self.precio = precio
    def imprimir(self):
        print(f"Stickers- Forma: {self.forma}, Color: {self.color}, Tamaño: {self.tamano}, Precio: {self.precio}")

class Pinza:
    def __init__(self, color, tamano, forma,precio):
        self.color = color 
        self.tamano = tamano 
        self.forma = forma
        self.precio = precio

    def imprimir(self):
        print(f"Pinzas para el pelo- Color: {self.color}, Tamaño: {self.tamano}, Forma: {self.forma}, Precio: {self.precio}")

class Postal:
    def __init__(self, tamano, imagen,forma,precio):
        self.tamano = tamano 
        self.imagen = imagen 
        self.forma = forma
        self.precio = precio

    def imprimir(self):
        print(f"Postal- Tamaño: {self.tamano}, Imagen: {self.imagen}, Forma: {self.forma}, Precio: {self.precio}")

class Marco:
    def __init__(self, tamano, color, forma, imagen):
        self.tamano = tamano 
        self.color = color 
        self.forma = forma 
        self.imagen = imagen

    def imprimir(self):
        print(f"Marco Para Fotos- Tamaño: {self.tamano}, Color: {self.color}, Forma: {self.forma}, Imagen: {self.imagen}") 
