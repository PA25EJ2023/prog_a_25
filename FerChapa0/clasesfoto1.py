class Cuenta:
    def __init__(self,color,diametro, peso, forma):
        self.color=color
        self.diametro=diametro #diametro peso forma
        self.peso=peso
        self.forma=forma
    
    def imprimir_info(self):
        print("La cuenta es color ", self.color)
        print("El diametro de cuenta es ", self.diametro, " cm")
        print("El peso de cuenta es ", self.peso, " gramos")
        print("La forma de cuenta es ", self.forma)

class Boligrafo:
    def __init__(self, color, marca, precio,forma):
        self.color=color
        self.marca=marca
        self.precio=precio
        self.forma=forma

    def imprimir_info(self):
        print("El boligrafo es color ", self.color)
        print(f'La marca es {self.marca}')
        print(f'El precio es {self.precio} pesos')
        print(f'La forma del boligrafo es {self.forma}')

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
    def __init__(self, color, tipo, tamaño):
        self.color=color
        self.tipo=tipo
        self.tamaño=tamaño

    def imprimir_info(self):
        print(f'El color de la tijera es: {self.color}')
        print(f'El tipo de la tijera es: {self.tipo}')
        print(f'El tamaño de la tijera es: {self.tamaño} cm')

class Libreta:
    def __init__(self, color, largo, ancho, tipo):
        self.color=color
        self.largo=largo
        self.ancho=ancho
        self.tipo=tipo
    
    def mostrar_info(self):
        print(f'El color de la libreta es: {self.color}')
        print(f'El tipo de la libreta es: {self.tipo}')
        print(f'El alto de la libreta es de: {self.largo} cm')
        print(f'El ancho de la libreta es de: {self.ancho} cm')

class Cinta:
    def __init__(self, color, ancho, longitud) :
        self.color=color
        self.ancho=ancho
        self.longitud=longitud
    
    def mostrar_info(self):
        print(f' El color de la cinta es: {self.color}')
        print(f' El ancho de la cinta es: {self.ancho} cm')
        print(f' La longitud de la cinta es: {self.longitud}')

class Espejo:
    def __init__(self, color, forma, precio,tamaño) :
        self.color=color
        self.forma=forma
        self.precio=precio
        self.tamaño=tamaño
    
    def mostrar_info(self):
        print(f' El color del Espejo es: {self.color}')
        print(f' La forma del Espejo es: {self.forma}')
        print(f' El precio del espejo es: {self.precio} pesos')
        print(f' El tamaño del espejo es: {self.tamaño} cm')

class Pintura_uñas:
    def __init__(self,color,forma,peso,medida) :
        self.color=color
        self.forma=forma
        self.peso=peso
        self.medida=medida

    def mostrar_info(self):
        print(f' El color del pinta uñas es: {self.color}')
        print(f' La forma del pinta uñas es: {self.forma}')
        print(f' La peso del pinta uñas es: {self.peso} gr')
        print(f' La medida del pinta uñas es: {self.medida} cm')

class Pegamento:
    def __init__(self,color,forma, precio, tamaño) :
        self.color=color
        self.forma=forma
        self.precio=precio
        self.tamaño=tamaño

    def mostrar_info(self):
        print(f' El color del pegamento es: {self.color}')
        print(f' La forma del pegamento es: {self.forma}')
        print(f' El precio del pegamento es: {self.precio}')
        print(f' El tamaño del pegamento es: {self.tamaño}')

class Retrato:
    def __init__(self, color, largo, ancho, detalle):
        self.color=color
        self.largo=largo
        self.ancho=ancho
        self.detalle=detalle
    
    def mostrar_info(self):
        print(f'El color del retrato es: {self.color}')
        print(f'El detalle del retrato es: {self.detalle}')
        print(f'El alto del retrato es {self.largo} cm')
        print(f'El ancho del retrato es de: {self.ancho} cm')

class Telefono:
    def __init__(self,color,tipo, precio, peso) :
        self.color=color
        self.tipo=tipo
        self.precio=precio
        self.peso=peso

    def mostrar_info(self):
        print(f' El color del telefono es: {self.color}')
        print(f' El tipo del telefono es: {self.tipo}')
        print(f' El precio del telefono es: {self.precio} pesos')
        print(f' El peso del telefono es: {self.peso}')

class Hoja_sticker:
    def __init__(self,color,forma, cantidad):
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

class Cuca:
    def __init__(self,color,tamaño,tipo, detalle) :
        self.color=color
        self.tamaño=tamaño
        self.tipo=tipo
        self.detalle=detalle

    def mostrar_info(self):
        print(f' El color de la Cuca es: {self.color}')
        print(f' El tamaño de la Cuca es: {self.tamaño}')
        print(f' El tipo de la Cuca es: {self.tipo}')
        print(f' El detalle que tiene la Cuca es: {self.detalle}')

class Pinta_Labios:
    def __init__(self,color,forma,peso,detalle) :
        self.color=color
        self.forma=forma
        self.peso=peso
        self.detalle=detalle

    def mostrar_info(self):
        print(f' El color del labial es: {self.color}')
        print(f' La forma del labial es: {self.forma}')
        print(f' La peso del labial es: {self.peso} gr')
        print(f' El detalle del labial es: {self.detalle}')