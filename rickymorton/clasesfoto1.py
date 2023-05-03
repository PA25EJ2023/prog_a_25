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




