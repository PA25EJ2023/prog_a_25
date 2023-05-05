# https://www.pexels.com/es-es/foto/escritorio-oficina-escritura-boligrafos-10605242/
# https://www.pexels.com/es-es/foto/bolso-de-cuero-marron-ropa-y-macbook-57750/

class Esmalte:
    
    def __init__(self, color, tamano, forma):
        self.color = color
        self.tamano = tamano
        self.forma = forma

    def imprimir(self):
        print(f"{self.color} {self.forma} {self.tamano} {self.sticker}")

class Marco_foto:
    
    def __init__(self, color, forma, tamano):
        self.color = color
        self.forma = forma
        self.tamano = tamano

    def imprimir(self):
        print(f"{self.color} {self.forma} {self.tamano}")

class Labial:

    def __init__(self, color, tamano, marca):
        self.color = color
        self.tamano = tamano
        self.marca = marca

    def imprimir(self):
        print(f"{self.color} {self.tamano} {self.marca}")

class Cinta:

    def __init__(self, color, ancho, tamano, material):
        self.color = color
        self.ancho = ancho
        self.tamano = tamano
        self.material = material

    def imprimir(self):
        print(f"{self.color} {self.ancho} {self.tamano} {self.material}")

class Boligrafo:

    def __init__(self, tipo, color, marca, tamano):
        self.tipo = tipo
        self.color = color
        self.marca = marca
        self.tamano = tamano

    def imprimir(self):
        print(f"{self.tipo} {self.color} {self.marca} {self.tamano}")

class Cuenta:

    def __init__(self, color, tamano, forma):
        self.color = color
        self.tamano = tamano
        self.forma = forma
    
    def imprimir(self):
        print(f"{self.color} {self.tamano} {self.forma}") 

class Espejo:
    
    def __init__(self, forma, tamano, color):
        self.forma = forma
        self.tamano = tamano
        self.color = color

    def imprimir(self):
        print(f"{self.forma} {self.tamano} {self.color}")

class Telefono:

    def __init__(self, tipo, color, tamano):
        self.tipo = tipo
        self.color = color
        self.tamano = tamano
    
    def imprimir(self):
        print(f"{self.tipo} {self.color} {self.tamano}")

class Cuaderno:

    def __init__(self, tipo, color, tamano):
        self.tipo = tipo
        self.color = color
        self.tamano = tamano

    def imprimir(self):
        print(f"{self.tipo} {self.color} {self.tamano}")

class Poster:

    def __init__(self, contenido, tamano):
        self.contenido = contenido
        self.tamano = tamano

    def imprimir(self):
        print(f"{self.tamano}")

class Tijeras:  
    
    def __init__(self, tipo_punta, color, tamano):
        self.tipo_punta = tipo_punta
        self.color = color
        self.tamano = tamano

    def imprimir(self):
        print(f"{self.tipo_punta} {self.tamano}")

class Pegamento:

    def __init__(self, tipo, color, tamano):
        self.tipo = tipo
        self.color = color
        self.tamano = tamano

    def imprimir(self):
        print(f"{self.tipo} {self.color} {self.tamano}")

class Pinza:

    def __init__(self, color, tamano, material):
        self.color = color
        self.tamano = tamano
        self.material = material

    def imprimir(self):
        print(f"{self.color} {self.tamano} {self.material}")

class Pegatina:

    def __init__(self, forma, color, tamano):
        self.forma = forma
        self.color = color
        self.tamano = tamano

    def imprimir(self):
        print(f"{self.forma} {self.color} {self.tamano}")