class Boligrafo:
    def __init__(self,color_empaque,color_tinta,punta,precio):
        self.color_empaque = color_empaque
        self.color_tinta = color_tinta
        self.punta = punta
        self.precio = precio
    def info(self):
        print(f"El empaque tiene un color: {self.color_empaque}")
        print(f"La tinta es color: {self.color_tinta}")
        print(f"El numero de punta es: {self.punta}")
        print(f"El precio es de: ${self.precio}")

class Esmalte:
    def __init__(self,color,tamaño,forma):
        self.color = color
        self.tamaño = tamaño
        self.forma = forma
    def info(self):
        print(f"El color del esmalte es: {self.color}")
        print(f"El tamaño es: {self.tamaño}")
        print(f"La forma es: {self.forma}")
    
class Espejo:
    def __init__(self,color_marco,tamaño,forma):
        self.color_marco = color_marco
        self.tamaño = tamaño
        self.forma = forma
    def info(self):
        print(f"El espejo tiene un marco de color: {self.color_marco}")
        print(f"El tamaño es: {self.tamaño}")
        print(f"La forma del espejo es: {self.forma}")

class Marco:
    def __init__(self,color,tamaño,foto):
        self.color = color
        self.tamaño = tamaño
        self.foto = foto
    def info(self):
        print(f"El color del marco es: {self.color}")
        print(f"El tamaño es: {self.tamaño}")
        print(f"Tiene una foto de: {self.foto}")

class Brillo_labial:
    pass

class Cuaderno:
    pass

class Cinta:
    pass

class Sticker:
    pass

class Cuentas:
    pass

class Tijeras:
    pass

class Pinzas:
    pass