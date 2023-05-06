class Boligrafo:
    def __init__(self,numero,marca,color,precio):
        self.numero = numero 
        self.marca = marca
        self.color = color
        self.precio = precio 

    def info(self):
        print(f'Boligrafo{self.numero}\n Marca {self.marca}\n Color {self.color}\n Precio {self.precio}')

class Espejo:
    def __init__(self,forma,color,tama):
        self.forma = forma
        self.color = color
        self.tama = tama
    
    def info(self):
        print(f'tamaño: {self.tamaño}\n forma: {self.forma}\n color: {self.color}')

class Telefono:
    def __init__(self,color,tamaño,tipo):
        self.color = color
        self.tamaño = tamaño
        self.tipo = tipo
    
    def info(self):
        print(f'color: {self.color}\n tamaño: {self.tamaño}\n tipo: {self.tipo}')

class Marco:
    def __init__(self,color,diseño,tama):
        self.color = color
        self.diseño = diseño
        self.tama = tama

    def info(self):
        print(f'forma: {self.forma}\n diseño: {self.diseño}\n tamaño: {self.tamaño}\n color: {self.color}')

class Esmalte:
    def __init__(self,color,forma,tamaño):
        self.color = color
        self.forma = forma
        self.tamaño = tamaño

    def info(self):
       print(f'Color: {self.color}\n Forma: {self.forma}\n Tamaño: {self.tamaño}')

class Cinta:
    def __init__(self,color,precio,tamaño):
        self.color = color
        self.precio = precio
        self.tamaño = tamaño

    def info(self):
       print(f'Color: {self.color}\n Forma: {self.precio}\n Tamaño: {self.tamaño}')

class Marcadores:
    def __init__(self,color,precio,marca):
        self.color = color
        self.precio = precio
        self.marca = marca

    def info(self):
       print(f'Color: {self.color}\n Forma: {self.precio}\n Tamaño: {self.marca}')

class Gloss:
    def __init__(self,color,precio,tamaño,marca):
        self.color = color
        self.precio = precio
        self.tamaño = tamaño
        self.marca = marca

    def info(self):
       print(f'Color: {self.color}\n Precio: {self.precio}\n Tamaño: {self.tamaño}\n Marca {self.marca}')
       
class Libreta:
    def __init__(self,color,precio,tamaño,marca,diseño):
        self.color = color
        self.precio = precio
        self.tamaño = tamaño
        self.marca = marca
        self.diseño = diseño

    def info(self):
       print(f'Color: {self.color}\n Precio: {self.precio}\n Tamaño: {self.tamaño}\n Marca {self.marca}\n Diseño {self.diseño}')

class Pegamento:
    def __init__(self,color,precio,marca,diseño):
        self.color = color
        self.precio = precio
        self.marca = marca
        self.diseño = diseño

    def info(self):
       print(f'Color: {self.color}\n Precio: {self.precio}\n Marca {self.marca}\n Diseño {self.diseño}')

class Pinzas:
    def __init__(self,color,precio,forma):
        self.color = color
        self.precio = precio
        self.forma = forma

    def info(self):
       print(f'Color: {self.color}\n Precio: {self.precio}\n Forma {self.forma}')

class Cuencas:
    def __init__(self,color,no_cuen,forma):
        self.color = color
        self.no_cuen = no_cuen
        self.forma = forma

    def info(self):
       print(f'Color: {self.color}\n Numero de Cuencas {self.no_cuen}\n Forma {self.forma}')

class Pegatinas:
    def __init__(self,color,precio,forma,no_pegat):
        self.color = color
        self.precio = precio
        self.forma = forma
        self.no_pegat = no_pegat

    def info(self):
       print(f'Color: {self.color}\n Precio: {self.precio}\n Forma {self.forma}\n Numero de pegatina {self.no_pegat}')

    