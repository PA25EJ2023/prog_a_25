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
    def __init__(self, numero, base, altura, material, color ):
       self.numero = numero
       self.base = base
       self.altura = altura
       self.material = material
       self.color = color
    def atributos_marco(self):
        print(f"Marco numero {self.numero}:")
        print(f"El marco tiene como medidas una base de {self.base}cm, una altura de {self.altura}cm, esta hecho de {self.material} y es de color {self.color}.")
    
class Pegamento:
    def __init__(self, numero, tipo, color, tamaño, material, ):
       self.numero = numero
       self.tipo = tipo
       self.color = color
       self.tamaño = tamaño
       self.material = material
    def atributos_pegam(self):
        print(f"Pegamento numero {self.numero}:")
        print(f"El pegamento es de {self.tipo}, color {self.color}, de tamaño {self.tamaño} y es de {self.material}.")

class Libreta:
    def __init__(self, numero, color, alt, anch, pasta):
       self.numero = numero
       self.color = color
       self.alt = alt
       self.anch = anch
       self.past = pasta
    def atributos_lib(self):
        print(f"Libreta numero {self.numero}:")
        print(f"La libreta es de color {self.color}, tiene una altura de {self.alt}cm, un ancho de {self.anch}cm y su pasta es {self.past}.")

class Espejo:
    def __init__(self, numero, forma, color, altura, material):
       self.numero = numero
       self.forma = forma
       self.color = color
       self.altura = altura
       self.mat = material
    def atributos_espejo(self):
        print(f"Espejo numero {self.numero}")
        print(f"El espejo tiene una forma de {self.forma}, es de color {self.color}, tiene una altura de {self.altura}cm y es de {self.mat}.")

class Telefono:
    def __init__(self, numero, color, cable, tipo, botones ):
        self.numero = numero
        self.color = color
        self.cable = cable
        self.tipo = tipo
        self.botones = botones
       
    def atributos_tel(self):
        print(f"Telefono numero {self.numero}:")
        print(f"El telefono es de color {self.color}, el cable es color {self.cable} es un telefono {self.tipo} y tiene sus botones en forma de {self.botones}.")

class Pegatinas:
    def __init__(self, numero, tamaño, color, forma, material):
        self.numero = numero
        self.tamaño = tamaño
        self.color = color
        self.forma = forma
        self.material = material
       
    def atributos_pegatinas(self):
        print(f"Juego de pegatinas numero {self.numero}:")
        print(f"Este juego de pegainas es {self.tamaño}, de color {self.color}, en forma de {self.forma} y están hechos de {self.material}.")

class Marcatextos:
    def __init__(self, numero, comp, color, tamaño, punta ):
        self.numero = numero
        self.comp = comp
        self.color = color
        self.tamaño = tamaño
        self.punta = punta
       
    def atributos_marcatextos(self):
        print(f"Marcatextos numero {self.numero}:")
        print(f"El marcatextos es {self.comp}, de color {self.color}, mide {self.tamaño}cm y tiene punta {self.punta}.")

class Cinta:
    def __init__(self, numero, color, largo, ancho, kg ):
       self.numero = numero
       self.color = color
       self.largo = largo
       self.ancho = ancho
       self.kg = kg

    def atributos_cinta(self):
        print(f"Cinta numero {self.numero}:")
        print(f"La cinta es de color {self.color}, mide {self.largo}m de largo,  {self.ancho}mm de ancho y pesa {self.kg}g.")

class Caja_de_maquillaje:
    def __init__(self, numero, material, color, sombras, kg):
       self.numero = numero
       self.material = material
       self.color = color
       self.sombras = sombras
       self.kg = kg

    def atributos_c_maqui(self):
        print(f"Caja de maquillaje numero {self.numero}:")
        print(f"La caja de maquillaje esta hecha de {self.material}, es de color {self.color}, contiene {self.sombras} sombras y pesa {self.kg}g.")

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
    def __init__(self, numero, color, tamaño, form, material ):
        self.numero = numero
        self.color = color
        self.tamaño = tamaño
        self.forma = form
        self.material = material
       
    def atributos_regla(self):
        print(f"Regla numero {self.numero}:")
        print(f"La regla es de color {self.color}, tiene un largo de {self.tamaño}cm, es en forma de {self.forma} y esta hecha de {self.material}.")

class Tijeras:
    def __init__(self, numero, color, tipo, punta, kg):
        self.numero = numero
        self.color = color
        self.tipo = tipo
        self.punta = punta
        self.kg = kg
           
    def atributos_tijera(self):
        print(f"Tijeras numero {self.numero}:")
        print(f"Las tijeras son de color {self.color}, de tipo {self.tipo}, tienen su punta {self.punta} y pesa {self.kg}g.")

class Pinza:
    def __init__(self, numero, tamaño, color, material, kg):
        self.numero = numero
        self.tamaño = tamaño
        self.color = color
        self.material = material
        self.kg = kg
        
    def atributos_pinza(self):
        print(f"Pinza numero {self.numero}:")
        print(f"Esta pinza es {self.tamaño}, tiene un color {self.color}, esta hecha de {self.material} y pesa {self.kg}g.")

class Cuentas:
    def __init__(self, numero, tamaño, color, material, kg):
        self.numero = numero
        self.tamaño = tamaño
        self.color = color
        self.material = material
        self.kg = kg

    def atributos_cuentas(self):
        print(f"Cuenta numero {self.numero}:")
        print(f"La cuenta es {self.tamaño}, de color {self.color}, esta hecha de {self.material} y pesa {self.kg}g.")