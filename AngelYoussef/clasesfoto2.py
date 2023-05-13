class Camisa:
    def __init__(self,marca,color,tipo,precio):
        self.marca = marca
        self.color = color
        self.tipo = tipo
        self.precio = precio

    def imprimir(self):
        print(f"Marca: {self.marca}\nColor: {self.color}\nTipo: {self.tipo}\nPrecio: {self.precio}")

class Cargador_portatil:
    def __init__(self,marca,color,precio,tipo_entrada):
        self.marca = marca 
        self.color = color
        self.precio = precio
        self.tipo_entrada = tipo_entrada

    def imprimir(self):
        print(f"Marca: {self.marca}\nColor: {self.color}\nPrecio: {self.precio}\nTipo de entrada: {self.tipo_entrada}")

class Computadora:
    def __init__(self,marca,precio,almacenamiento,color):
        self.marca = marca
        self.precio = precio
        self.almacenamiento = almacenamiento
        self.color = color

    def imprimir(self):
        print(f"Marca: {self.marca}\nPrecio: {self.precio}\nAlmacenamiento: {self.almacenamiento}\nColor: {self.color}")

class Celular:
    def __init__(self,marca,precio,almacenamiento,color):
        self.marca = marca
        self.precio = precio
        self.almacenamiento = almacenamiento
        self.color = color

    def imprimir(self):
        print(f"Marca: {self.marca}\nPrecio: {self.precio}\nAlmacenamiento: {self.almacenamiento}\nColor: {self.color}")

class Bolsa:
    def __init__(self,color,material,precio,marca):
        self.color = color
        self.material = material
        self.precio = precio
        self.marca = marca

    def imprimir(self):
        print(f"Color: {self.color}\nMaterial: {self.material}\nPrecio: {self.precio}\nMarca: {self.marca}")

class Tapa_Objetivo:
    def __init__(self,marca,color,precio,material):
        self.marca = marca
        self.color = color
        self.precio = precio
        self.material = material

    def imprimir(self):
        print(f"Marca: {self.marca}\nColor: {self.color}\nPrecio: {self.precio}\nMaterial: {self.material}")

class Lente_Camara:
    def __init__(self,marca,color,precio,material):
        self.marca = marca
        self.color = color
        self.precio = precio
        self.material = material

    def imprimir(self):
        print(f"Marca: {self.marca}\nColor: {self.color}\nPrecio: {self.precio}\nMaterial: {self.material}")

class Reloj:
    def __init__(self,marca,color,precio,tamano):
        self.marca = marca
        self.color = color
        self.precio = precio
        self.tamano = tamano

    def imprimir(self):
        print(f"Marca: {self.marca}\nColor: {self.color}\nPrecio: {self.precio}\nTamano: {self.tamano}")

class Cargador_Escritorio:
    def __init__(self,marca,color,longitud,precio):
        self.marca = marca
        self.color = color
        self.longitud = longitud
        self.precio = precio

    def imprimir(self):
        print(f"Marca: {self.marca}\nColor: {self.color}\nLongitud: {self.longitud}\nPrecio: {self.precio}")

class Disparador_Flash:
    def __init__(self,marca,color,precio,alcanze):
        self.marca = marca
        self.color = color
        self.precio = precio
        self.alcanze = alcanze

    def imprimir(self):
        print(f"Marca: {self.marca}\nColor: {self.color}\nPrecio: {self.precio}\nAlcanze: {self.alcanze}")

class Tripode:
    def __init__(self,marca,color,precio,material):
        self.marca = marca
        self.color = color
        self.precio = precio
        self.material = material

    def imprimir(self):
        print(f"Marca: {self.marca}\nColor: {self.color}\nPrecio: {self.precio}\nMaterial: {self.material}")

class Zapatos:
    def __init__(self,marca,color,precio,material,talla):
        self.marca = marca
        self.color = color
        self.precio = precio
        self.material = material
        self.talla = talla

    def imprimir(self):
        print(f"Marca: {self.marca}\nColor: {self.color}\nPrecio: {self.precio}\nMaterial: {self.material}\nTalla: {self.talla}")

class Revista:
    def __init__(self,titulo,precio,paginas,editorial):
        self.titulo = titulo
        self.precio = precio
        self.paginas = paginas
        self.editorial = editorial

    def imprimir(self):
        print(f"Titulo: {self.titulo}\nPrecio: {self.precio}\nPaginas: {self.paginas}\nEditorial: {self.editorial}")

class Estuche_camara:
    def __init__(self,marca,precio,color,tamano):
        self.marca = marca
        self.precio = precio
        self.color = color
        self.tamano = tamano

    def imprimir(self):
        print(f"Marca: {self.marca}\nPrecio: {self.precio}\nColor: {self.color}\nTamano: {self.tamano}")

class Boligrafo:
    def __init__(self,marca,precio,color,material):
        self.marca = marca
        self.precio = precio
        self.color = color
        self.material = material

    def imprimir(self):
        print(f"Marca: {self.marca}\nPrecio: {self.precio}\nColor: {self.color}\nMaterial: {self.material}")

class Lapiz:
    def __init__(self,marca,precio,color,material):
        self.marca = marca
        self.precio = precio
        self.color = color
        self.material = material

    def imprimir(self):
        print(f"Marca: {self.marca}\nPrecio: {self.precio}\nColor: {self.color}\nMaterial: {self.material}")