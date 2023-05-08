class Cinta:
    def __init__(self,color,ancho,largo,marca,material,tamano):
        self.color = color
        self.ancho = ancho
        self.largo = largo
        self.marca = marca
        self.material = material
        self.tamano = tamano

    def imprimir(self):
        print(f"Color: {self.color}\nAncho: {self.ancho}\nLargo: {self.largo}\nMarca: {self.marca}\nMaterial: {self.material}\nTamano: {self.tamano}")

class Labial:
    def __init__(self,marca,tono,acabado,tamano):
        self.marca = marca
        self.tono = tono 
        self.acabado = acabado 
        self.tamano = tamano

    def imprimir(self):
        print(f"Marca: {self.marca}\nTono: {self.tono}\nAcabado: {self.acabado}\nTamano: {self.tamano}")

class Espejo:
    def __init__(self,forma,color,marca,tamano):
        self.forma = forma
        self.color = color
        self.marca = marca
        self.tamano = tamano

    def imprimir(self):
        print(f"Forma: {self.forma}\nColor: {self.color}\nMarca: {self.marca}\nTamano: {self.tamano}")

class Telefono:
    def __init__(self,tipo,tamano,color,precio):
        self.tipo = tipo
        self.tamano = tamano 
        self.color = color
        self.precio = precio

    def imprimir(self):
        print(f"Tipo: {self.tipo}\nTamano: {self.tamano}\nColor: {self.color}\nPrecio: {self.precio}")

class Cuaderno:
    def __init__(self,tipo,color,tamano,precio):
        self.color = color
        self.tipo = tipo
        self.tamano = tamano
        self.precio = precio

    def imprimir(self):
        print(f"Color: {self.color}\nTipo: {self.tipo}\nTamano: {self.tamano}\nPrecio: {self.precio}")

class Poster:
    def __init__(self,contenido,tamano,imagen,color):
        self.contenido = contenido
        self.tamano = tamano
        self.imagen = imagen
        self.color = color

    def imprimir(self):
        print(f"Contenido: {self.contenido}\nTamano: {self.tamano}\nImagen: {self.imagen}\nColor: {self.color}")

class Tijeras:
    def __init__(self,tipo_punta,color,tamano,precio):
        self.tipo_punta = tipo_punta
        self.color = color
        self.tamano = tamano
        self.precio = precio

    def imprimir(self):
        print(f"Tipo de punta: {self.tipo_punta}\nColor: {self.color}\nTamano: {self.tamano}\nPrecio: {self.precio}")
    
class Pegamento:
    def __init__(self,tamano,tipo,color,marca):
        self.tamano = tamano
        self.tipo = tipo
        self.color = color
        self.marca = marca

    def imprimir(self):
        print(f"Tamano: {self.tamano}\nTipo: {self.tipo}\nColor: {self.color}\nMarca: {self.marca}")

class Pinza:
    def __init__(self,color,tamano,material,marca):
        self.color = color
        self.tamano = tamano
        self.material = material
        self.marca = marca

    def imprimir(self):
        print(f"Color: {self.color}\nTamano: {self.tamano}\nMaterial: {self.material}\nMarca: {self.marca}")

class Pegatina:
    def __init__(self,color,forma,tamano,tipo):
        self.color = color 
        self.forma = forma
        self.tamano = tamano
        self.tipo = tipo
    
    def imprimir(self):
        print(f"Color: {self.color}\nForma: {self.forma}\nTamano: {self.tamano}\nTipo: {self.tipo}")

class Esmalte:
    def __init__(self,color,tamano,forma,marca):
        self.color = color
        self.tamano = tamano
        self.forma = forma
        self.marca = marca

    def imprimir(self):
        print(f"\nColor: {self.color}\nTamano: {self.tamano}\nForma: {self.forma}\nMarca: {self.marca}")

class Marco_foto:
    def __init__(self,color,forma,tamano,grosor):
        self.color = color
        self.forma = forma
        self.tamano = tamano
        self.grosor = grosor

    def imprimir(self):
        print(f"Color: {self.color}\nForma: {self.forma}\nTamano: {self.tamano}\nGrosor: {self.grosor}")

class Cuenta:
    def __init__(self,color,tamano,forma,material):
        self.color = color
        self.forma = forma
        self.tamano = tamano
        self.material = material

    def imprimir(self):
        print(f"Color: {self.color}\nForma: {self.forma}\nTamano: {self.tamano}\nMaterial: {self.material}")
    
class Boligrafo:
    def __init__(self,color,precio,marca,grosor):
        self.color = color
        self.precio = precio
        self.marca = marca
        self.grosor = grosor

    def imprimir(self):
        print(f"Color: {self.color}\nPrecio: {self.precio}\nMarca: {self.marca}\nGrosor: {self.grosor}")