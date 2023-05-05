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
    def __init__(self,marca,tipo,color,precio):
        self.color = color
        self.marca = marca
        self.tipo = tipo
        self.precio = precio 
    def info(self):
        print(f"El color es: {self.color}")
        print(f"La marca es: {self.marca}")
        print(f"Es de tipo: {self.tipo}")
        print(f"El precio es de: ${self.precio}")

class Revista:
    def __init__(self,precio,titulo,editorial,idioma):
        self.precio = precio
        self.titulo = titulo
        self.editorial = editorial
        self.idioma = idioma
    def info(self):
        print(f"El precio es de: {self.precio}")
        print(f"Titulo: {self.titulo}")
        print(f"La editorial es: {self.editorial}")
        print(f"Esta en idioma: {self.idioma}")

class Reloj:
    def __init__(self,marca,tipo,precio,color):
        self.marca = marca
        self.tipo = tipo
        self.precio = precio 
        self.color = color
    def info(self):
        print(f"La marca es: {self.marca}")
        print(f"Es de tipo: {self.tipo}")
        print(f"El precio es de: ${self.precio}")
        print(f"El color es: {self.color}")

class Zapato:
    def __init__(self,material,color,estilo,precio):
        self.material = material
        self.color = color
        self.estilo = estilo
        self.precio = precio
    def info(self):
        print(f"El material es: {self.material}")
        print(f"El color es: {self.color}")
        print(f"El estilo es: {self.estilo}")
        print(f"El precio es de: ${self.precio}")

class Lapiz:
    def __init__ (self,precio,marca,color,tipo):
        self.precio = precio
        self.marca = marca
        self.color = color
        self.tipo = tipo
    def info(self):
        print(f"El precio es de: ${self.precio}")
        print(f"La marca es: {self.marca}")
        print(f"El color es: {self.color}")
        print(f"Es de tipo: {self.tipo}")
        
class Lente:
    def __init__(self,color,marca,tipo,precio):
        self.color = color
        self.marca = marca
        self.tipo = tipo
        self.precio = precio
    def info(self):
        print(f"El color es: {self.color}")
        print(f"La marca es: {self.marca}")
        print(f"Es de tipo: {self.tipo}")
        print(f"El precio es de: ${self.precio}")
        
class Bateria:
    def __init__(self,marca,tipo,precio,):
        self.marca = marca
        self.tipo = tipo
        self.precio = precio
    def info(self):
        print(f"La marca es: {self.marca}")
        print(f"Es de tipo: {self.tipo}")
        print(f"El precio es de: ${self.precio}")

class Estuche:
    def __init__(self,color,material,precio,tipo):
        self.color = color
        self.material = material
        self.precio = precio
        self.tipo = tipo
    def info(self):
        print(f"El color es: {self.color}")
        print(f"El material es: {self.material}")
        print(f"El precio es de: ${self.precio}")
        print(f"Es de tipo: {self.tipo}")