class Camisa:
    def __init__(self, color, material,precio,talla):
        self.color = color
        self.material = material
        self.precio = precio
        self.talla = talla

    def imprimir(self):
        print(f"Camisa- Color:{self.color}, Material:{self.material}, Precio:{self.precio}, Talla:{self.talla}")

class Laptop:
    def __init__(self, marca, color, precio, modelo):
        self.marca = marca
        self.color = color 
        self.precio = precio
        self.modelo = modelo

    def imprimir(self):
        print(f"Laptop- Marca:{self.marca}, Color:{self.color}, Precio:{self.precio}, Modelo:{self.modelo}")

class Reloj:
    def __init__(self,color, tipo, precio,marca):
        self.color = color 
        self.tipo = tipo 
        self.precio = precio
        self.marca = marca

    def imprimir(self):
        print(f"Reloj- Color{self.color}, Tipo:{self.tipo}, Precio:{self.precio}, Marca:{self.marca}")


class Lente:
    def __init__(self, color, marca, tipo, precio):
        self.color = color 
        self.marca = marca
        self.tipo = tipo 
        self.precio = precio

    def imprimir(self):
        print(f"Lente- Color:{self.color}, Marca:{self.marca}, Tipo:{self.tipo}, Precio:{self.precio}")


class Revista:
    def __init__(self, titulo, paginas, portada, precio):
        self.titulo = titulo  
        self.paginas = paginas
        self.portada = portada
        self.precio = precio

    def imprimir(self):
        print(f"Revista- Titulo:{self.titulo}, Paginas:{self.paginas}, Portada:{self.portada}, Precio:{self.precio}")


class Maletin:
    def __init__(self, color, marca, precio, medidas):
        self.color = color  
        self.marca = marca
        self.precio = precio
        self.medidas = medidas
    def imprimir(self):
        print(f"Maletin- Color:{self.color}, Marca:{self.marca}, Precio:{self.precio}, Medidas:{self.medidas}")


class Cargador:
    def __init__(self, color, marca, precio, longitud):
        self.color = color 
        self.marca = marca 
        self.precio = precio
        self.longitud = longitud

    def imprimir(self):
        print(f"Cargador: Color:{self.color}, Marca:{self.marca}, Precio:{self.precio}, Longitud:{self.longitud }")


class Pluma:
    def __init__(self,color, marca, tipo, precio): 
        self.color = color 
        self.marca = marca
        self.tipo = tipo
        self.precio = precio

    def imprimir(self):
        print(f"Pluma- Color:{self.color}, Marca:{self.marca}, Tipo:{self.tipo}, Precio:{self.precio}")


class Lapiz:
    def __init__(self,color, marca, tipo, precio): 
        self.color = color 
        self.marca = marca
        self.tipo = tipo
        self.precio = precio

    def imprimir(self):
        print(f"Lapiz- Color:{self.color}, Marca:{self.marca}, Tipo:{self.tipo}, Precio:{self.precio}")


class Zapato:
    def __init__(self,color, talla, marca, precio): 
        self.color = color 
        self.talla = talla 
        self.marca = marca 
        self.precio = precio

    def imprimir(self):
        print(f"Zapato- Color:{self.color}, Talla:{self.talla}, Marca:{self.marca}, Precio:{self.precio}")


class Telefono:
    def __init__(self, color, tipo, marca, precio):
        self.color = color 
        self.tipo = tipo
        self.marca = marca 
        self.precio = precio

    def imprimir(self):
        print(f"Telefono- Color:{self.color}, Tipo:{self.tipo}, Marca:{self.marca}, Precio:{self.precio}")


class Tripode:
    def __init__(self, color, tamano, marca, precio):
        self.color = color 
        self.tamano = tamano 
        self.marca = marca 
        self.precio = precio

    def imprimir(self):
        print(f"Tripode- Color:{self.color}, Tamaño:{self.tamano}, Marca:{self.marca}, Precio:{self.precio}")
