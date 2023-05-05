class Boligrafo():
    def __init__(self,color,marca,tamaño,precio):
        self.color = color
        self.marca = marca
        self.tamaño = tamaño
        self.precio = precio
    def inf(self):
        print(f"Color de tinta>> {self.color}\nMarca de pluma>> {self.marca}\nTamaño de pluma>> {self.tamaño}\n¿Cuanto costo?>> {self.precio}")

class Cuaderno():
    def __init__(self,color,marca,tamaño,tipo):
        self.color = color
        self.marca = marca
        self.tamaño = tamaño 
        self.tipo = tipo
    
    def inf(self):
        print(f"Color>> {self.color}\nMarca>> {self.marca}\nTamaño>> {self.tamaño}\nTipo de libreta>> {self.tipo}")

class Plumones():
    def __init__(self,color,marca,tamaño,precio):
        self.color = color 
        self.marca = marca  
        self.tamaño = tamaño
        self.precio = precio

    def inf(self):
        print(f"Color>> {self.color}\nMarca>> {self.marca}\nTamaño>> {self.tamaño}\nPrecio>> {self.precio}")

class Tijeras():
    def __init__(self,color,marca,tamaño,precio):
        self.color = color 
        self.marca = marca  
        self.tamaño = tamaño
        self.precio = precio
    def inf(self):
        print(f"Color>> {self.color}\nMarca>> {self.marca}\nTamaño>> {self.tamaño}\nPrecio>> {self.precio}")


class Esmalte():
    def __init__(self,color,marca,tamaño,forma):
        self.color = color 
        self.marca = marca  
        self.tamaño = tamaño
        self.forma = forma
    def inf(self):
        print(f"Color>> {self.color}\nMarca>> {self.marca}\nTamaño>> {self.tamaño}\nForma>> {self.forma}")