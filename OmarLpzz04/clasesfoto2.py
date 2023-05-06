class Camisetas():
    def __init__(self,color,talla,tipo,):
        self.color = color
        self.talla = talla
        self.tipo = tipo
    def inf(self):
        print(f"Color>> {self.color}\nTalla>> {self.talla}\nTipo>> {self.tipo}")

class Maletin():
    def __init__(self,color,tamaño,material,):
        self.color = color
        self.tamaño = tamaño
        self.material = material 
    def inf(self):
        print(f"Color>> {self.color}\nTamaño>> {self.tamaño}\nMaterial>> {self.material}")

class Cargadores():
    def __init__(self,color,medida,tipo,marca):
        self.color = color 
        self.medida = medida 
        self.tipo = tipo 
        self.marca = marca 
    def inf(self):
        print(f"Color>> {self.color}\nMedida>> {self.medida}\nTipo>> {self.tipo}\nMarca>> {self.marca}")

class Lapices():
    def __init__(self,color,medida,marca):
        self.color = color 
        self.medida = medida 
        self.marca = marca 
    def inf(self):
        print(f"Color>> {self.color}\nMedida>> {self.medida}\nMarca>> {self.marca}")

class Celular():
    def __init__(self,color,marca,sistema,tipo_pantalla):
        self.color = color 
        self.marca = marca 
        self.sistema = sistema 
        self.tipo = tipo_pantalla
    def inf(self):
        print(f"Color>> {self.color}\nMarca>> {self.marca}\nSistema {self.sistema}\nTipo>> {self.tipo}")
        
class Zapatos():
    def __init__(self,talla,color,material,):
        self.talla = talla 
        self.color = color 
        self.material = material 
    def inf(self):
        print(f"Color>> {self.color}\nTalla>> {self.talla}\nDe que estan hechos>> {self.material}")

class Lentes():
    def __init__(self,tamaño,tipo,precio,marca):
        self.tamaño = tamaño 
        self.tipo = tipo
        self.precio = precio 
        self.marca = marca 
    def inf(self):
        print(f"Tamaño>> {self.tamaño}\nTipo de lente>> {self.tipo}\nPrecio>> {self.precio}\nMarca>> {self.marca}")

class Tripie():
    def __init__(self,medida,color,marca):
        self.medida = medida 
        self.color = color 
        self.marca = marca 
    def inf(self):
        print(f"Color>> {self.color}\nMedida>> {self.medida}\nMarca>> {self.marca}")

class Revista():
    def __init__(self,color,categoria,marca,precio):
        self.color = color
        self.categoria = categoria 
        self.marca = marca
        self.precio = precio 
    def inf(self):
        print(f"Color>> {self.color}\nCategoria>> {self.categoria}\nMarca>> {self.marca}\nPrecio>> {self.precio}")
        


        