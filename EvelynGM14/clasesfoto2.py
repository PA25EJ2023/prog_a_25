class Maletin:
    def __init__(self,color,tamaño,material,marca):
        self.color = color
        self.tamaño = tamaño
        self.material = material
        self.marca = marca
    
    def info(self):
        print(f"1 MALETIN\nColor: {self.color}\nTamaño: {self.tamaño}\nPrecio: {self.material}\nMarca: {self.marca}")


class Laptop:
    def __init__(self,color,tamaño,precio,marca):
        self.color = color
        self.tamaño = tamaño
        self.precio = precio
        self.marca = marca
    
    def info(self):
        print(f"1 LAPTOP\nColor: {self.color}\nTamaño: {self.tamaño}\nPrecio: {self.precio}\nMarca: {self.marca}")


class Reloj:
    def __init__(self,color,tamaño,material,marca):
        self.color = color
        self.tamaño = tamaño
        self.material = material
        self.marca = marca
    
    def info(self):
        print(f"1 RELOJ\nColor: {self.color}\nTamaño: {self.tamaño}\nPrecio: {self.material}\nMarca: {self.marca}")


class Celular:
    def __init__(self,color,tamaño,precio,marca):
        self.color = color
        self.tamaño = tamaño
        self.precio = precio
        self.marca = marca
    
    def info(self):
        print(f"1 CELULAR\nColor: {self.color}\nTamaño: {self.tamaño}\nPrecio: {self.precio}\nMarca: {self.marca}")


class Camisa:
    def __init__(self,color,talla,material,marca):
        self.color = color
        self.talla = talla
        self.material = material
        self.marca = marca
    
    def info(self):
        print(f"1 CAMISA\nColor: {self.color}\nTamaño: {self.talla}\nPrecio: {self.material}\nMarca: {self.marca}")


class Saco:
    def __init__(self,color,talla,material,marca):
        self.color = color
        self.talla = talla
        self.material = material
        self.marca = marca
    
    def info(self):
        print(f"1 SACO\nColor: {self.color}\nTamaño: {self.talla}\nPrecio: {self.material}\nMarca: {self.marca}")


class Cargador_laptop:
    def __init__(self,color,longitud,material,marca):
        self.color = color
        self.longitud = longitud
        self.material = material
        self.marca = marca
    
    def info(self):
        print(f"1 CARGADOR DE LAPTOP\nColor: {self.color}\nTamaño: {self.longitud}\nPrecio: {self.material}\nMarca: {self.marca}")


class Tripie_camara:
    def __init__(self,color,altura,material,precio):
        self.color = color
        self.altura = altura 
        self.material = material
        self.precio = precio

    def info(self):
        print(f"1 TRIPIE DE CAMARA\nColor: {self.color}\nAltura: {self.altura}\nMaterial: {self.material}\nPrecio: {self.precio}")


class Revista:
    def __init__(self,color,categoria,marca,precio):
        self.color = color
        self.categoria = categoria
        self.marca = marca
        self.precio = precio
    
    def info(self):
        print(f"1 REVISTA\nColor: {self.color}\nCategoria: {self.categoria}\nMarca: {self.marca}\nPrecio: {self.precio}")