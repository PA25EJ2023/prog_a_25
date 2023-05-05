class Revista:
    def __init__(self,nombre,tipo,fecha_salida,precio):
        self.nombre = nombre
        self.tipo = tipo
        self.fecha_salida = fecha_salida
        self.precio = precio
    
    def info(self):
        print(f'nombre: {self.nombre}\n tipo: {self.tipo}\n fecha_salida: {self.fecha_salida}\n precio: {self.precio}')

class Portafolio:
    def __init__(self,marca,color,tamaño,precio):
        self.marca = marca
        self.color = color
        self.tamaño = tamaño
        self.precio = precio
    
    def info(self):
        print(f'marca: {self.marca}\n color: {self.color}\n tamaño {self.tamaño}\n precio: {self.precio}')

class Zapatos:
    def __init__(self,marca,color,precio):
        self.marca = marca
        self.color = color
        self.precio = precio
    
    def info(self):
        print(f'marca: {self.marca}\n color: {self.color}\n precio: {self.precio}')

class Laptop:
    def __init__(self,marca,color,precio):
        self.marca = marca
        self.color = color 
        self.precio = precio

    def info(self):
        print(f'marca: {self.marca}\n color: {self.color}\n precio: {self.precio}')

class Pila_camara:
    def __init__(self,marca,color,tipo,precio):
        self.marca = marca
        self.color = color
        self.tipo = tipo
        self.precio = precio
    
    def info(self):
        print(f'marca: {self.marca}\n color: {self.color}\n tipo de pila: {self.tipo}\n precio: {self.precio}')

class Tripie:
    def __init__(self,marca,color,tamaño,precio):
        self.marca = marca
        self.color = color
        self.tamaño = tamaño
        self.precio = precio
    
    def info(self):
        print(f'marca: {self.marca}\n color: {self.color}\n tamaño: {self.tamaño}\n precio: {self.precio}')