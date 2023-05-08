class Estuche_camara:
    def __init_(self,tamaño,color,marca):
        self.tamaño=tamaño
        self.color=color
        self.marca = marca
         
    
    def imprimir(self):
        print(f"El estuche es de color:{self.color},su tamao es de:{self.tamaño}, y es de la marca:{self.marca}")

class Chaqueta:
    def __init_(self,talla,color):
        self.talla=talla
        self.color=color
         
    
    def imprimir(self):
        print(f"La chaqueta es de color:{self.color},y su talla es:{self.talla}")

class Marcador:
    def __init_(self,tamaño,color,marca):
        self.tamaño=tamaño
        self.color=color
        self.marca=marca
    
    def imprimir(self):
        print(f"El marcador es de color:{self.color},es de la marca {self.marca},y su tamaño es:{self.tamaño}")

class Lapiz:
    def __init_(self,tamaño,color,marca):
        self.tamaño=tamaño
        self.color=color
        self.maraca= marca
    
    def imprimir(self):
        print(f"El lapiz es de color:{self.color},es de la marca {self.marca},y su tamaño es:{self.tamaño}")

class Zapatos:
    def __init_(self,talla,color,marca):
        self.talla=talla
        self.color=color
        self.marca= marca
    
    def imprimir(self):
        print(F"Los zapatos son color:{self.color},su talla es:{self.talla},y son de la marca{self.marca}")
