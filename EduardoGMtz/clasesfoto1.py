class Pila_portatil:
    def __init__(self, color, tamaño):
          self.color = color
          self.tamaño = tamaño

    def atributos_pila_P(self):
        print(f"La pila portatil es de color {self.color} y el tamaño es de {self.tamaño} pulgadas")


class Camisa:
    def __init__(self, marca, color, talla, material, botones):
        self.marca = marca
        self.color = color
        self.talla = talla
        self.material = material
        self.botones = botones

    def atributos_camisa(self):
        print(f"La camisa es marca {self.marca}, es de color {self.color}, su talla es {self.talla}, es de {self.material} y tiene {self.botones} botones")


class Camisan:
    def __init__(self, marca, color, talla, material):
        self.marca = marca
        self.color = color
        self.talla = talla
        self.material = material

    def atributos_camisa_n(self):
        print(f"La segunda camisa es marca {self.marca}, es de color {self.color}, su talla es {self.talla}, es de {self.material} y no tiene botones")

class Celular:
    def __init__(self, color, tamaño,):
        self.color = color
        self.tamaño = tamaño

    def atributos_cel(self):
        print(f"El celular es de color {self.color} y su tamaño es de {self.tamaño} pulgadas")

class Reloj:
    def __init__(self, color, tamaño, tipo):
        self.color = color
        self.tamaño = tamaño
        self.tipo = tipo

    def atributos_reloj(self):
        print(f"El reloj es de color {self.color}, su tamaño es de {self.tamaño}cm y es de tipo {self.tipo}")

class Revista:
    def __init__(self, tamaño, tipo, color):
        self.tamaño = tamaño
        self.tipo = tipo
        self.color = color

    def atributos_revista(self):
        print(f"El tamaño de la revista es de {self.tamaño}cm de alto, es una revista de {self.tipo} y es de color {self.color}")

class Lentes_camara:
    def __init__(self, tamaño, color, aumento):
        self.tamaño = tamaño
        self.color = color
        self.aumento = aumento

    def atributos_lentes(self):
        print(f"Los lentes de la camara son de color {self.color}, son de {self.tamaño} pulgadas y tienen un aumento de {self.aumento}X") 
    

class Baterias_camara:
    def __init__(self, capacidad, tamaño, color):
        self.capacidad = capacidad
        self.tamaño = tamaño
        self.color = color

    def atributos_bat(self):
        print(f"Las baterias de la camara son de {self.capacidad}mAh, es de {self.tamaño} pulgadas y de color {self.color}")

class Portafolio:
    def __init__(self, tamaño, material, color,):
        self.tamaño = tamaño
        self.material = material
        self.color = color

    def atributos_port(self):
        print(f"El portafolio es de {self.tamaño} pulgadas, esta hecho de {self.material} y es color {self.color}")

class Tripie: 
    def __init__(self, color, altura, marca):
        self.color = color
        self.altura = altura
        self.marca = marca

    def atributos_trip(self):
        print(f"El tripie es color {self.color}, tiene una altura de {self.altura}cm y es de la marca {self.marca}")

class Macbook:
    def __init__(self, marca, color, tamaño):
        self.marca = marca
        self.tamaño = tamaño
        self.color = color

    def atributos_mac(self):
        print(f"La computadora es de marca {self.marca}, color {self.color} y es de {self.tamaño} pulgadas")

class Zapatos:
    def __init__(self, color, estilo, talla, material):
        self.color = color
        self.estilo = estilo
        self.talla = talla
        self.material = material

    def atributos_zapatos(self):
        print(f"Los zapatos son de color {self.color}, talla {self.talla}, estilo {self.estilo} y de {self.material}")

class Cable:
    def __init__(self, color, largo,):
        self.color = color
        self.largo = largo

    def atributos_cable(self):
        print(f"El cable es de color {self.color} y mide {self.largo}cm")

class Plumas:
    def __init__(self, material, color, tinta, tamaño, punta):
        self.material = material
        self.color = color
        self.tinta = tinta
        self.tamaño = tamaño
        self.punta = punta

    def atributos_pluma(self):
        print(f"Las plumas son de {self.material}, color {self.color}, tinta {self.tinta}, mide {self.tamaño}cm y su punta es de {self.punta}mm")

class Lapices:
    def __init__(self, material, color, tamaño, punta):
        self.material = material
        self.color = color
        self.tamaño = tamaño
        self.punta = punta

    def atributos_lapiz(self):
        print(f"Los lapices son de {self.material}, color {self.color}, mide {self.tamaño}cm y su punta es de {self.punta}")

class Estuche_camara:
    def __init__(self, color, capacidad, material):
        self.color = color
        self.capacidad = capacidad
        self.material =material

    def atributos_estu(self):
        print(f"El estuche de la camara es de color {self.color}, es para una camara de tamaño {self.capacidad} y esta hecho de {self.material}")

class Tapas_camara:
    def __init__(self, color, marca):
        self.color = color
        self.marca = marca

    def atributos_tapas(self):
        print(f"Las tapas de los lentes de la camara son marca {self.marca} y son de color {self.color}")
