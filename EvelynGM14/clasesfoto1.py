class Boligrafo:
    def __init__(self,color,tamaño,precio,marca):
        self.color = color
        self.tamaño = tamaño
        self.precio = precio
        self.marca = marca
    
    def info(self):
        print(f"Color: {self.color}\nTamaño: {self.tamaño}\nPrecio: {self.precio}\nMarca: {self.marca}")



class Marcador:
    def __init__(self,color,tamaño,precio,marca):
        self.color = color
        self.tamaño = tamaño
        self.precio = precio
        self.marca = marca

    def info(self):
        print(f"Color: {self.color}\nTamaño: {self.tamaño}\nPrecio: {self.precio}\nMarca: {self.marca}")


class Cinta_Adhesiva:
    def __init__(self,color,ancho,longitud,marca):
        self.color = color
        self.ancho = ancho
        self.longitud =longitud
        self.marca = marca

    def info(self):
        print(f"Color: {self.color}\nAncho: {self.ancho}\nLongitud: {self.longitud}\nMarca: {self.marca}")


class Retrato:
    def __init__(self,tamaño):
        self.tamaño = tamaño

    def info(self):
        print(f"Tamaño: {self.tamaño}")


class Esmalte:
    def __init__(self,color,marca,forma):
        self.color = color
        self.marca = marca
        self.precio = forma

    def info(self):
        print(f"Color: {self.color}\nMarca: {self.marca}\nForma: {self.forma}")


class Sticker:
    def __init__(self,cantidad):
        self.cantidad = cantidad

    def info(self):
        print(f"Cantidad: {self.cantidad}")

    







    



