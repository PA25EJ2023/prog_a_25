class Espejo:
    def __init__(self,numero,color,marca,forma,tamaño):
        self.numero = numero
        self.color = color
        self.marca = marca
        self.forma = forma
        self.tamaño = tamaño

    def info (self):
        print("***Espejos***")
        print(f"Numero espejo: {self.numero} \nColor: {self.color} \nMarca: {self.marca} \nForma: {self.forma} \nTamaño: {self.tamaño}")


class Telefono:
    def __init__(self,numero,color,marca,tamaño):
        self.numero = numero
        self.color = color
        self.marca = marca
        self.tamaño = tamaño

    def info (self):
        print("***Telefonos***")
        print(f"Numero telefono: {self.numero} \nColor: {self.color} \nMarca: {self.marca} \nTamaño:{self.tamaño}")

class Esmalte:
    def __init__(self,numero,color,marca,tamaño):
        self.numero = numero
        self.color = color
        self.marca = marca
        self.tamaño = tamaño

    def info (self):
            print("***Esmaltes***")
            print(f"Numero esmalte: {self.numero} \nColor: {self.color} \nMarca: {self.marca} \nTamaño: {self.tamaño}")

class Boligrafo:
    def __init__(self,numero,color,marca,tamaño):
        self.numero = numero
        self.color = color
        self.marca = marca
        self.tamaño = tamaño

    def info (self):
            print("***Boligrafos***")
            print(f"Numero boligrafo: {self.numero} \nColor: {self.color} \nMarca: {self.marca} \nTamaño: {self.tamaño}")


