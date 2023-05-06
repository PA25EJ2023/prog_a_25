class Pila_portatil:
    def __init__(self, numero, color, tamaño):
          self.numero = numero
          self.color = color
          self.tamaño = tamaño
    def atributos_pila_P(self):
        print(f"Pila portatil numero {self.numero}:")
        print(f"La pila portatil es de color {self.color} y el tamaño es de {self.tamaño} pulgadas")

class Camisa:
    def __init__(self, numero, marca, color, talla, material):
        self.numero = numero
        self.marca = marca
        self.color = color
        self.talla = talla
        self.material = material
        
    def atributos_camisa(self):
        print(f"Camisa numero {self.numero}:")
        print(f"La camisa es marca {self.marca}, es de color {self.color}, su talla es {self.talla} y es de {self.material}")
class Celular:
    def __init__(self, numero, color, tamaño,):
        self.numero = numero
        self.color = color
        self.tamaño = tamaño
    def atributos_cel(self):
        print(f"Celular numero {self.numero}:")
        print(f"El celular es de color {self.color} y su tamaño es de {self.tamaño} pulgadas")

class Reloj:
    def __init__(self, numero, color, tamaño, tipo):
        self.numero = numero
        self.color = color
        self.tamaño = tamaño
        self.tipo = tipo

    def atributos_reloj(self):
        print(f"Reloj numero {self.numero}:")
        print(f"El reloj es de color {self.color}, su tamaño es de {self.tamaño}cm y es de tipo {self.tipo}")

class Revista:
    def __init__(self, numero, tamaño, tipo, color):
        self.numero = numero
        self.tamaño = tamaño
        self.tipo = tipo
        self.color = color

    def atributos_revista(self):
        print(f"Revista numero {self.numero}:")
        print(f"El tamaño de la revista es de {self.tamaño}cm de alto, es una revista de {self.tipo} y es de color {self.color}")

class Lentes_camara:
    def __init__(self, numero, tamaño, color, aumento):
        self.numero = numero
        self.tamaño = tamaño
        self.color = color
        self.aumento = aumento

    def atributos_lentes(self):
        print(f"Lente numero {self.numero}:")
        print(f"El lente de la camara es de color {self.color}, mide {self.tamaño} pulgadas y tiene un aumento de {self.aumento}X") 

class Baterias_camara:
    def __init__(self, numero, capacidad, tamaño, color):
        self.numero = numero
        self.capacidad = capacidad
        self.tamaño = tamaño
        self.color = color
    def atributos_bat(self):
        print(f"Bateria numero {self.numero}:")
        print(f"La bateria es de {self.capacidad}mAh, mide {self.tamaño} pulgadas y tiene un color {self.color}")

class Portafolio:
    def __init__(self, numero, tamaño, material, color,):
        self.numero = numero
        self.tamaño = tamaño
        self.material = material
        self.color = color

    def atributos_port(self):
        print(f"Portafolio numero {self.numero}:")
        print(f"El portafolio es de {self.tamaño} pulgadas, esta hecho de {self.material} y es color {self.color}")

class Tripie: 
    def __init__(self, numero, color, altura, marca):
        self.numero = numero
        self.color = color
        self.altura = altura
        self.marca = marca

    def atributos_trip(self):
        print(f"Tripie numero {self.numero}:")
        print(f"El tripie es color {self.color}, tiene una altura de {self.altura}cm y es de la marca {self.marca}")

class Macbook:
    def __init__(self, numero, marca, color, tamaño):
        self.numero = numero
        self.marca = marca
        self.tamaño = tamaño
        self.color = color
    def atributos_mac(self):
        print(f"Laptop numero {self.numero}:")
        print(f"La computadora es de marca {self.marca}, color {self.color} y es de {self.tamaño} pulgadas")

class Zapatos:
    def __init__(self, numero, color, estilo, talla, material):
        self.numero = numero
        self.color = color
        self.estilo = estilo
        self.talla = talla
        self.material = material

    def atributos_zapatos(self):
        print(f"Zapatos numero {self.numero}:")
        print(f"Los zapatos son de color {self.color}, estilo {self.estilo}, talla {self.talla} y esta hecho de {self.material}")

class Cable:
    def __init__(self, numero, color, largo,):
        self.numero = numero
        self.color = color
        self.largo = largo

    def atributos_cable(self):
        print(f"Cable numero {self.numero}:")
        print(f"El cable es de color {self.color} y mide {self.largo}cm")

class Plumas: 
    def __init__(self, numero, material, color, tinta, tamaño, punta):
        self.numero = numero
        self.material = material
        self.color = color
        self.tinta = tinta
        self.tamaño = tamaño
        self.punta = punta

    def atributos_pluma(self):
        print(f"Pluma numero {self.numero}:")
        print(f"La pluma es de {self.material}, color {self.color}, tinta {self.tinta}, mide {self.tamaño}cm y su punta es de {self.punta}mm")

class Lapices:
    def __init__(self, numero, material, color, tamaño, punta):
        self.numero = numero
        self.material = material
        self.color = color
        self.tamaño = tamaño
        self.punta = punta

    def atributos_lapiz(self):
        print(f"Lapiz numero {self.numero}:")
        print(f"El lapiz es de {self.material}, tiene un color {self.color}, mide {self.tamaño}cm y su punta es de {self.punta}")

class Estuche_camara:
    def __init__(self, numero, color, capacidad, material):
        self.numero = numero
        self.color = color
        self.capacidad = capacidad
        self.material =material

    def atributos_estu(self):
        print(f"Estuche numero {self.numero}:")
        print(f"El estuche de la camara es de color {self.color}, es para una camara de tamaño {self.capacidad} y esta hecho de {self.material}")

class Tapas_camara:
    def __init__(self, numero, color, marca):
        self.numero = numero
        self.color = color
        self.marca = marca

    def atributos_tapas(self):
        print(f"Tapa numero {self.numero}:")
        print(f"La tapa del lente es color {self.color} y de la marca {self.marca}")