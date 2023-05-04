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
    def __init__(self,color,tamaño,precio):
        self.color = color
        self.tamaño = tamaño
        self.precio = precio
    def info(self):
        print(f"El color del brillo es: {self.color}")
        print(f"El tamaño es: {self.tamaño}")
        print(f"Su precio es de: ${self.precio}")    

class Cuaderno:
    def __init__(self,tipo_hoja,color,tipo):
        self.tipo_hoja = tipo_hoja
        self.color = color
        self.tipo = tipo
    def info(self):
        print(f"El tipo de hojas es: {self.tipo_hoja}")
        print(f"El color es: {self.color}")
        print(f"El tipo es de: {self.tipo}")   
        
class Cinta:
    def __init__(self,color,tamaño):
        self.color = color
        self.tamaño = tamaño
    def info(self):
        print(f"El color es: {self.color}")
        print(f"El tamaño es: {self.tamaño}")    

class Sticker:
    def __init__ (self,forma,color,tamaño):
        self.forma = forma
        self.color = color
        self.tamaño = tamaño
    def info(self):
        print(f"El color es: {self.color}")
        print(f"El tamaño es: {self.tamaño}")
        print(f"Su forma es: {self.forma}")    

class Cuenta:
    def __init__(self,tamaño,forma,color):
        self.forma = forma
        self.color = color
        self.tamaño = tamaño
    def info(self):
        print(f"El color es: {self.color}")
        print(f"El tamaño es: {self.tamaño}")
        print(f"Su forma es: {self.forma}")    

class Tijera:
    def __init__(self,color,tamaño):
        self.color = color
        self.tamaño = tamaño
    def info(self):
        print(f"El color es: {self.color}")
        print(f"El tamaño es: {self.tamaño}")

class Pinza:
    def __init__(self,color,tamaño,precio):
        self.color = color
        self.tamaño = tamaño
        self.precio = precio
    def info(self):
        print(f"El color es: {self.color}")
        print(f"El tamaño es: {self.tamaño}")
        print(f"Su precio es de: ${self.precio}")   

class Telefono:
    def __init__(self,color,precio):
        self.color = color
        self.precio = precio
    def info(self):
        print(f"El color es: {self.color}")
        print(f"Su precio es de: ${self.precio}") 
        
class Plumon:
    def __init__(self,color,precio,marca):
        self.color = color
        self.precio = precio
        self.marca = marca
    def info(self):
        print(f"El color es: {self.color}")
        print(f"Su precio es de: ${self.precio}") 
        print(f"La marca es: {self.marca}")

class Regla:
    def __init__(self,color,precio):
        self.color = color
        self.precio = precio
    def info(self):
        print(f"El color es: {self.color}")
        print(f"Su precio es de: ${self.precio}") 

class Pegamento:
    def __init__(self,color_empaque,precio,marca):
        self.color_empaque = color_empaque
        self.precio = precio
        self.marca = marca
    def info(self):
        print(f"El color del empaque es: {self.color_empaque}")
        print(f"Su precio es de: ${self.precio}")
        print(f"La marca es: {self.marca}")
        