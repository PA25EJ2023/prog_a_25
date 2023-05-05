class Libreta:
    def __init__(self, numero, color, tamaño, tipo):
        self.color = color
        self.numero = numero
        self.tamaño = tamaño
        self.tipo = tipo
    
    def info_libreta(self):
        print(f"Libreta {self.numero}")
        print(f"Es de color: {self.color}, es de tamaño: {self.tamaño} y es {self.tipo}")

class Espejo:
    def __init__(self, numero, color, tamaño, forma):
        self.color = color
        self.numero = numero
        self.tamaño = tamaño
        self.forma = forma
    
    def info_espejo(self):
        print(f"Libreta {self.numero}")
        print(f"Es de color: {self.color}, es de tamaño: {self.tamaño} y tiene forma de {self.forma}")

class Marco:
    def __init__(self, numero, color, tamaño, forma, decoracion):
        self.color = color
        self.numero = numero
        self.tamaño = tamaño
        self.forma = forma
        self.decoracion = decoracion
    
    def info_marco(self):
        print(f"Marco {self.numero}")
        print(f"Es de color: {self.color}, es de tamaño: {self.tamaño}, tiene forma de {self.forma} y esta decorado con: {self.decoracion}")

class Esmalte:
    def __init__(self, numero, color, forma):
        self.color = color
        self.numero = numero
        self.forma = forma
    
    def info_esmalte(self):
        print(f"Esmalte {self.numero}")
        print(f"Es de color: {self.color} y tiene forma de {self.forma}")

class Tijeras:
    def __init__(self, numero, color, material, tipo):
        self.color = color
        self.numero = numero
        self.material = material
        self.tipo = tipo
    
    def info_espejo(self):
        print(f"Tijeras {self.numero}")
        print(f"Son de color: {self.color} y están hechas de: {self.material}")

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

class Plumones:
    def __init__(self, numero, color, grosor, marca, material):
        self.color = color
        self.numero = numero
        self.grosor = grosor
        self.marca = marca
        self.material = material
    
    def info_plumon(self):
        print(f"Plumón {self.numero}")
        print(f"Es de color: {self.color}, su grosor es de: {self.grosor} mm, es de la marca: {self.marca} y esta hecha de: {self.material}")

class Pinza_pelo:
    def __init__(self, numero, color, tamaño, material):
        self.color = color
        self.numero = numero
        self.tamaño = tamaño
        self.material = material

    def info_pinza(self):
        print(f"Pinza {self.numero}")
        print(f"Es de color: {self.color}, es de tamaño: {self.tamaño} y esta hecha de: {self.material}")

class Pegamento:
    def __init__(self, numero, color, tamaño, forma):
        self.color = color
        self.numero = numero
        self.tamaño = tamaño
        self.forma = forma

    def info_pinza(self):
        print(f"Pegamento {self.numero}")
        print(f"Es de color: {self.color}, es de tamaño: {self.tamaño} y tiene forma de: {self.forma}")

class Cinta:
    def __init__(self, numero, color, tamaño):
        self.color = color
        self.numero = numero
        self.tamaño = tamaño

    def info_pinza(self):
        print(f"Pinza {self.numero}")
        print(f"Es de color: {self.color} y es de tamaño: {self.tamaño}")

class Stickers:
    def __init__(self, numero, color, tamaño, forma):
        self.color = color
        self.numero = numero
        self.tamaño = tamaño
        self.forma = forma

    def info_pinza(self):
        print(f"Pinza {self.numero}")
        print(f"Es de color: {self.color}, es de tamaño: {self.tamaño} y tienen forma de: {self.forma}")
