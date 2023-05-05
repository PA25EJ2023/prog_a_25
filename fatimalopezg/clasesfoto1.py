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
        print(f"El color de la tinta es: {self.color}")
        print(f"El precio es de: {self.precio}")    
        print(f"El tipo es (tinta normal/agua/gel) de: {self.tipo}")
        print(f"La marca es de {self.marca}")

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
    def __init__(self,tamaño,precio,marca,aplicador): #aplicador es en barra o liquido
        self.tamaño=tamaño
        self.precio=precio
        self.marca=marca
        self.aplicador=aplicador

    def info(self):
        print(f"El tamaño del pegamento es: {self.tamaño}")    
        print(f"El precio es de: {self.precio}")
        print(f"La marca es de: {self.marca}")
        print(f"El aplicador (barra/líquido) es de: {self.aplicador}")

class Cinta:
    def __init__(self,tipo,precio,tamaño,color):
        self.tipo=tipo
        self.precio=precio
        self.tamaño=tamaño
        self.color=color

    def info(self):
        print(f"El tipo de cinta (adhesiva/de papel/doble cara/aislante) es de: {self.tipo}")
        print(f"El precio es de: {self.precio}")    
        print(f"El tamaño (ch/md/gr)es de: {self.tamaño}")
        print(f"El color es: {self.color}")

class Telefono:
    def __init__(self,precio,color,num_tel,marca):
        self.precio=precio
        self.color=color
        self.num_tel=num_tel
        self.marca=marca
        
    def info(self):
        print(f"El precio es de: {self.precio}")    
        print(f"El color es: {self.color}")
        print(f"El numero de telefono es: {self.num_tel}")
        print(f"La marca es: {self.marca}")
        
    
class Sticker:
    def __init__(self,tamaño,figura,color,precio):
        self.tamaño=tamaño
        self.figura=figura
        self.color=color
        self.precio=precio

    def info(self):
        print(f"El tamaño (ch/md/gr)es: {self.tamaño}")    
        print(f"La figra (estrella/corazon/luna) es: {self.figura}")
        print(f"El color es: {self.color}")
        print(f"El precio es de: {self.precio}")
        

class Broche:
    def __init__(self,color,precio,marca,material):
        self.color=color
        self.precio=precio
        self.marca=marca
        self.material=material

    def info(self):
        print(f"El color es: {self.color}")
        print(f"El precio es de: {self.precio}")
        print(f"La marca es: {self.marca}")
        print(f"El material es de: {self.material}")

class Labial:
    def __init__(self,marca,precio,tamaño,color,tipo):
        self.marca=marca
        self.precio=precio
        self.tamaño=tamaño
        self.color=color
        self.tipo=tipo

    def info(self):
        print(f"La marca del labial es: {self.marca}")
        print(f"El precio es de: {self.precio}")
        print(f"El tamaño (md/gr) es: {self.tamaño}")
        print(f"El color es: {self.color}")
        print(f"El tipo (líquido/mate/gloss) es: {self.tipo}")
    
class Tijeras:
    def __init__ (self,color,precio,marca,tipo):
        self.color=color
        self.precio=precio
        self.marca=marca
        self.tipo=tipo

    def info(self):
        print(f"El color es: {self.color}")
        print(f"El precio es de: {self.precio}")
        print(f"La marca es: {self.marca}")
        print(f"El tipo (diestro/zurdo) es: {self.tipo}")
    
class Piedritas:
    def __init__(self,color,tamaño,precio,material):
        self.color=color
        self.tamaño=tamaño
        self.precio=precio
        self.material=material

    def info(self):
        print(f"El color es: {self.color}")
        print(f"El tamaño es: {self.tamaño}")
        print(f"El precio es de: {self.precio}")
        print(f"El material es: {self.material}")

        #pluma1,pluma2,pluma3 y meter datos a cada una
        #camisa y especificar color