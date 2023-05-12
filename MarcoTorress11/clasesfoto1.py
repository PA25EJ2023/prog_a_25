class Libreta:
    def __init__(self, numero, color, tamaño, tipo):
        self.color = color
        self.numero = numero
        self.tamaño = tamaño
        self.tipo = tipo
    
    def info_libreta(self):
        print(f"Libreta {self.numero}")
        print(f"Es de color: {self.color}, es de tamaño: {self.tamaño} y es: {self.tipo}")

class Espejo:
    def __init__(self, numero, color, tamaño, forma, marca):
        self.color = color
        self.numero = numero
        self.tamaño = tamaño
        self.forma = forma
        self.marca = marca
    
    def info_espejo(self):
        print(f"Libreta {self.numero}")
        print(f"Es de color: {self.color}, es de tamaño: {self.tamaño}, tiene forma de {self.forma} y es de la marca: {self.marca}")

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
    def __init__(self, numero, color, forma, marca, cantidad):
        self.color = color
        self.numero = numero
        self.forma = forma
        self.marca = marca
        self.cantidad = cantidad
    
    def info_esmalte(self):
        print(f"Esmalte {self.numero}")
        print(f"Es de color: {self.color}, tiene forma de {self.forma}, es de la marca: {self.marca} y tiene cantidad de: {self.cantidad} ml")

class Tijeras:
    def __init__(self, numero, color, material, marca, tipo):
        self.numero = numero
        self.color = color
        self.material = material
        self.marca = marca
        self.tipo = tipo
    
    def info_tijeras(self):
        print(f"Tijeras {self.numero}")
        print(f"Son de color: {self.color}, están hechas de: {self.material}, son de la marca: {self.marca} y son de tipo {self.tipo}")

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
    def __init__(self, numero, color, tamaño, material, marca):
        self.color = color
        self.numero = numero
        self.tamaño = tamaño
        self.material = material
        self.marca = marca

    def info_pinza(self):
        print(f"Pinza {self.numero}")
        print(f"Es de color: {self.color}, es de tamaño: {self.tamaño}, esta hecha de: {self.material} y es de la marca: {self.marca}")

class Pegamento:
    def __init__(self, numero, color, tamaño, forma, marca):
        self.color = color
        self.numero = numero
        self.tamaño = tamaño
        self.forma = forma
        self.marca = marca

    def info_pegamento(self):
        print(f"Pegamento {self.numero}")
        print(f"Es de color: {self.color}, es de tamaño: {self.tamaño}, tiene forma de: {self.forma} y es de la marca: {self.marca}")

class Cinta:
    def __init__(self, numero, color, tamaño, largo):
        self.color = color
        self.numero = numero
        self.tamaño = tamaño
        self.largo = largo

    def info_cinta(self):
        print(f"Pinza {self.numero}")
        print(f"Es de color: {self.color}, es de tamaño: {self.tamaño} y tiene un largo de {self.largo} m")

class Stickers:
    def __init__(self, numero, color, forma, cantidad ):
        self.color = color
        self.numero = numero
        self.forma = forma
        self.cantidad = cantidad

    def info_sticker(self):
        print(f"Sticker {self.numero}")
        print(f"Es de color: {self.color}, tienen forma de: {self.forma} y son: {self.cantidad} en total")

class Cuentas:
    def __init__(self, numero, color, material, marca):
        self.color = color
        self.numero = numero
        self.material = material
        self.marca = marca

    def info_cuentas(self):
        print(f"Cuenta {self.numero}")
        print(f"Es de color: {self.color}, están hechas de: {self.material} y son de la marca: {self.marca}")

class Maquillaje:
    def __init__(self, numero, color, tamaño, colores):
        self.color = color
        self.numero = numero
        self.tamaño = tamaño
        self.colores = colores

    def info_maquillaje(self):
        print(f"Maquillaje {self.numero}")
        print(f"Es de color: {self.color}, es de tamaño: {self.tamaño} y tiene: {self.colores} colores diferentes de maquillaje")

class Fotos:
    def __init__(self, numero, imagen, tamaño, material):
        self.imagen = imagen
        self.numero = numero
        self.tamaño = tamaño
        self.material = material

    def info_fotos(self):
        print(f"Foto {self.numero}")
        print(f"En la foto aparece una: {self.imagen}, mide: {self.tamaño} cm, y esta impresa en: {self.material}")

class Regla:
    def __init__(self, numero, color, tamaño, material):
        self.color = color
        self.numero = numero
        self.tamaño = tamaño
        self.material = material

    def info_regla(self):
        print(f"Regla {self.numero}")
        print(f"Es de color: {self.color}, mide: {self.tamaño} cm y esta hecha de: {self.material}")
