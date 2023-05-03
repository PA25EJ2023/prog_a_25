class Pluma:
    def __init__(self,color_empaque,color_tinta,tamaño,precio):
        self.color_empaque = color_empaque
        self.color_tinta = color_tinta
        self.tamaño = tamaño
        self.precio = precio
    def info(self):
        print(f"El empaque es color: {self.color_empaque}")
        print(f"La tinta es color: {self.color_tinta}")
        print(f"El tamaño es: {self.tamaño}")
        print(f"El precio es : {self.precio}")

class Retrato:
    def __init_(self,largo,ancho):
        self.largo=largo
        self.ancho= ancho
        

    def info(self):
        print(f"El largo es de: {self.largo}")
        print(f"El ancho es de: {self.ancho}")

    def imprimir(self):
        print({self.largo},{self.ancho})

class Esmalte:
    def __init_(self,color,forma,precio):
        self.color=color
        self.forma= forma
        self.precio= precio
        
        

    def info(self):
        print(f"El color es: {self.color}")
        print(f"La forma es: {self.forma}")
        print(f"Elprecio es de: {self.precio}")

    def imprimir(self):
        print({self.color},{self.forma},{self.precio})

class Cinta:
    def __init_(self,color,ancho,longuitud):
        self.color=color
        self.ancho= ancho
        self.longuitud= longuitud
        
        

    def info(self):
        print(f"El colo es: {self.color}")
        print(f"El ancho es: {self.ancho}")
        print(f"La longuitud es: {self.longuitud}")

    def imprimir(self):
        print({self.color},{self.ancho},{self.longuitud})
