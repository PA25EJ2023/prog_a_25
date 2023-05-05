class Boligrafo:
    def __init__(self,marca,color,precio):
        self.marca = marca 
        self.color = color
        self.precio = precio
    
    def info(self):
        print(f'marca: {self.marca}\n color: {self.color}\n precio: {self.precio}')

class Espejo:
    def __init__(self,tamaño,forma,color):
        self.tamaño = tamaño
        self.forma = forma
        self.color = color
    
    def info(self):
        print(f'tamaño: {self.tamaño}\n forma: {self.forma}\n color: {self.color}')


class Recuadro:
    def __init__(self,forma,diseño,tamaño,color):
        self.forma = forma
        self.diseño = diseño
        self.tamaño = tamaño
        self.color = color
    
    def info(self):
        print(f'forma: {self.forma}\n diseño: {self.diseño}\n tamaño: {self.tamaño}\n color: {self.color}')

class Esmalte:
    def __init__(self,color,forma,tamaño):
        self.color = color
        self.forma = forma
        self.tamaño = tamaño
    
    def info(self):
        print(f'color: {self.color}\n forma: {self.forma}\n tamaño: {self.tamaño}')

class Cinta:
    def __init__(self,color,tamaño,precio):
        self.color = color
        self.tamaño = tamaño
        self.precio = precio
    
    def info(self):
        print(f'color: {self.color}\n tamaño: {self.tamaño}\n precio: {self.precio}')
        
class Marcadores:
    def __init__(self,color,marca,precio):
        self.color = color
        self.marca = marca
        self.precio = precio
    
    def info(self):
        print(f'color: {self.color}\n marca: {self.marca}\n precio: {self.precio}')
