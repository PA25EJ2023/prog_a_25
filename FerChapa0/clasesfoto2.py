class Camisa:
    def __init__(self, color, marca, precio, talla):
        self.color=color
        self.marca=marca
        self.precio=precio
        self.talla=talla

    def imprimir_info(self):
        print("El camisa es color ", self.color)
        print(f'El precio es {self.precio}')
        print(f'La marca es {self.marca}')
        print(f'La talla de la camisa es {self.talla}')

class Chaqueta:
    def __init__(self, color, marca, precio, talla):
        self.color=color
        self.marca=marca
        self.precio=precio
        self.talla=talla

    def imprimir_info(self):
        print("La chaqueta es color ", self.color)
        print(f'El precio es {self.precio}')
        print(f'La marca es {self.marca}')
        print(f'La talla de la chaqueta es {self.talla}')

class Laptop:
    def __init__(self, color, marca, precio, tamaño):
        self.color=color
        self.marca=marca
        self.precio=precio
        self.tamaño=tamaño

    def imprimir_info(self):
        print("La laptop es color ", self.color)
        print(f'El precio es {self.precio}')
        print(f'La marca es {self.marca}')
        print(f'El tamaño es {self.marca} pulgadas')

class Lente:
    def __init__(self, color, marca, precio, diametro):
        self.color=color
        self.marca=marca
        self.precio=precio
        self.diametro=diametro

    def imprimir_info(self):
        print(f'El Lente es color {self.color}')
        print(f'El precio es {self.precio}')
        print(f'La marca es {self.marca}')
        print(f'El diametro del lente es {self.diametro}')

class Tapa_Lente:
    def __init__(self, color, marca, diametro, precio):
        self.color=color
        self.marca=marca
        self.diametro=diametro
        self.precio=precio

    def imprimir_info(self):
        print(f'La tapa es color {self.color}')
        print(f'El precio es {self.precio} pesos')
        print(f'La marca es {self.marca}')
        print(f'El diametro de la tapa es {self.diametro}')

class Pila:
    def __init__(self, color, marca, tipo, precio):
        self.color=color
        self.marca=marca
        self.tipo=tipo
        self.precio=precio

    def imprimir_info(self):
        print(f'La pila es color {self.color}')
        print(f'El tipo de la pila es {self.tipo}')
        print(f'La marca de la pila es {self.marca}')
        print(f'El precio de la pila es {self.precio} pesos')

class Revista:
    def __init__(self, marca, precio,largo,tipo):
        self.marca=marca
        self.precio=precio
        self.largo=largo
        self.tipo=tipo
    def imprimir_info(self):
        print(f'El precio de la revista es {self.precio} pesos')
        print(f'La marca de la revista es {self.marca}')
        print(f'El largo de la revista es {self.largo} cm')
        print(f'La tipo de la revista es {self.tipo}')

class Cargador:
    def __init__(self, color, tipo, marca, precio):
        self.color=color
        self.tipo=tipo
        self.marca=marca
        self.precio=precio
    
    def imprimir_info(self):
        print(f'El color del cargador es {self.color}')
        print(f'El tipo del cargador es {self.tipo}')
        print(f'La marca del cargador es {self.marca}')
        print(f'El precio del cargador es {self.precio}')

class Zapato:
    def __init__(self,color, talla,precio,tipo ) :
        self.color=color
        self.talla=talla
        self.precio=precio
        self.tipo=tipo
    
    def imprimir_info(self):
        print(f'El color de los zapatos es {self.color}')
        print(f'La talla de los zapatos es {self.talla}')
        print(f'El precio de los zapatos es {self.precio}')
        print(f'El tipo de zapato es {self.tipo}')

class Maletin:
    def __init__(self,color,material,tamaño,precio):
        self.color=color
        self.material=material
        self.tamaño=tamaño
        self.precio=precio

    def imprimir_info(self):
        print(f'El color del Maletin es {self.color}')
        print(f'El material del Maletin es {self.material}')
        print(f'El tamaño del Maletin es {self.tamaño}')
        print(f'El precio del Maletin es {self.precio} pesos')

class Celular:
    def __init__(self,color,marca,tamaño,precio):
        self.color=color
        self.marca=marca
        self.tamaño=tamaño
        self.precio=precio

    def imprimir_info(self):
        print(f'El color del Celular es {self.color}')
        print(f'La marca del Celular es {self.marca}')
        print(f'El tamaño del Celular es {self.tamaño} pulgadas')
        print(f'El precio del Celular es {self.precio}')

class Reloj:
    def __init__(self,color,material,marca,precio):
        self.color=color
        self.material=material
        self.marca=marca
        self.precio=precio

    def imprimir_info(self):
        print(f'El color del reloj es {self.color}')
        print(f'El material del reloj es {self.material}')
        print(f'La marca del reloj es {self.marca}')
        print(f'El precio del reloj es {self.precio}')

class Tripie:
    def __init__(self, color, tamaño, tipo, precio):
        self.color=color
        self.tamaño=tamaño
        self.tipo=tipo
        self.precio=precio
    
    def imprimir_info(self):
        print(f'El color del tripie es {self.color}')
        print(f'El tamaño del tripie es {self.tamaño}')
        print(f'La tipo del tripie es {self.tipo}')
        print(f'El precio del tripie es {self.precio}')

class Estuche:
    def __init__(self, color, marca, precio,tamaño):
        self.color=color
        self.marca=marca
        self.precio=precio
        self.tamaño=tamaño
    
    def imprimir_info(self):
        print(f'El color del estuche es {self.color}')
        print(f'El tamaño del estuche es {self.tamaño} cm')
        print(f'La marca del estuche es {self.marca}')
        print(f'El precio del estuche es {self.precio} pesos')

class Lapiz:
    def __init__(self, forma, color, marca, clasificacion):#2b b hb 2h
        self.forma=forma
        self.color=color
        self.marca=marca
        self.clasificacion=clasificacion

    def imprimir_info(self):
        print(f'El color del lapiz es {self.color}')
        print(f'La forma del lapiz es {self.forma}')
        print(f'La marca del lapiz es {self.marca}')
        print(f'La casificacion del lapiz es {self.clasificacion}') 

class Plumon:
    def __init__(self,color, grosor,marca,tamaño):
        self.color=color
        self.grosor=grosor
        self.marca=marca
        self.tamaño=tamaño

    def imprimir_info(self):
        print(f'El color del plumon es {self.color}')
        print(f'El grosor del plumon es {self.grosor}')
        print(f'La marca del plumon es {self.marca}')
        print(f'El tamaño del plumon es {self.tamaño}')

class Cable:
    def __init__(self, color, tipo, forma,largo):
        self.color=color
        self.tipo=tipo
        self.forma=forma
        self.largo=largo

    def imprimir_info(self):
        print(f'El color del cable es {self.color}')
        print(f'El tipo del cable es {self.tipo}')
        print(f'La forma del cable es {self.forma}')
        print(f'El largo del cable es {self.largo}')
