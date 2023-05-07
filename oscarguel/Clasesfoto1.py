class Pluma:
    def __init__(self,color_empaque,color_tinta,tamaño,precio):
        self.color_empaque = color_empaque
        self.color_tinta = color_tinta
        self.tamaño = tamaño
        self.precio = precio

    def imprimir(self):
        print(f"Color de empaque={self.color_empaque},Color de tinta={self.color_tinta},Tamaño={self.tamaño},Precio={self.precio}")

class Retrato:
    def __init_(self,largo,ancho,material):
        self.largo=largo
        self.ancho= ancho
        self.material =material 
    def imprimir(self):
        print(F"Tiene un largo de:{self.largo},un ancho de:{self.ancho}, y el material del que esta echo es de:{self.material}")

class Esmalte:
    def __init_(self,color,forma,precio):
        self.color=color
        self.forma= forma
        self.precio= precio

    def imprimir(self):
        print(f"Color={self.color},Forma={self.forma},Precio={self.precio}")

class Cinta:
    def __init_(self,color,ancho,longuitud):
        self.color=color
        self.ancho= ancho
        self.longuitud= longuitud
        

    def imprimir(self):
        print(F"El color es:{self.color},tiene un ancho de:{self.ancho},y una longuitud de:{self.longuitud}")



class Pegamento:
    def __init_(self,color,marca,tipo):
        self.color=color
        self.tipo= tipo
        self.marca= marca

    def imprimir(self):
        print(f"El color es={self.color},el tipo de pegamento es={self.tipo},y es de la marca={self.marca}")

class Tijeras:
    def __init_(self,color,marca):
        self.color=color
        self.marca= marca

    def imprimir(self):
        print(f"El color es={self.color},y es de la marca={self.marca}")

class Espejo:
    def __init_(self,color,marca,forma):
        self.color=color
        self.forma= forma
        self.marca= marca
    
    def imprimir(self):
        print(f"El espejo tiene una forma de={self.forma}, es de color={self.color},y es de la marca={self.marca}")

class Telefono:
     def __init__(self,color,tipo):
        self.color=color
        self.tipo=tipo

     def imprimir(self):
        print(f"El telefono es de colo:{self.color},y es de tipo={self.tipo}")

class Pinzas:
     def __init__(self,color,tamaño):
        self.color=color
        self.tamaño=tamaño
        
     def imprimir(self):
        print(f"La pinza es de colo:{self.color},y de tamaño de={self.tamaño}")



    


