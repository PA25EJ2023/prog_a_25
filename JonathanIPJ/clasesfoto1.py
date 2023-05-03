class Pluma:
    def __init__(self, color, precio, tamano, marca):
        self.color = color
        self.precio = precio 
        self.tamano = tamano
        self.marca = marca 
    
    def imprimir(self):
        print({self.color}, {self.precio}, {self.tamano}, {self.marca})


class Tijera:
    def __init__(self, color, tamano, precio, marca):
        self.color = color
        self.tamano = tamano
        self.precio = precio
        self.marca = marca 

    def imprimir(self):
        print({self.color}, {self.tamano}, {self.precio}, {self.marca}) 


class Libreta:
    def __init__(self, color, num_hojas, marca, precio):
        self.color = color
        self.num_hojas = num_hojas
        self.marca = marca
        self.precio = precio

    def imprimir(self):
        print({self.color}, {self.num_hojas}, {self.marca}, {self.precio})


class Espejo:
    def __init__(self,forma,color,precio):
        self.forma = forma 
        self.color = color 
        self.precio = precio 

    def imprimir(self):
        print({self.forma}, {self.color}, {self.precio})

class Pegamento:
    def __init__(self,tipo,marca,precio,tamano):
        self.tipo = tipo
        self.marca = marca 
        self.precio = precio 
        self.tamano = tamano 

    def imprimir(self):
        print({self.tipo},{self.marca},{self.precio},self.tamano)


class Marco:
    def __init__(self, tamano, color, forma, imagen):
        self.tamano = tamano 
        self.color = color 
        self.forma = forma 
        self.imagen = imagen

    def imprimir(self):
        print({self.tamano}, {self.color}, {self.forma}, {self.imagen}) 



