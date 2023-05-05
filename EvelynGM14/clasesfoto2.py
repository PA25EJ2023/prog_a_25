class Maletin:
    def __init__(self,color,tamaño,material,marca):
        self.color = color
        self.tamaño = tamaño
        self.material = material
        self.marca = marca
    
    def info(self):
        print(f"1 MALETIN\nColor: {self.color}\nTamaño: {self.tamaño}\nPrecio: {self.material}\nMarca: {self.marca}")


class Laptop:
    def __init__(self,color,tamaño,precio,marca):
        self.color = color
        self.tamaño = tamaño
        self.precio = precio
        self.marca = marca
    
    def info(self):
        print(f"1 LAPTOP\nColor: {self.color}\nTamaño: {self.tamaño}\nPrecio: {self.precio}\nMarca: {self.marca}")


class Reloj:
    def __init__(self,color,tamaño,material,marca):
        self.color = color
        self.tamaño = tamaño
        self.material = material
        self.marca = marca
    
    def info(self):
        print(f"1 RELOJ\nColor: {self.color}\nTamaño: {self.tamaño}\nPrecio: {self.material}\nMarca: {self.marca}")