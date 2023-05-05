class Celular:
    def __init__(self,color,marca,precio,almacenamiento):
        self.color = color
        self.marca = marca
        self.precio = precio
        self.alamcenamiento = almacenamiento
    def info(self):
        print(f"La marca del celular es: {self.marca}")
        print(f"El precio es de: ${self.precio}")
        print(f"Su color es: {self.color}")
        print(f"La capacidad de almacenamiento es de: {self.almacenamiento}")

class Camisa:
    def __init__(self,color,marca,precio,material):
        self.color = color
        self.marca = marca
        self.precio = precio
        self.material = material
    def info(self):
        print(f"El color de la playera es: {self.color}")
        print(f"La marca es: {self.marca}")
        print(f"El precio es de: ${self.precio}")
        print(f"El material es: {self.material}")

class Maletin:
    def __init__(self,color,marca,material,precio):
        self.color = color
        self.marca = marca
        self.material = material
        self.precio = precio
    def info(self):
        print(f"El color del maletin es: {self.color}")
        print(f"La marca es: {self.marca}")
        print(f"El material es: {self.material}")
        print(f"El precio es de: ${self.precio}")
        
class Cargador:
    def __init__(self,marca,color,tipo,precio):
        self.color = color
        self.marca = marca
        self.tipo = tipo
        self.precio = precio 
    def info(self):
        print(f"El color del maletin es: {self.color}")
        print(f"La marca es: {self.marca}")
        print(f"Es de tipo: {self.tipo}")
        print(f"El precio es de: ${self.precio}")

class Laptop:
    pass

class Revista:
    pass

class Reloj:
    pass

class Zapato:
    pass

class Lapiz:
    pass

class Lente:
    pass

class Bateria:
    pass

class Estuche:
    pass