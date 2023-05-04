class Cuenta:
    def __init__(self,color,cantidad):
        self.color=color
        self.cantidad=cantidad #diametro peso forma
    
    def imprimir_info(self):
        print("La cuenta es color ", self.color)
        print("la cantidad de cuentas ", self.color, " son", self.cantidad)

class Boligrafo:
    def __init__(self, color, marca, precio,forma):
        self.color=color
        self.marca=marca
        self.precio=precio
        self.forma=forma

    def imprimir_info(self):
        print("El boligrafo es color ", self.color)
        print(f'El precio es {self.precio}')
        print(f'La marca es {self.marca}')
        print(f'La froma del boligrafo es {self.forma}')


class Plumon:
    def __init__(self,color,marca,precio) :
        self.color=color
        self.marca=marca
        self.precio=precio

    def imprimir_info(self):
        print("El Plumon es color ", self.color)
        print(f'El precio del plumon es {self.precio}')
        print(f'La marca del plumon es {self.marca}')

class Tijera:
    def __init__(self, color, tipo):
        self.color=color
        self.tipo=tipo

    def imprimir_info(self):
        print(f'El color de la tijera es: {self.color}')
        print(f'El tipo de la tijera es: {self.tipo}')

class Libreta:
    def __init__(self, color, largo, ancho, tipo):
        self.color=color
        self.largo=largo
        self.ancho=ancho
        self.tipo=tipo
    
    def mostrar_info(self):
        print(f'El color de la libreta es: {self.color}')
        print(f'El tipo de la libreta es: {self.tipo}')
        print(f'El alto de la libreta es de: {self.alto} cm')
        print(f'El ancho de la libreta es de: {self.ancho} cm')

class Cinta:
    def __init__(self, color, ancho, longitud) :
        self.color=color
        self.ancho=ancho
        self.longitud=longitud
    
    def mostrar_info(self):
        print(f' El color de la cinta es: {self.color}')
        print(f' El ancho de la cinta es: {self.ancho}')
        print(f' La longitud de la cinta es: {self.longitud}')


class Espejo:
    def __init__(self, color, forma, precio,tamaño) :
        self.color=color
        self.forma=forma
        self.precio=precio
        self.tamaño=tamaño
    
    def mostrar_info(self):
        print(f' El color del Espejo es: {self.color}')
        print(f' La forma del Espejo es: {self.froma}')
        print(f' El precio del espejo es: {self.precio}')
        print(f' El tamaño del espejo es: {self.tamaño} cm')


class Pintura_uñas:
    def __init__(self,color,forma) :
        self.color=color
        self.forma=forma

    def mostrar_info(self):
        print(f' El color del pinta uñas es: {self.color}')
        print(f' La forma del pinta uñas es: {self.forma}')
class Pegamento:
    def __init__(self,color,forma) :
        self.color=color
        self.forma=forma

    def mostrar_info(self):
        print(f' El color del pegamento es: {self.color}')
        print(f' La forma del pegamento es: {self.forma}')

class Retrato:
    def __init__(self, color, largo, ancho, detalle):
        self.color=color
        self.largo=largo
        self.ancho=ancho
        self.detalle=detalle
    
    def mostrar_info(self):
        print(f'El color del retrato es: {self.color}')
        print(f'El detalle del retrato es: {self.detalle}')
        print(f'El alto del retrato es{self.alto} cm')
        print(f'El ancho del retrato es de: {self.ancho} cm')

class Telefono:
    def __init__(self,color,tipo) :
        self.color=color
        self.tipo=tipo

    def mostrar_info(self):
        print(f' El color del telefono es: {self.color}')
        print(f' El tipo del telefono es: {self.tipo}')

class Sticker:
    def __init__(self,color,forma, cantidad) :
        self.color=color
        self.forma=forma
        self.cantidad=cantidad

    def mostrar_info(self):
        print(f' El color de los Stickers es: {self.color}')
        print(f' El forma del los Stickers es: {self.forma}')
        print(f' La cantidad del Stickers es: {self.cantidad}')

class Poster:
    def __init__(self,color,forma,detalle) :
        self.color=color
        self.forma=forma
        self.detalle=detalle

    def mostrar_info(self):
        print(f' El color del retrato es: {self.color}')
        print(f' El forma del retrato es: {self.forma}')
        print(f' Los detalles del retrato son: {self.detalle}')

class Sticker:
    def __init__(self,color,tipo) :
        self.color=color
        self.tipo=tipo

    def mostrar_info(self):
        print(f' El color de la cuca es: {self.color}')
        print(f' El tipo de la cuca es: {self.tipo}')