class Bateria_Portatil:
    def __init__(self,numero,color,marca,tamaño):
        self.numero = numero
        self.color = color
        self.marca = marca
        self.tamaño = tamaño

    def info (self):
        print(f"Numero bateria: {self.numero} \nColor: {self.color} \nMarca: {self.marca} \nTamaño:{self.tamaño}")

class Celular:
    def __init__(self,numero,color,modelo,marca):
        self.numero = numero
        self.color = color
        self.modelo = modelo
        self.marca = marca

    def info (self):
        print(f"Numero celular: {self.numero} \nColor: {self.color} \nMarca: {self.marca} \nModelo:{self.modelo}")

class Camisas:
    def __init__(self,numero,color,marca,tela):
        self.numero = numero
        self.color = color
        self.marca = marca
        self.tela = tela

    def info (self):
        print(f"Numero camisa: {self.numero} \nColor: {self.color} \nMarca: {self.marca} \nTipo de tela:{self.tela}")

class Cable:
    def __init__(self,numero,color,dispo):
        self.numero = numero
        self.color = color
        self.dispo = dispo

    def info(self):
        print(f"Numero cable: {self.numero} \nColor: {self.color} \nDispositivo al que pertenece: {self.dispo}")

