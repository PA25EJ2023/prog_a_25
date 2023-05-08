class Bolso:
    def __init__(self,color,tamaño,material):
        pass

class Laptop:
    def __init__(self,color,tamaño,tamaño_pantalla,marca):
        self.color= color
        self.tamaño= tamaño
        self.tamaño_pantalla= tamaño_pantalla
        self.marca= marca
    
    def mostrar_info(self):
        print(f"Color: {self.color}\nTamaño: {self.tamaño}\nTamaño Pantalla: {self.tamaño_pantalla}\nMarca: {self.marca}")

class Reloj_Muñeca:
    def __init__(self,color,tamaño,diametro_dial,material):
        self.color= color
        self.tamaño= tamaño
        self.diametro_dial= diametro_dial
        self.material= material
    
    def mostrar_info(self):
        print(f"Color: {self.color}\nTamaño del Producto: {self.tamaño}\nDiametro del Dial: {self.diametro_dial}\nMaterial: {self.material}")

class Tripode_Camara:
    def __init__(self,color,altura_max,altura_min,longitud_plegada,material):
        self.color= color
        self.altura_max= altura_max
        self.altura_min= altura_min
        self.longitud_plegada= longitud_plegada
        self.material= material

    def mostrar_info(self):
        print(f"Color: {self.color}\nAltura Máx: {self.altura_max}\nAltura Min: {self.altura_min}\nLongitud Plegada: {self.longitud_plegada}\nMaterial {self.material}")

class Par_Zapatos:
    def __init__(self,color,talla,material,forma_punta,tipo_ajuste):
        self.color= color
        self.talla= talla
        self.material= material
        self.forma_punta= forma_punta
        self.tipo_ajuste= tipo_ajuste
    
    def mostrar_info(self):
        print(f"Color: {self.color}\nTalla: {self.talla}\nMaterial: {self.material}\nForma Punta: {self.forma_punta}\nTipo de Ajuste: {self.tipo_ajuste}")

class Lapiz:
    def __init__(self,color,tamaño,forma,marca):
        self.color= color
        self.tamaño= tamaño
        self.forma= forma 
        self.marca= marca
    
    def mostrar_info(self):
        print(f"Color: {self.color}\nTamaño: {self.tamaño}\nForma: {self.forma}\nMarca: {self.marca}")

class Boligrafo:
    def __init__(self,color,tamaño,tamaño_punta,marca):
        self.color= color
        self.tamaño= tamaño
        self.tamaño_punta= tamaño_punta
        self.marca= marca
    
    def mostrar_info(self):
        print(f"Color: {self.color}\nTamaño: {self.tamaño}\nTamaño de Punta: {self.tamaño_punta}\nMarca: {self.marca}")

class Funda_Camara:
    def __init__(self,color,tamaño,material,marca):
        self.color= color
        self.tamaño= tamaño
        self.material= material
        self.marca= marca
    
    def mostrar_info(self):
        print(f"Color: {self.color}\nTamaño: {self.tamaño}\nMaterial: {self.material}\nMarca: {self.marca}")

class Cargador:
    def __init__(self,color,tamaño,cantidad_w,marca):
        self.color= color
        self.tamaño= tamaño
        self.cantidad_w= cantidad_w
        self.marca= marca
    
    def mostrar_info(self):
        print(f"Color: {self.color}\nTamaño: {self.tamaño}\nCantidad Watts: {self.cantidad_w}\nMarca: {self.marca}")

class Disparador_Flash:
    def __init__(self,color,tamaño,alcance_sincronizacion,marca):
        self.color= color
        self.tamaño= tamaño
        self.alcance_sincronizacion= alcance_sincronizacion
        self.marca= marca
    
    def mostrar_info(self):
        print(f"Color: {self.color}\nTamaño: {self.tamaño}\nAlcance de Sincronización: {self.alcance_sincronizacion}\nMarca: {self.marca}")





