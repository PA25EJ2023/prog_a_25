class Camisa:
    def __init__(self, color, marca, precio):
        self.color=color
        self.marca=marca
        self.precio=precio

    def imprimir_info(self):
        print("El camisa es color ", self.color)
        print(f'El precio es {self.precio}')
        print(f'La marca es {self.marca}')

class Laptop:
    def __init__(self, color, marca, precio, tamaño):
        self.color=color
        self.marca=marca
        self.precio=precio
        self.tamaño=tamaño

    def imprimir_info(self):
        print("La laptop es color ", self.color)
        print(f'El precio es {self.precio}')
        print(f'La marca es {self.marca}')
        print(f'El tamaño es {self.marca} pulgadas')

class Lente:
    def __init__(self, color, marca, precio):
        self.color=color
        self.marca=marca
        self.precio=precio

    def imprimir_info(self):
        print(f'El Lente es color {self.color}')
        print(f'El precio es {self.precio}')
        print(f'La marca es {self.marca}')

class Pila:
    def __init__(self, color, marca, tipo):
        self.color=color
        self.marca=marca
        self.tipo=tipo

    def imprimir_info(self):
        print(f'El camisa es color {self.color}')
        print(f'El tipo de la camisa es {self.tipo}')
        print(f'La marca de la camisa es {self.marca}')

class Revista:
    def __init__(self, marca, precio):
        self.marca=marca
        self.precio=precio

    def imprimir_info(self):
        print(f'El precio de la revista es {self.precio}')
        print(f'La marca de la revista es {self.marca}')

class Cargador:
    def __init__(self, color, tipo, marca):
        self.color=color
        self.tipo