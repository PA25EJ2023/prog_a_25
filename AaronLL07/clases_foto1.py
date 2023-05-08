class Esmalte:
    
    def __init__(self, color, tamano, forma):
        self.color = color
        self.tamano = tamano
        self.forma = forma

    def imprimir(self):
        print(f"Color: {self.color}\nTamaño: {self.tamano}\nForma: {self.forma}")

class Marco_foto:
    
    def __init__(self, color, forma, tamano, descripcion):
        self.color = color
        self.forma = forma
        self.tamano = tamano
        self.descripcion = descripcion

    def imprimir(self):
        print(f"Color: {self.color}\nForma: {self.forma}\nTamaño: {self.tamano}\nDescripción: {self.descripcion}")

class Labial:

    def __init__(self, color, tamano, marca, forma):
        self.color = color
        self.tamano = tamano
        self.marca = marca
        self.forma = forma

    def imprimir(self):
        print(f"Color: {self.color}\nTamaño: {self.tamano}\nMarca: {self.marca}\nForma: {self.forma}")

class Cinta:

    def __init__(self, color, ancho, tamano, material):
        self.color = color
        self.ancho = ancho
        self.tamano = tamano
        self.material = material

    def imprimir(self):
        print(f"Color: {self.color}\nAncho: {self.ancho}\nTamaño: {self.tamano}\nMaterial: {self.material}")

class Boligrafo:

    def __init__(self, tipo, color, marca, tamano, precio):
        self.tipo = tipo
        self.color = color
        self.marca = marca
        self.tamano = tamano
        self.precio = precio

    def imprimir(self):
        print(f"Tipo: {self.tipo}\nColor: {self.color}\nMarca: {self.marca}\nTamaño: {self.tamano}\nPrecio: {self.precio}")

class Cuenta:

    def __init__(self, color, tamano, forma, cantidad):
        self.color = color
        self.tamano = tamano
        self.forma = forma
        self.cantidad = cantidad
    
    def imprimir(self):
        print(f"Color: {self.color}\nTamaño: {self.tamano}\nForma: {self.forma}\nCantidad: {self.cantidad}") 

class Espejo:
    
    def __init__(self, forma, tamano, color):
        self.forma = forma
        self.tamano = tamano
        self.color = color

    def imprimir(self):
        print(f"Forma: {self.forma}\nTamaño: {self.tamano}\nColor: {self.color}")

class Telefono:

    def __init__(self, tipo, color, tamano):
        self.tipo = tipo
        self.color = color
        self.tamano = tamano
    
    def imprimir(self):
        print(f"Tipo: {self.tipo}\nColor: {self.color}\nTamaño: {self.tamano}")

class Cuaderno:

    def __init__(self, tipo, color, tamano):
        self.tipo = tipo
        self.color = color
        self.tamano = tamano

    def imprimir(self):
        print(f"Tipo: {self.tipo}\nColor: {self.color}\nTamaño: {self.tamano}")

class Poster:

    def __init__(self, contenido, tamano):
        self.contenido = contenido
        self.tamano = tamano

    def imprimir(self):
        print(f"Contenido: {self.contenido}\nTamaño: {self.tamano}")

class Tijera:  
    
    def __init__(self, tipo_punta, color, tamano):
        self.tipo_punta = tipo_punta
        self.color = color
        self.tamano = tamano

    def imprimir(self):
        print(f"Tipo de punta: {self.tipo_punta}\nColor: {self.color}\nTamaño: {self.tamano}")

class Pegamento:

    def __init__(self, tipo, color, tamano):
        self.tipo = tipo
        self.color = color
        self.tamano = tamano

    def imprimir(self):
        print(f"Tipo: {self.tipo}\nColor: {self.color}\nTamaño: {self.tamano}")

class Pinza:

    def __init__(self, color, tamano, material):
        self.color = color
        self.tamano = tamano
        self.material = material

    def imprimir(self):
        print(f"Pinza: {self.color}\nTamaño: {self.tamano}\nMaterial: {self.material}")

class Pegatina:

    def __init__(self, forma, color, tamano, cantidad):
        self.forma = forma
        self.color = color
        self.tamano = tamano
        self.cantidad = cantidad

    def imprimir(self):
        print(f"Forma: {self.forma}\nColor: {self.color}\nTamaño: {self.tamano}\nCantidad: {self.cantidad}")