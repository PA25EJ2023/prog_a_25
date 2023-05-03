class Celular:
    def __init__(self, color, tamaño):
        self.color = color
        self.tamaño = tamaño
    
    def atributos_cel(self):
        print(f"El celular es de color: {self.color}")
        print(f"Tiene un tamaño de: {self.tamaño} Pulgadas")

class Camisa:
    def __init__(self, color, tamaño, marca, material):
        self.color = color
        self.tamaño = tamaño
        self.marca = marca
        self.material = material
    
    def atributos_camisa(self):
        print(f"La camisa es de color: {self.color}, el material de la camisa es: {self.material}, es talla: {self.tamaño} y es de marca: {self.marca}")

class Portafolio:
    def __init__(self, color, tamaño, marca, material):
        self.color = color
        self.tamaño = tamaño
        self.marca = marca
        self.material = material
    
    def info(self):
        print(f"La camisa es de color: {self.color}, el material de la camisa es: {self.material}, es talla: {self.tamaño} y es de marca: {self.marca}")


class Lentes:
    def __init__(self, color, tamaño, marca, material, aumento):
        self.color = color
        self.tamaño = tamaño
        self.marca = marca
        self.material = material
        self.aumento = aumento
    
    def info_cam(self):
        print(f"El lente de la camara es de color: {self.color}, mide: {self.tamaño} cm, es de la marca: {self.marca}, esta hecho de: {self.material} y tiene un aumento de {self.aumento} ")
    

class Tapas:
    def __init__(self, color, tamaño, marca, material):
        self.color = color
        self.tamaño = tamaño
        self.marca = marca
        self.material = material

    def info_tapa(self):
        print(f"La tapa de la camara es de color: {self.color}, mide: {self.tamaño} cm, es de la marca: {self.marca} y esta hecho de {self.material}")


class Computadora:
    def __init__(self, color, tamaño, marca, material, peso):
        self.color = color
        self.tamaño = tamaño
        self.marca = marca
        self.material = material
        self.peso = peso
    
    def info_compu(self):
        print(f"La computadora es de color: {self.color}, mide {self.tamaño} cm de largo, es de la marca {self.marca}, esta hecha de {self.material} y pesa {self.peso} kg")

class Pila_portatil:
    def __init__(self, color, tamaño, marca, material, peso, capacidad):
        self.color = color
        self.tamaño = tamaño
        self.marca = marca
        self.material = material
        self.peso = peso
        self.capacidad = capacidad

    def info_pilaP(self):
        print(f"La pila portatil es de color: {self.color}, mide {self.tamaño} cm de largo, es de la marca {self.marca}, esta hecha de {self.material}, pesa {self.peso} gr y tiene capacidad de {self.capacidad} mAh")
    

class Pila_camara:
    def __init__(self, color, tamaño, marca, material, peso, capacidad):
        self.color = color
        self.tamaño = tamaño
        self.marca = marca
        self.material = material
        self.peso = peso
        self.capacidad = capacidad

    def info_pilaP(self):
        print(f"La pila de la camara es de color: {self.color}, mide {self.tamaño} cm de largo, es de la marca {self.marca}, esta hecha de {self.material}, pesa {self.peso} gr y tiene capacidad de {self.capacidad} mAh")
    
    
class Tripode:
    def __init__(self, color, tamaño, tamañomax, marca, material, peso, capacidad):
        self.color = color
        self.tamaño = tamaño
        self.tamañomax = tamañomax
        self.marca = marca
        self.material = material
        self.peso = peso
        self.capacidad = capacidad
    
    def info_tri(self):
        print(f"El tripode es de color: {self.color}, mide: {self.tamaño} cm y se puede extender hasta: {self.tamañomax} cm, es de la marca: {self.marca}, esta hecho de: {self.material}, pesa: {self.peso} gr y puede cargar hasta: {self.capacidad} kg")

    
class Zapatos:
    def __init__(self, color, tamaño, marca, material, tipo):
        self.color = color
        self.tamaño = tamaño
        self.marca = marca
        self.material = material
        self.tipo = tipo

    def info_zapato(self):
        print(f"Los zapatos son de color: {self.color}, son talla: {self.tamaño} cm, son de la marca: {self.marca}, están hechos de: {self.material} y son de tipo {self.tipo}")
    

#class plumas:
    

#class lapiz:
    

#class estuche:
    

#class cable:
    

#class reloj:
    

#class revista:
    
cta1 = Celular("negro","25")
cta1.atributos_cel()


