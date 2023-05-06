class Camisetas():
    def __init__(self,color,talla,tipo,):
        self.color = color
        self.talla = talla
        self.tipo = tipo
    def inf(self):
        print(f"Color>> {self.color}\nTalla>> {self.talla}\nTipo>> {self.tipo}")

class Maletin():
    def __init__(self,color,tamaño,material,):
        self.color = color
        self.tamaño = tamaño
        self.material = material 
    def inf(self):
        print(f"Color>> {self.color}\nTamaño>> {self.tamaño}\nMaterial>> {self.material}")

class Cargadores():
    def __init__(self,color,medida,tipo,marca):
        self.color = color 
        self.medida = medida 
        self.tipo = tipo 
        self.marca = marca 
    def inf(self):
        print(f"Color>> {self.color}\nMedida>> {self.medida}\nTipo>> {self.tipo}\nMarca>> {self.marca}")
        
        