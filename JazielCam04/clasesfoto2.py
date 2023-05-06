class Revista:
    def __init__(self,nombre,tipo,precio):
        self.nombre = nombre
        self.tipo = tipo
        self.precio = precio
    
    def info(self):
        print(f'nombre: {self.nombre}\n tipo: {self.tipo}\n \n precio: {self.precio}')

class Portafolio:
    def __init__(self,color,tamaño,precio):
        self.color = color
        self.tamaño = tamaño
        self.precio = precio
    
    def info(self):
        print(f'color: {self.color}\n tamaño {self.tamaño}\n precio: {self.precio}')

class Zapatos:
    def __init__(self,marca,color,tipo):
        self.marca = marca
        self.color = color
        self.tipo = tipo
    
    def info(self):
        print(f'marca: {self.marca}\n color: {self.color}\n tipo: {self.tipo}')

class Laptop:
    def __init__(self,marca,modelo,color,precio):
        self.marca = marca
        self.modelo = modelo
        self.color = color 
        self.precio = precio


    def info(self):
        print(f'marca: {self.marca}\n modelo: {self.modelo}\n color: {self.color}\n precio: {self.precio}')

class Flash:
    def __init__(self,marca,color,tipo,precio):
        self.marca = marca
        self.color = color
        self.tipo = tipo
        self.precio = precio
    
    def info(self):
        print(f'marca: {self.marca}\n color: {self.color}\n tipo de pila: {self.tipo}\n precio: {self.precio}')

class Tripie:
    def __init__(self,marca,color,tamaño,precio):
        self.marca = marca
        self.color = color
        self.tamaño = tamaño
        self.precio = precio
    
    def info(self):
        print(f'marca: {self.marca}\n color: {self.color}\n tamaño: {self.tamaño}\n precio: {self.precio}')

class Celular:
    def __init__(self,marca,modelo,color,precio):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.precio = precio
    
    def info(self):
        print(f'marca: {self.marca}\n modelo: {self.modelo}\n color: {self.color}\n precio: {self.precio}')

class Pila:
    def __init__(self,marca,tipo,color,precio):
        self.marca = marca
        self.tipo = tipo
        self.color = color
        self.precio = precio
    
    def info(self):
        print(f'marca: {self.marca}\n tipo: {self.tipo}\n color: {self.color}\n precio: {self.precio}')

class Reloj:
    def __init__(self,marca,color,precio):
        self.marca = marca
        self.color = color
        self.precio = precio
    
    def info(self):
        print(f'marca: {self.marca}\n color: {self.color}\n precio: {self.precio}')

class Camisa:
    def __init__(self,marca,color,talla,tipo):
        self.marca = marca
        self.color = color
        self.talla = talla
        self.tipo = tipo
    
    def info(self):
        print(f'marca: {self.marca}\n color: {self.color}\n talla: {self.talla}\n tipo: {self.tipo}')

class Lente_camara:
    def __init__(self,marca,color,tamaño,precio):
        self.marca = marca
        self.color = color
        self.tamaño = tamaño 
        self.precio = precio
    
    def info(self):
        print(f'marca: {self.marca}\n color: {self.color}\n tamaño: {self.tamaño}\n precio: {self.precio}')

class Chaqueta:
    def __init__(self,marca,color,talla,tipo):
        self.marca = marca
        self.color = color
        self.talla = talla
        self.tipo = tipo
    
    def info(self):
        print(f'marca: {self.marca}\n color: {self.color}\n talla: {self.talla}\n tipo: {self.tipo}')

class Protector:
    def __init__(self,marca,color,tamaño,precio):
        self.marca = marca
        self.color = color
        self.tamaño = tamaño
        self.precio = precio
    
    def info(self):
        print(f'marca: {self.marca}\n color: {self.color}\n tamaño: {self.tamaño}\n precio: {self.precio}')

class Estuche_camara:
    def __init__(self,marca,color,tamaño,precio):
        self.marca = marca
        self.color = color
        self.tamaño = tamaño
        self.precio = precio
    
    def info(self):
        print(f'marca: {self.marca}\n color: {self.color}\n tamaño: {self.tamaño}\n precio: {self.precio}')

class Marcador:
    def __init__(self,marca,color,tipo_pluma,tamaño):
        self.marca = marca
        self.color = color
        self.tipo_pluma = tipo_pluma
        self.tamaño = tamaño
    
    def info(self):
        print(f'marca: {self.marca}\n color: {self.color}\n tipo pluma: {self.tipo_pluma}\n tamaño: {self.tamaño}')

class Lapices:
    def __init__(self,marca,color,precio,tamaño):
        self.marca = marca
        self.color = color
        self.precio = precio
        self.tamaño = tamaño
    
    def info(self):
        print(f'marca: {self.marca}\n color: {self.color}\n precio: {self.precio}\n tamaño: {self.tamaño}')

class Cargador_lap:
    def __init__(self,marca,tipo,color,precio):
        self.marca = marca
        self.tipo = tipo
        self.color = color
        self.precio = precio
    
    def info(self):
        print(f'marca: {self.marca}\n tipo: {self.tipo}\n color: {self.color}\n precio: {self.precio}')