class Boligrafo:
    def __init__(self,color,tamaño,marca,precio):
        self.color= color
        self.tamaño= tamaño
        self.marca= marca
        self.precio= precio 

    def mostrar_info(self):
        print(f"Color: {self.color}\nTamaño: {self.tamaño}\nMarca: {self.marca} \nPrecio: {self.precio}")

class Marcador:
    def __init__(self,color,tamaño,marca,precio):
        self.color= color
        self.tamaño= tamaño
        self.marca= marca
        self.precio= precio 

    def mostrar_info(self):
        print(f"Color: {self.color}\nTamaño: {self.tamaño}\nMarca: {self.marca}\nPrecio: {self.precio}")
    
class Cinta:
    def __init__(self,color,longitud,ancho,marca):
        self.color= color
        self.longitud= longitud
        self.ancho= ancho
        self.marca= marca
    
    def mostrar_info(self):
        print(f"Color: {self.color}\nLongitud: {self.longitud}\nAncho: {self.ancho}\nMarca: {self.marca}")

class Libreta:
    def __init__(self,color,tamaño,num_hojas,tipo):
        self.color= color
        self.tamaño= tamaño
        self.num_hojas= num_hojas
        self.tipo= tipo
    
    def mostrar_info(self):
        print(f"Color: {self.color}\nTamaño: {self.tamaño}\nNúmero de Hojas: {self.num_hojas}\nTipo: {self.tipo}")

class Esmalte_Uñas:
    def __init__(self,color,contenido,forma,marca):
        self.color= color
        self.contenido= contenido
        self.forma= forma
        self.marca= marca
    
    def mostrar_info(self):
        print(f"Color: {self.color}\nContenido Neto: {self.contenido}\nForma: {self.forma}\nMarca: {self.marca}")

class Brillo_labial:
    def __init__(self,color,contenido,forma,marca):
        self.color= color
        self.contenido= contenido
        self.forma= forma
        self.marca= marca
    
    def mostrar_info(self):
        print(f"Color: {self.color}\nContenido Neto: {self.contenido}\nForma: {self.forma}\nMarca: {self.marca}")





