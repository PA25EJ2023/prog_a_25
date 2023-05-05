#clases foto 1 (tocador,peinador)
class Esmalte:
    def __init__(self,color,forma_envase,precio,tamaño,cantidad):
        self.color=color   #PONERLO EN MODO PRIVADO
        self.forma_envase=forma_envase
        self.precio=precio
        self.tamaño=tamaño
        self.cantidad=cantidad
    
    def info(self):
        print(" *** ESMALTE ***")
        print(f"Color del esmalte: {self.color}")
        print(f"Forma del envase: {self.forma_envase}")
        print(f"Precio: {self.precio}")    
        print(f"Tamaño: {self.tamaño}")
        print (f"Cantidad en ml: {self.cantidad}")


class Espejo_corazon:
    def __init__(self,altura,ancho,color,precio):
        self.altura=altura
        self.ancho=ancho
        self.color=color
        self.precio=precio
        
    def info(self):
        print("*** ESPEJO ***")
        print(f"MEDIDAS\nAltura del espejo en cm: {self.altura} y el ancho del espejo en cm: {self.ancho}")
        print(f"Color marco: {self.color}")
        print(f"$ {self.precio}")    

class Retrato:
    def __init__(self,altura,ancho,color,precio,decoracion):
        self.altura=altura
        self.ancho=ancho
        self.color=color
        self.precio=precio
        self.decoracion=decoracion
        #self.altura_foto=altura_foto
        #self.ancho_foto=ancho_foto

    def info(self):
        print("*** RETRATO ***")
        print(f"MEDIDAS\nAltura del retrato en cm: {self.altura} y el ancho del retrato en cm: {self.ancho}")
        print(f"Color base/principal del retrato: {self.color}")
        print(f"$ {self.precio}")  
        print(f"Decoracion: {self.decoracion}")    

class Marcador:
    def __init__(self,color,precio,tipo,marca): #tipo es permanente o de agua
        self.color=color
        self.precio=precio
        self.tipo=tipo
        self.marca=marca

    def info(self):
        print("*** MARCADOR ***")
        print(f"Color del marcadoror: {self.color}")
        print(f"$ {self.precio}")    
        print(f"Tipo (agua/permanente): {self.tipo}")
        print(f"Marca: {self.marca}")

class Boligrafo:
    def __init__(self,color,precio,tipo,marca):
        self.color=color
        self.precio=precio
        self.tipo=tipo
        self.marca=marca

    def info(self):
        print("*** BOLIGRAFO ***")
        print(f"Color de la tinta: {self.color}")
        print(f"$ {self.precio}")    
        print(f"Tipo (tinta normal/agua/gel): {self.tipo}")
        print(f"Marca: {self.marca}")

class Libreta:
    def __init__(self,color,tamaño,precio,tipo,marca): 
        self.color=color
        self.tamaño=tamaño
        self.precio=precio
        self.tipo=tipo
        self.marca=marca

    def info(self):
        print("*** LIBRETA ***")
        print(f"Color de la libreta: {self.color}")
        print(f"Tamaño (ch,md,gr): {self.tamaño}")
        print(f"$ {self.precio}")    
        print(f"Tipo (raya/cuadro): {self.tipo}")
        print(f"Marca: {self.marca}")

class Pegamento:
    def __init__(self,tamaño,precio,marca,aplicador): #aplicador es barra o liquido
        self.tamaño=tamaño
        self.precio=precio
        self.marca=marca
        self.aplicador=aplicador

    def info(self):
        print("*** PEGAMENTO ***")
        print(f"Tamaño del pegamento: {self.tamaño}")    
        print(f"$ {self.precio}")
        print(f"Marca: {self.marca}")
        print(f"Aplicador (barra/líquido): {self.aplicador}")

class Cinta:
    def __init__(self,tipo,precio,tamaño,color):
        self.tipo=tipo
        self.precio=precio
        self.tamaño=tamaño
        self.color=color

    def info(self):
        print("*** CINTA ***")
        print(f"Tipo de cinta (adhesiva/de papel/doble cara/aislante): {self.tipo}")
        print(f"$ {self.precio}")    
        print(f"Tamaño (ch/md/gr): {self.tamaño}")
        print(f"Color: {self.color}")

class Telefono:
    def __init__(self,precio,color,num_tel,marca):
        self.precio=precio
        self.color=color
        self.num_tel=num_tel
        self.marca=marca
        
    def info(self):
        print("*** TELEFONO ***")    
        print(f"Color del telefono: {self.color}")
        print(f"$ {self.precio}")
        print(f"Numero de telefono: {self.num_tel}")
        print(f"Marca: {self.marca}")
        
    
class Sticker:
    def __init__(self,tamaño,figura,color,precio):
        self.tamaño=tamaño
        self.figura=figura
        self.color=color
        self.precio=precio

    def info(self):
        print("*** STICKER ***")
        print(f"Tamaño del sticker (ch/md/gr): {self.tamaño}")    
        print(f"Figura (estrella/corazon/luna): {self.figura}")
        print(f"Color: {self.color}")
        print(f"$ {self.precio}")
        

class Broche:
    def __init__(self,color,precio,marca,material):
        self.color=color
        self.precio=precio
        self.marca=marca
        self.material=material

    def info(self):
        print("*** BROCHE ***")
        print(f"Color del broche: {self.color}")
        print(f"$ {self.precio}")
        print(f"Marca: {self.marca}")
        print(f"Material: {self.material}")

class Labial:
    def __init__(self,marca,precio,tamaño,color,tipo):
        self.marca=marca
        self.precio=precio
        self.tamaño=tamaño
        self.color=color
        self.tipo=tipo

    def info(self):
        print("*** LABIAL ***")
        print(f"Marca del labial: {self.marca}")
        print(f"$ {self.precio}")
        print(f"Tamaño (md/gr): {self.tamaño}")
        print(f"Color: {self.color}")
        print(f"Tipo (líquido/mate/gloss): {self.tipo}")
    
class Tijeras:
    def __init__ (self,color,precio,marca,tipo):
        self.color=color
        self.precio=precio
        self.marca=marca
        self.tipo=tipo

    def info(self):
        print("*** TIJERAS ***")
        print(f"Color de las tijeras: {self.color}")
        print(f"$ {self.precio}")
        print(f"Marca: {self.marca}")
        print(f"Tipo (diestro/zurdo): {self.tipo}")
    
class Piedrita:
    def __init__(self,color,tamaño,precio,material):
        self.color=color
        self.tamaño=tamaño
        self.precio=precio
        self.material=material

    def info(self):
        print("*** PIEDRITA ***")
        print(f"Color de la piedrita: {self.color}")
        print(f"Tamaño: {self.tamaño}")
        print(f"$ {self.precio}")
        print(f"Material: {self.material}")

class Hoja_plantilla:
    def __init__(self,imagen,tamaño,precio,material):
        self.imagen=imagen
        self.tamaño=tamaño
        self.precio=precio
        self.material=material

    def info(self):
        print("*** PLANTILLA ***")
        print(f"Imagen de la hoja es: {self.imagen}")
        print(f"Tamaño (ch/md/gr): {self.tamaño}")
        print(f"$ {self.precio}")
        print(f"Material (plastico,papel,cartón): {self.material}")


    