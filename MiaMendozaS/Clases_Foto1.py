class Boligrafo:
    def __init__(self,tamaño,color,marca,precio):
        self.tamaño= tamaño
        self.color= color
        self.marca= marca
        self.precio= precio 

    def mostrar_info(self):
        print(f"Tamaño: {self.tamaño} \nColor: {self.color} \nMarca: {self.marca} \nPrecio: {self.precio}")

class Marcador:
    def __init__(self,tamaño,color,marca,precio):
        self.tamaño= tamaño
        self.color= color
        self.marca= marca
        self.precio= precio 

    def mostrar_info(self):
        print(f"Tamaño: {self.tamaño} \nColor: {self.color} \nMarca: {self.marca} \nPrecio: {self.precio}")
    
class Cinta:
    def __init__(self,color,longitud,ancho,marca):
        self.color= color
        self.longitud= longitud
        self.ancho= ancho
        self.marca= marca
    
    def mostrar_info(self):
        print(f"Color: {self.color}\nLongitud: {self.longitud}\nAncho: {self.ancho}\nMarca: {self.marca}")






