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
        pass

class Marco:
    def __init__(self,color,diseño,tama):
        self.color = color
        self.diseño = diseño
        self.tama = tama

    def info(self):
        pass

class Telefono:
    def __init__(self,color,diseño,tama):
        self.color = color
        self.diseño = diseño
        self.tama = tama

    def info(self):
        pass

