class Boligrafo():
    def __init__(self,color,marca,tamaño,precio):
        self.color = color
        self.marca = marca
        self.tamaño = tamaño
        self.precio = precio
    def inf(self):
        print(f"Color de tinta>> {self.color}\nMarca de pluma>> {self.marca}\nTamaño de pluma>> {self.tamaño}\n¿Cuanto costo?>> {self.precio}")

class Cuaderno():
    def __init__(self,color,marca,tamaño,tipo):
        self.color = color
        self.marca = marca
        self.tamaño = tamaño 
        self.tipo = tipo
    
    def inf(self):
        print(f"Color>> {self.color}\nMarca>> {self.marca}\nTamaño>> {self.tamaño}\nTipo de libreta>> {self.tipo}")

class Plumones():
    def __init__(self,color,marca,tamaño,precio):
        self.color = color 
        self.marca = marca  
        self.tamaño = tamaño
        self.precio = precio

    def inf(self):
        print(f"Color>> {self.color}\nMarca>> {self.marca}\nTamaño>> {self.tamaño}\nPrecio>> {self.precio}")

class Tijeras():
    def __init__(self,color,marca,tamaño,precio):
        self.color = color 
        self.marca = marca  
        self.tamaño = tamaño
        self.precio = precio
    def inf(self):
        print(f"Color>> {self.color}\nMarca>> {self.marca}\nTamaño>> {self.tamaño}\nPrecio>> {self.precio}")


class Esmalte():
    def __init__(self,color,marca,tamaño,forma):
        self.color = color 
        self.marca = marca  
        self.tamaño = tamaño
        self.forma = forma
    def inf(self):
        print(f"Color>> {self.color}\nMarca>> {self.marca}\nTamaño>> {self.tamaño}\nForma>> {self.forma}")

class Regla():
    def __init__(self,color,medida,forma,marca):
        self.color = color
        self.medida = medida 
        self.forma = forma 
        self.marca = marca 
    def inf(self):
        print(f"Color>> {self.color}\nMedida>> {self.medida}\nForma>> {self.forma}\nMarca>> {self.marca}")

class Resistol():
    def __init__(self,color,tamaño,marca,forma):
        self.color = color 
        self.tamaño = tamaño 
        self.marca = marca 
        self.forma = forma 
    def inf(self):
        print(f"Color>> {self.color}\nTamaño>> {self.tamaño}\nMarca>> {self.marca}\nForma>> {self.forma}")

class Fotos():
    def __init__(self,tamaño,calidad,forma_marco,decoracion):
        self.tamaño = tamaño
        self.calidad = calidad
        self.forma_marco = forma_marco
        self.decoracion = decoracion
    def inf(self):
        print(f"Tamaño>> {self.tamaño}\nCalidad>> {self.calidad}\nForma de la foto>> {self.forma_marco}\nDecoracion>> {self.decoracion}")

class Labiales():
    def __init__(self,color,tamaño,forma,marca):
        self.color = color
        self.tamaño = tamaño 
        self.forma = forma 
        self.marca = marca 
    def inf(self):
        print(f"Color>> {self.color}\nTamaño>> {self.tamaño}\nForma>> {self.forma}\nMarca>> {self.marca}")

class Cintas():
    def __init__(self,color,marca,longitud,ancho):
        self.color = color
        self.marca = marca 
        self.longitud = longitud 
        self.ancho = ancho 
    def inf(self):
        print(f"Color>> {self.color}\nMarca>> {self.marca}\nLongitud>> {self.longitud}\nAncho>> {self.ancho}")
        
class Broches():
    def __init__(self,color,tamaño,figura,marca):
        self.color = color
        self.tamaño = tamaño
        self.figura = figura 
        self.marca = marca
    def inf(self):
        print(f"Color>> {self.color}\nTamaño>> {self.tamaño}\nForma>> {self.figura}\nMarca>> {self.marca}")

class Espejo():
    def __init__(self,tamaño,color,forma,precio):
        self.tamaño = tamaño 
        self.color = color
        self.forma = forma 
        self.precio = precio 
    def inf(self):
        print(f"Color>> {self.color}\nTamaño>> {self.tamaño}\nForma>> {self.forma}\nPrecio>> {self.precio}")

class Telefono():
    def __init__(self,color,tamaño,precio,marca):
        self.color = color
        self.tamaño = tamaño
        self.precio = precio 
        self.marca = marca 
    def inf(self):
        print(f"Color>> {self.color}\nTamaño>> {self.tamaño}\nPrecio>> {self.precio}\nMarca>> {self.marca}")

class Cuentas():
    def __init__(self,color,cantidad,material,tamaño):
        self.color = color
        self.cantidad = cantidad
        self.material = material
        self.tamaño = tamaño

    def info(self):
        print(f"Color: {self.color}\nCantidad: {self.cantidad}\nMaterial: {self.material}\nTamaño: {self.tamaño}")


class Stickers():
    def __init__(self,estado,cantidad,forma,material):
        self.estado = estado
        self.cantidad = cantidad
        self.forma = forma
        self.material = material

    def info(self):
        print(f"Estado: {self.estado}\nCantidad: {self.cantidad}\nForma: {self.forma}\nMaterial: {self.material}")