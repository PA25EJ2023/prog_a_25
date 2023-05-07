class Esmaltes:  
    def __init__(self, numero, color, ml, recipiente, tapa ):
       self.numero = numero
       self.color = color
       self.cap = ml
       self.recipiente = recipiente
       self.tapa = tapa
    def atributos_esmaltes(self):
        print(f"Esmalte numero {self.numero}:")
        print(f"El esmalte es de color {self.color}, es de {self.cap}ml, su recipiente es de {self.recipiente} y su tapa de {self.tapa}.")

class Gloss:
    def __init__(self, numero, color, ml, recipiente, tapa ):
       self.numero = numero
       self.color = color
       self.cap = ml
       self.recipiente = recipiente
       self.tapa = tapa
    def atributos_gloss(self):
        print(f"Gloss numero {self.numero}:")
        print(f"El gloss es de color {self.color}, contiene {self.cap}ml, tiene un recipiente de {self.recipiente} y tapa de {self.tapa}.")

class Marco:
    def __init__(self, numero, base, altura, material ):
       self.numero = numero
       self.base = base
       self.altura = altura
       self.material = material
    def atributos_marco(self):
        print(f"Marco numero {self.numero}:")
        print(f"El marco tiene como medidas una base de {self.base}cm, una altura de {self.altura}cm y esta hecho de {self.material}.")
    
class Pegamento:
    def __init__(self, numero, color, tamaño):
       self.numero = numero
       self.color = color
       self.tamaño = tamaño
    def atributos_pegam(self):
        print(f"Pegamento numero {self.numero}:")
        print(f"El pegamento es de color {self.color} y de tamaño {self.tamaño}.")

class Libreta:
    def __init__(self, numero, color, alt, anch):
       self.numero = numero
       self.color = color
       self.alt = alt
       self.anch = anch
    def atributos_lib(self):
        print(f"Libreta numero {self.numero}:")
        print(f"La libreta es de color {self.color}, tiene una altura de {self.alt}cm y un ancho de {self.anch}cm.")

class Espejo:
    def __init__(self, numero, forma, color, altura):
       self.numero = numero
       self.forma = forma
       self.color = color
       self.altura = altura
    def atributos_espejo(self):
        print(f"Espejo numero {self.numero}")
        print(f"El espejo tiene una forma de {self.forma}, es de color {self.color} y tiene una altura de {self.altura}cm.")

class Telefono:
    def __init__(self, numero, color, tipo, botones ):
        self.numero = numero
        self.color = color
        self.tipo = tipo
        self.botones = botones
       
    def atributos_tel(self):
        print(f"Telefono numero {self.numero}:")
        print(f"El telefono es de color {self.color}, es un telefono {self.tipo} y tiene sus botones en forma de {self.botones}.")

class Pegatinas:
    def __init__(self, numero, color, forma, material):
        self.numero = numero
        self.color = color
        self.forma = forma
        self.material = material
       
    def atributos_pegatinas(self):
        print(f"Juego de pegatinas numero {self.numero}:")
        print(f"Este juego de pegainas es de color {self.color}, en forma de {self.forma} y están hechos de {self.material}.")

class Marcatextos:
    def __init__(self, numero, color, tamaño, punta ):
        self.numero = numero
        self.color = color
        self.tamaño = tamaño
        self.punta = punta
       
    def atributos_marcatextos(self):
        print(f"Marcatextos numero {self.numero}:")
        print(f"El marcatextos es de color {self.color}, mide {self.tamaño}cm y tiene punta {self.punta}.")

class Cinta:
    def __init__(self, numero, color, largo, ancho ):
       self.numero = numero
       self.color = color
       self.largo = largo
       self.ancho = ancho

    def atributos_cinta(self):
        print(f"Cinta numero {self.numero}:")
        print(f"La cinta es de color {self.color}, mide {self.largo}m de largo y {self.ancho}mm de ancho.")

class Caja_de_maquillaje:
    def __init__(self, numero, material, color, sombras):
       self.numero = numero
       self.material = material
       self.color = color
       self.sombras = sombras

    def atributos_c_maqui(self):
        print(f"Caja de maquillaje numero {self.numero}:")
        print(f"La caja de maquillaje esta hecha de {self.material}, es de color {self.color} y contiene {self.sombras} sombras.")

class Pluma_:
    def __init__(self, numero, color, tamaño, tinta, punta):
       self.numero = numero
       self.color = color
       self.tamaño = tamaño
       self.tinta = tinta
       self.punta = punta

    def atributos_pluma(self):
        print(f"Pluma numero {self.numero}:")
        print(f"La pluma es de color {self.color}, mide {self.tamaño}cm, tiene tinta {self.tinta} y es de punta {self.punta}")

class Regla:
    def __init__(self, numero, color, tamaño, material ):
        self.numero = numero
        self.color = color
        self.tamaño = tamaño
        self.material = material
       
    def atributos_regla(self):
        print(f"Regla numero {self.numero}:")
        print(f"La regla es de color {self.color}, tiene un largo de {self.tamaño}cm y esta hecha de {self.material}.")

class Tijeras:
    def __init__(self, numero, color, tipo, punta):
        self.numero = numero
        self.color = color
        self.tipo = tipo
        self.punta = punta
           
    def atributos_tijera(self):
        print(f"Tijeras numero {self.numero}:")
        print(f"Las tijeras son de color {self.color}, de tipo {self.tipo} y tienen su punta {self.punta}.")

class Pinza:
    def __init__(self, numero, tamaño, color, material):
        self.numero = numero
        self.tamaño = tamaño
        self.color = color
        self.material = material
        
    def atributos_pinza(self):
        print(f"Pinza numero {self.numero}:")
        print(f"Esta pinza es {self.tamaño}, tiene un color {self.color} y esta hecha de {self.material}.")

class Cuentas:
    def __init__(self, numero, color, material):
        self.numero = numero
        self.color = color
        self.material = material

    def atributos_cuentas(self):
        print(f"Cuenta numero {self.numero}:")
        print(f"La cuenta es de color {self.color} y esta hecha de {self.material}.")