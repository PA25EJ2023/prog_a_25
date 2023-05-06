class Maletin:
    def __init__(self,color,tamaño,material,marca):
        self.color = color
        self.tamaño = tamaño
        self.material = material
        self.marca = marca
    
    def info(self):
        print(f"1 MALETIN\nColor: {self.color}\nTamaño: {self.tamaño}\nPrecio: {self.material}\nMarca: {self.marca}")
        print("-"*25)


class Laptop:
    def __init__(self,color,tamaño,precio,marca):
        self.color = color
        self.tamaño = tamaño
        self.precio = precio
        self.marca = marca
    
    def info(self):
        print(f"1 LAPTOP\nColor: {self.color}\nTamaño: {self.tamaño}\nPrecio: {self.precio}\nMarca: {self.marca}")
        print("-"*25)


class Reloj:
    def __init__(self,color,tamaño,material,marca):
        self.color = color
        self.tamaño = tamaño
        self.material = material
        self.marca = marca
    
    def info(self):
        print(f"1 RELOJ\nColor: {self.color}\nTamaño: {self.tamaño}\nPrecio: {self.material}\nMarca: {self.marca}")
        print("-"*25)


class Celular:
    def __init__(self,color,tamaño,precio,marca):
        self.color = color
        self.tamaño = tamaño
        self.precio = precio
        self.marca = marca
    
    def info(self):
        print(f"1 CELULAR\nColor: {self.color}\nTamaño: {self.tamaño}\nPrecio: {self.precio}\nMarca: {self.marca}")
        print("-"*25)


class Camisa:
    def __init__(self,color,talla,material,marca):
        self.color = color
        self.talla = talla
        self.material = material
        self.marca = marca
    
    def info(self):
        print(f"1 CAMISA\nColor: {self.color}\nTamaño: {self.talla}\nPrecio: {self.material}\nMarca: {self.marca}")
        print("-"*25)


class Saco:
    def __init__(self,color,talla,material,marca):
        self.color = color
        self.talla = talla
        self.material = material
        self.marca = marca
    
    def info(self):
        print(f"1 SACO\nColor: {self.color}\nTamaño: {self.talla}\nPrecio: {self.material}\nMarca: {self.marca}")
        print("-"*25)


class Cargador_laptop:
    def __init__(self,color,longitud,material,marca):
        self.color = color
        self.longitud = longitud
        self.material = material
        self.marca = marca
    
    def info(self):
        print(f"1 CARGADOR DE LAPTOP\nColor: {self.color}\nTamaño: {self.longitud}\nPrecio: {self.material}\nMarca: {self.marca}")
        print("-"*25)


class Tripie_camara:
    def __init__(self,color,altura,material,precio):
        self.color = color
        self.altura = altura 
        self.material = material
        self.precio = precio

    def info(self):
        print(f"1 TRIPIE DE CAMARA\nColor: {self.color}\nAltura: {self.altura}\nMaterial: {self.material}\nPrecio: {self.precio}")
        print("-"*25)


class Revista:
    def __init__(self,color,categoria,marca,precio):
        self.color = color
        self.categoria = categoria
        self.marca = marca
        self.precio = precio
    
    def info(self):
        print(f"1 REVISTA\nColor: {self.color}\nCategoria: {self.categoria}\nMarca: {self.marca}\nPrecio: {self.precio}")
        print("-"*25)


class Estuche_camara:
    def __init__(self,color,material,tamaño,precio):
        self.color = color
        self.material = material
        self.tamaño = tamaño
        self.precio = precio

    def info(self):
        print(f"1 ESTUCHE DE CÁMARA\nColor: {self.color}\nMaterial: {self.material}\nTamaño: {self.tamaño}\nPrecio: {self.precio}")
        print("-"*25)


class Pluma_estilografica:
    def __init__(self,color,material,marca,precio):
        self.color = color
        self.material = material
        self.marca = marca
        self.precio = precio

    def info(self):
        print(f"1 PLUMA ESTILOGRAFICA\nColor: {self.color}\nMaterial: {self.material}\nMarca: {self.marca}\nPrecio: {self.precio}")
        print("-"*25)

class Lapiz:
    def __init__(self,tipo,color,marca,precio):
        self.tipo = tipo
        self.color = color
        self.marca = marca
        self.precio = precio

    def info(self):
        print(f"1 LAPIZ\nTipo: {self.tipo}\nColor: {self.color}\nMarca: {self.marca}\nPrecio: {self.precio}")
        print("-"*25)


class Pila_camara:
    def __init__(self,amperaje,marca,color,precio):
        self.amperaje = amperaje
        self.marca = marca
        self.color = color
        self.precio = precio

    def info(self):
        print(f"1 PILA DE CAMARA\nColor: {self.color}\nMarca: {self.marca}\nColor: {self.color}\nPrecio: {self.precio}")
        print("-"*25)

class Lente_camara:
    def __init__(self,tipo,marca,color,precio):
        self.tipo = tipo
        self.marca = marca
        self.color = color
        self.precio = precio

    def info(self):
        print(f"1 LENTE DE CAMARA\nTipo: {self.tipo}\nMarca: {self.marca}\nColor: {self.color}\nPrecio: {self.precio}")
        print("-"*25)

class Tapa_lente_camara:
    def __init__(self,tipo,marca,color,precio):
        self.tipo = tipo
        self.marca = marca
        self.color = color
        self.precio = precio

    def info(self):
        print(f"1 TAPA DE LENTE DE CAMARA\nTipo: {self.tipo}\nMarca: {self.marca}\nColor: {self.color}\nPrecio: {self.precio}")
        print("-"*25)


class Bateria_portatil:
    def __init__(self,amperaje,color,marca,precio):
        self.amperaje = amperaje
        self.color = color
        self.marca = marca
        self.precio = precio

    def info(self):
        print(f"1 BATERIA PORTATIL\nAmperaje: {self.amperaje}\nColor: {self.color}\nMarca: {self.marca}\nPrecio: {self.precio}")
        print("-"*25)


class Zapato_derecho:
    def __init__(self,color,material,talla,tipo):
        self.color = color
        self.material = material
        self.talla = talla
        self.tipo = tipo

    def info(self):
        print(f"1 ZAPATO DERECHO\nColor: {self.color}\nMaterial: {self.material}\nTalla: {self.talla}\nTipo: {self.tipo}")
        print("-"*25)

class Zapato_izquierdo:
    def __init__(self,color,material,talla,tipo):
        self.color = color
        self.material = material
        self.talla = talla
        self.tipo = tipo

    def info(self):
        print(f"1 ZAPATO IZQUIERDO\nColor: {self.color}\nMaterial: {self.material}\nTalla: {self.talla}\nTipo: {self.tipo}")
        print("-"*25)