#clases foto 1 (tocador,peinador)
class Esmalte:
    def __init__(self,color,forma_envase,precio,tamaño,cantidad):
        self.color=color   #PONERLO EN MODO PRIVADO
        self.forma_envase=forma_envase
        self.precio=precio
        self.tamaño=tamaño
        self.cantidad=cantidad
    
    def info(self):
        print(f"El color del esmalte es: {self.color}")
        print(f"La forma del envase es: {self.forma_envase}")
        print(f"El precio es de: {self.precio}")    
        print(f"El tamaño es de: {self.tamaño}")
        print (f"Su cantidad en mg es de: {self.cantidad}")


class Espejo_corazon:
    def __init__(self,altura,ancho,color,precio):
        self.altura=altura
        self.ancho=ancho
        self.color=color
        self.precio=precio
        
    def info(self):
        print(f"- MEDIDAS- La altura del espejo es de: {self.altura} y el ancho del espejo es de: {self.ancho}")
        print(f"El color del marco del espejo es de: {self.color}")
        print(f"El precio es de: {self.precio}")    

class Retrato:
    def __init__(self,altura,ancho,color,precio,altura_foto,ancho_foto):
        self.altura=altura
        self.ancho=ancho
        self.color=color
        self.precio=precio
        self.altura_foto=altura_foto
        self.ancho_foto=ancho_foto

    def info(self):
        print(f"- MEDIDAS- La altura del retrato es de: {self.altura} y el ancho del retrato es de: {self.ancho}")
        print(f"El color base del retrato es de: {self.color}")
        print(f"El precio es de: {self.precio}")  
        print(f"- MEDIDAS- La altura de la foto es de: {self.altura_foto} y el ancho de la foto es de: {self.ancho_foto}")
    
class Marcador:
    def __init__(self,color,precio,tipo,marca): #tipo es permanente o de agua
        self.color=color
        self.precio=precio
        self.tipo=tipo
        self.marca=marca

    def info(self):
        print(f"El color del marcador es de: {self.color}")
        print(f"El precio es de: {self.precio}")    
        print(f"El tipo es de: {self.tipo}")
        print (f"La marca es de {self.marca}")

class Boligrafo:
    def __init__(self,color,precio,tipo,marca):
        self.color=color
        self.precio=precio
        self.tipo=tipo
        self.marca=marca

    def info(self):
        print(f"El color del boligrafo o pluma es de: {self.color}")
        print(f"El precio es de: {self.precio}")    
        print(f"El tipo es de: {self.tipo}")
        print (f"La marca es de {self.marca}")

class Libreta:
    def __init__(self,color,tamaño,precio,tipo,marca): #tipo es raya, cuadro y el tamaño es grande,chica o mediana
        self.color=color
        self.tamaño=tamaño
        self.precio=precio
        self.tipo=tipo
        self.marca=marca

    def info(self):
        print(f"El color de la libreta es de: {self.color}")
        print(f"El tamaño es: {self.tamaño}")
        print(f"El precio es de: {self.precio}")    
        print(f"El tipo es de: {self.tipo}")
        print (f"La marca es de {self.marca}")

class Pegamento:
    pass

class Cinta:
    pass

class Telefono:
    pass

class Sticker:
    pass

class Broche:
    pass

class Labial:
    pass

class Tijeras:
    pass











        #pluma1,plima2,puma 3 y meter datos a cada una

        #camisa y especificar color