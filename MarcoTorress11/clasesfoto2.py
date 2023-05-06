class Celular:
    def __init__(self, numero, color, tamaño):
        self.color = color
        self.numero = numero
        self.tamaño = tamaño
    
    def atributos_cel(self):
        print(f"Celular {self.numero}")
        print(f"Es de color: {self.color}\ntiene un tamaño de: {self.tamaño} Pulgadas")

class Camisa:
    def __init__(self, numero, color, tamaño, marca, material):
        self.color = color
        self.numero = numero
        self.tamaño = tamaño
        self.marca = marca
        self.material = material
    
    def atributos_camisa(self):
        print(f"Camisa {self.numero}")
        print(f"Es de color: {self.color}, el material de la camisa es: {self.material}, es talla: {self.tamaño} y es de marca: {self.marca}")

class Portafolio:
    def __init__(self, numero, color, tamaño, marca, material):
        self.color = color
        self.numero = numero
        self.tamaño = tamaño
        self.marca = marca
        self.material = material
    
    def info(self):
        print(f"Portafolio {self.numero}")
        print(f"Es de color: {self.color}, esta hecho de: {self.material}, tiene un tamaño: {self.tamaño} y es de la marca: {self.marca}")


class Lentes:
    def __init__(self, numero, color, tamaño, marca, material, aumento):
        self.color = color
        self.numero = numero
        self.tamaño = tamaño
        self.marca = marca
        self.material = material
        self.aumento = aumento
    
    def info_cam(self):
        print(f"Lente de cámara {self.numero}")
        print(f"Es de color: {self.color}, mide: {self.tamaño} cm, es de la marca: {self.marca}, esta hecho de: {self.material} y tiene un aumento de: x{self.aumento} ")
    

class Tapas:
    def __init__(self, numero, color, tamaño, marca, material):
        self.color = color
        self.numero = numero
        self.tamaño = tamaño
        self.marca = marca
        self.material = material

    def info_tapa(self):
        print(f"Tapa {self.numero}")
        print(f"Es de color: {self.color}, mide: {self.tamaño} cm, es de la marca: {self.marca} y esta hecho de {self.material}")


class Computadora:
    def __init__(self, numero, color, tamaño, marca, material, peso):
        self.color = color
        self.numero = numero
        self.tamaño = tamaño
        self.marca = marca
        self.material = material
        self.peso = peso
    
    def info_compu(self):
        print(f"Computadora {self.numero}")
        print(f"Es de color: {self.color}, mide {self.tamaño} pulgadas, es de la marca {self.marca}, esta hecha de {self.material} y pesa {self.peso} kg")

class Pila_portatil:
    def __init__(self, numero, color, tamaño, marca, material, peso, capacidad):
        self.color = color
        self.numero = numero
        self.tamaño = tamaño
        self.marca = marca
        self.material = material
        self.peso = peso
        self.capacidad = capacidad

    def info_pilaP(self):
        print(f"Pila pórtatil {self.numero}")
        print(f"Es de color: {self.color}, mide {self.tamaño} cm de largo, es de la marca {self.marca}, esta hecha de {self.material}, pesa {self.peso} gr y tiene capacidad de {self.capacidad} mAh")
    

class Pila_camara:
    def __init__(self, numero, color, tamaño, marca, material, peso, capacidad):
        self.color = color
        self.numero = numero
        self.tamaño = tamaño
        self.marca = marca
        self.material = material
        self.peso = peso
        self.capacidad = capacidad

    def info_pilaC(self):
        print(f"Pila de cámara {self.numero}")
        print(f"Es de color: {self.color}, mide {self.tamaño} cm de largo, es de la marca {self.marca}, esta hecha de {self.material}, pesa {self.peso} gr y tiene capacidad de {self.capacidad} mAh")
    
    
class Tripode:
    def __init__(self, numero, color, tamaño, tamañomax, marca, material, peso, capacidad):
        self.color = color
        self.numero = numero
        self.tamaño = tamaño
        self.tamañomax = tamañomax
        self.marca = marca
        self.material = material
        self.peso = peso
        self.capacidad = capacidad
    
    def info_tri(self):
        print(f"Tripode {self.numero}")
        print(f"Es de color: {self.color}, mide: {self.tamaño} cm y se puede extender hasta: {self.tamañomax} cm, es de la marca: {self.marca}, esta hecho de: {self.material}, pesa: {self.peso} gr y puede cargar hasta: {self.capacidad} kg")

    
class Zapatos:
    def __init__(self, numero, color, tamaño, marca, material, tipo):
        self.color = color
        self.numero = numero
        self.tamaño = tamaño
        self.marca = marca
        self.material = material
        self.tipo = tipo

    def info_zapato(self):
        print(f"Zapatos {self.numero}")
        print(f"Son de color: {self.color}, son talla: {self.tamaño} cm, son de la marca: {self.marca}, están hechos de: {self.material} y son de tipo {self.tipo}")
    

class Plumas:
    def __init__(self, numero, color, grosor, marca, material):
        self.color = color
        self.numero = numero
        self.grosor = grosor
        self.marca = marca
        self.material = material
    
    def info_plumas(self):
        print(f"Pluma {self.numero}")
        print(f"Es de color: {self.color}, su grosor es de: {self.grosor} mm, es de la marca: {self.marca} y esta hecha de: {self.material}")
    

class Lapiz:
    def __init__(self, numero, color, numerol, marca, material):
        self.color = color
        self.numero = numero
        self.numerol = numerol
        self.marca = marca
        self.material = material

    def info_lapiz(self):
        print(f"Lápiz {self.numero}")
        print(f"Es de color: {self.color}, es del número: {self.numerol}, es de la marca: {self.marca} y esta hecho de: {self.material}")
    

class Estuche:
    def __init__(self, numero, color, tamaño, marca, material):
        self.color = color
        self.numero = numero
        self.tamaño = tamaño
        self.marca = marca
        self.material = material
    
    def info_estuche(self):
        print(f"Estuche {self.numero}")
        print(f"Es de color: {self.color}, esta hecho de: {self.material}, tiene un tamaño: {self.tamaño} y es de la marca: {self.marca}")
    

class Cable:
    def __init__(self, numero, color, tamaño, marca, tipo):
        self.color = color
        self.numero = numero
        self.tamaño = tamaño
        self.marca = marca
        self.tipo = tipo

    def info_cable(self):
        print(f"Cable {self.numero}")
        print(f"Es de color: {self.color},tiene un tamaño de: {self.tamaño}cm, es de la marca: {self.marca} y es de tipo: {self.tipo}")
    

class Reloj:
    def __init__(self, numero, color, tamaño, marca, tipo, material):
        self.color = color
        self.numero = numero
        self.tamaño = tamaño
        self.marca = marca
        self.tipo = tipo
        self.material = material
    
    def info_reloj(self):
        print(f"Reloj {self.numero}")
        print(f"Es de color: {self.color}, tiene un tamaño de: {self.tamaño} mm, es de la marca: {self.marca}, es de tipo: {self.tipo} y esta hecho de: {self.material}")
    

class Revista:
    def __init__(self, numero, color, marca, tipo, material):
        self.color = color
        self.numero = numero
        self.marca = marca
        self.tipo = tipo
        self.material = material

    def info_revista(self):
        print(f"Revista {self.numero}")
        print(f"Es de color: {self.color}, es de la editorial: {self.marca}, es del tipo: {self.tipo} y esta hecha de: {self.material}")

    