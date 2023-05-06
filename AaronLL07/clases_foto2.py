class Cargador:
    
    def __init__(self, color, capacidad, tamano):
        self.color = color
        self.capacidad = capacidad
        self.tamano = tamano
    
    def imprimir(self):
        print(f"Color: {self.color}\nCapacidad de carga: {self.capacidad}\n Tamaño: {self.tamano}")

class Celular:

    def __init__(self, marca, color, tamano, precio):
        self.marca = marca
        self.color = color
        self.tamano = tamano
        self.precio = precio

    def imprimir(self):
        print(f"Marca: {self.marca}\nColor: {self.color}\nTamaño: {self.tamano}\nPrecio: {self.precio}")

class Maletin:

    def __init__(self, material, marca, color, precio, tamano):
        self.material = material
        self.marca = marca
        self.color = color
        self.precio = precio
        self.tamano = tamano

    def imprimir(self):
        print(f"Material: {self.material}\nMarca: {self.marca}\nColor: {self.color}\nPrecio: {self.precio}\nTamaño: {self.tamano}")

class Tripie:

    def __init__(self, color, tamano, marca, precio):
        self.color = color
        self.tamano = tamano
        self.marca = marca
        self.precio = precio
    
    def imprimir(self):
        print(f"Color: {self.color}\nTamaño: {self.tamano}\nMarca: {self.marca}\nPrecio: {self.precio}")

class Camisa:

    def __init__(self, marca, color, talla, precio):
        self.marca = marca
        self.color = color
        self.talla = talla
        self.precio = precio

    def imprimir(self):
        print(f"Marca: {self.marca}\nColor: {self.color}\nTalla: {self.talla}\nPrecio: {self.precio}")

class Lente:

    def __init__(self, marca, color, tamano):
        self.marca = marca
        self.color = color
        self.tamano = tamano

    def imprimir(self):
        print(f"Marca: {self.marca}\nColor: {self.color}\nTamaño: {self.tamano}")

class Tapa_Lente:

    def __init__(self, marca, color, tamano):
        self.marca = marca
        self.color = color
        self.tamano = tamano

    def imprimir(self):
        print(f"Marca: {self.marca}\nColor: {self.color}\nTamaño: {self.tamano}")

class Pila:

    def __init__(self, marca, capacidad, tamano):
        self.marca = marca
        self.capacidad = capacidad
        self.tamano = tamano

    def imprimir(self):
        print(f"Marca: {self.marca}\Capacidad: {self.capacidad}\nTamaño: {self.tamano}")

class Computadora:

    def __init__(self, marca, color, precio, gama):
        self.marca = marca 
        self.color = color
        self.precio = precio
        self.gama = gama

    def imprimir(self):
        print(f"Marca: {self.marca}\Color: {self.color}\nPrecio: {self.precio}\nGama: {self.gama}")

class Chamarra:

    def __init__(self, marca, color, talla, precio):
        self.marca = marca
        self.color = color
        self.talla = talla
        self.precio = precio

    def imprimir(self):
        print(f"Marca: {self.marca}\nColor: {self.color}\nTalla: {self.talla}\nPrecio: {self.precio}")

class Reloj:

    def __init__(self, marca, color, precio, tamano):
        self.marca = marca
        self.color = color
        self.precio = precio
        self.tamano = tamano

    def imprimir(self):
        print(f"Marca: {self.marca}\nColor: {self.color}\nPrecio: {self.precio}\nTamañpo: {self.tamano}")

class Zapato:

    def __init__(self, marca, color, talla, precio):
        self.marca = marca
        self.color = color
        self.talla = talla
        self.precio = precio

    def imprimir(self):
        print(f"Marca: {self.marca}\nColor: {self.color}\nTalla: {self.talla}\nPrecio: {self.precio}")

class Revista:

    def __init__(self, nombre, descripcion, tamano, precio):
        self.nombre = nombre
        self.descripcion = descripcion
        self.tamano = tamano
        self.precio = precio
    
    def imprimir(self):
        print(f"Nombre: {self.nombre}\nDescripción: {self.descripcion}\nTamaño: {self.tamano}\nPrecio: {self.precio}")

class Cargador:

    def __init__(self, marca, color, tamano):
        self.marca = marca
        self.color = color
        self.tamano = tamano

    def imprimir(self):
        print(f"Marca: {self.marca}\nColor: {self.color}\nTamaño: {self.tamano}")

class Estuche:

    def __init__(self, marca, color, tamano, desc):
        self.marca = marca
        self.color = color
        self.tamano = tamano
        self.desc = desc
    
    def imprimir(self):
        print(f"Marca: {self.marca}\nColor: {self.color}\nTamaño: {self.tamano}\n Descripción: {self.desc}")

