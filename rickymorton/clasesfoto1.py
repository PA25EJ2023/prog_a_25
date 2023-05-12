class Boligrafo:
    def __init__(self,marca,color,precio,tamaño):
        self.marca = marca 
        self.color = color
        self.precio = precio
        self.tamaño = tamaño
    
    def info(self):
        print(f'marca: {self.marca}\n color: {self.color}\n precio: {self.precio}\n tamaño: {self.tamaño}')

class Espejo:
    def __init__(self,marca,tamaño,forma,color):
        self.marca = marca
        self.tamaño = tamaño
        self.forma = forma
        self.color = color
    
    def info(self):
        print(f'marca: {self.marca}\n tamaño: {self.tamaño}\n forma: {self.forma}\n color: {self.color}')


class Recuadro:
    def __init__(self,forma,diseño,tamaño,color):
        self.forma = forma
        self.diseño = diseño
        self.tamaño = tamaño
        self.color = color
    
    def info(self):
        print(f'forma: {self.forma}\n diseño: {self.diseño}\n tamaño: {self.tamaño}\n color: {self.color}')

class Esmalte:
    def __init__(self,color,forma,tamaño,precio):
        self.color = color
        self.forma = forma
        self.tamaño = tamaño
        self.precio = precio
    
    def info(self):
        print(f'color: {self.color}\n forma: {self.forma}\n tamaño: {self.tamaño}\n precio: {self.precio}')

class Cinta:
    def __init__(self,marca,color,tamaño,precio):
        self.marca = marca
        self.color = color
        self.tamaño = tamaño
        self.precio = precio
    
    def info(self):
        print(f'marca: {self.marca}\n color: {self.color}\n tamaño: {self.tamaño}\n precio: {self.precio}')
        
class Marcadores:
    def __init__(self,color,marca,tamaño,precio):
        self.color = color
        self.marca = marca
        self.tamaño = tamaño
        self.precio = precio
    
    def info(self):
        print(f'color: {self.color}\n marca: {self.marca}\n tamaño: {self.tamaño}\n precio: {self.precio}')

class Lip_gloss:
    def __init__(self,color,tamaño,precio,marca):
        self.color = color
        self.tamaño = tamaño
        self.precio = precio
        self.marca = marca
    
    def info(self):
        print(f'color: {self.color}\n tamaño: {self.tamaño}\n precio: {self.precio}\n marca: {self.marca}')

class Reloj:
    def __init__(self,marca,modelo,color,precio):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.precio = precio
    
    def info(self):
        print(f'marca: {self.marca}\n modelo: {self.modelo}\n color: {self.color}\n precio: {self.precio}')

class Libreta:
    def __init__(self,marca,color,diseño,precio):
        self.marca = marca
        self.color = color
        self.diseño = diseño
        self.precio = precio
    
    def info(self):
        print(f'marca: {self.marca}\n color: {self.color}\n diseño {self.diseño}\n precio: {self.precio}')

class Pegamento:
    def __init__(self,marca,color,tamaño,precio):
        self.marca = marca
        self.color = color
        self.tamaño = tamaño
        self.precio = precio
    
    def info(self):
        print(f'marca: {self.marca}\n color: {self.color}\n tamaño: {self.tamaño}\n precio: {self.precio}')

class Sticker:
    def __init__(self,marca,forma,color,no_stick):
        self.marca = marca
        self.forma = forma
        self.color = color
        self.no_stick = no_stick
    
    def info(self):
        print(f'marca: {self.marca}\n forma: {self.forma}\n color: {self.color}\n Numero de stickers: {self.no_stick}')

class Cuencas:
    def __init__(self,forma,color,material,no_cuen):
        self.forma = forma
        self.color = color
        self.material = material
        self.no_cuen = no_cuen
    
    def info(self):
        print(f'forma: {self.forma}\n color: {self.color}\n material: {self.material}\n Numero de cuencas: {self.no_cuen}')

class Pinzas:
    def __init__(self,forma,color,material,precio):
        self.forma = forma
        self.color = color
        self.material = material
        self.precio = precio
    
    def info(self):
        print(f'forma: {self.forma}\n color: {self.color}\n material: {self.material}\n precio: {self.precio}')