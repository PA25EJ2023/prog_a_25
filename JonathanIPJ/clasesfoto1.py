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