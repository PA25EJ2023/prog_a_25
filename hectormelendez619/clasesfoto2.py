class Ropa:
    def __init__(self,color,marca,precio,prenda):
        self.color = color
        self.marca = marca
        self.precio = precio
        self.prenda = prenda
    
    def inform(self):
        print(f'Color:{self.color}\nMarca:{self.marca}\nPrecio:{self.precio}\nPrenda:{self.prenda}\n')

class Cable:
    def __init__(self,color,tipoent,precio,medida):
        self.color = color
        self.tipoent = tipoent
        self.precio = precio
        self.medida = medida

    def inform(self):
        print(f'Color:{self.color}\nTipoent:{self.tipoent}\nPrecio:{self.precio}\nMedida:{self.medida}\n')

class Compu:
    def __init__(self,color,precio,marca,medida):
        self.color = color
        self.precio = precio
        self.marca = marca
        self.medida = medida

    def inform(self):
        print(f'Color:{self.color}\nPrecio:{self.precio}\nMarca:{self.marca}\nMedida:{self.medida}\n')

class Revista:
    def __init__(self,nombre,precio,color,tema):
        self.nombre = nombre
        self.precio = precio
        self.color = color
        self.tema = tema

    def inform(self):
        print(f'Nombre:{self.nombre}\nPrecio:{self.precio}\nColor:{self.color}\nTema:{self.tema}\n')

class Lentefto:
    def __init__(self,marca,precio,color,medida):
        self.marca = marca
        self.precio = precio
        self.color = color
        self.medida = medida

    def inform(self):
        print(f'Marca:{self.marca}\nPrecio:{self.precio}\nColor:{self.color}\nMedida:{self.medida}\n')

class Tapalen:
    def __init__(self,marca,precio,color,medida):
        self.marca = marca
        self.precio = precio
        self.color = color
        self.medida = medida

    def inform(self):
        print(f'Marca:{self.marca}\nPrecio:{self.precio}\nColor:{self.color}\nMedida:{self.medida}\n')

class Bateria:
    def __init__(self,capacidad,precio,color,medida):
        self.capacidad = capacidad
        self.precio = precio
        self.color = color
        self.medida = medida

    def inform(self):
        print(f'Capacidad:{self.capacidad}\nPrecio:{self.precio}\nColor:{self.color}\nMedida:{self.medida}\n')

class Telefono:
    def __init__(self,marca,precio,color,almacenamiento):
        self.marca = marca
        self.precio = precio
        self.color = color
        self.almacenamiento = almacenamiento

    def inform(self):
        print(f'Marca:{self.marca}\nPrecio:{self.precio}\nColor:{self.color}\nAlmacenamiento:{self.almacenamiento}\n')

class Estuche:
    def __init__(self,marca,precio,color,almacena):
        self.marca = marca
        self.precio = precio
        self.color = color
        self.almacena = almacena

    def inform(self):
        print(f'Marca:{self.marca}\nPrecio:{self.precio}\nColor:{self.color}\nAlmacena:{self.almacena}\n')

class Reloj:
    def __init__(self,marca,precio,color,tipo):
        self.marca = marca
        self.precio = precio
        self.color = color
        self.tipo = tipo

    def inform(self):
        print(f'Marca:{self.marca}\nPrecio:{self.precio}\nColor:{self.color}\nTipo:{self.tipo}\n')

class Lapiz:
    def __init__(self,marca,precio,color,tamaño):
        self.marca = marca
        self.precio = precio
        self.color = color
        self.tamaño = tamaño

    def inform(self):
        print(f'Marca:{self.marca}\nPrecio:{self.precio}\nColor:{self.color}\nTamaño:{self.tamaño}\n')

class Marcador:
    def __init__(self,marca,precio,color,tamaño):
        self.marca = marca
        self.precio = precio
        self.color = color
        self.tamaño = tamaño

    def inform(self):
        print(f'Marca:{self.marca}\nPrecio:{self.precio}\nColor:{self.color}\nTamaño:{self.tamaño}\n')

class Tripie:
    def __init__(self,marca,precio,color,tamaño):
        self.marca = marca
        self.precio = precio
        self.color = color
        self.tamaño = tamaño

    def inform(self):
        print(f'Marca:{self.marca}\nPrecio:{self.precio}\nColor:{self.color}\nTamaño:{self.tamaño}\n')

class Zapato:
    def __init__(self,marca,precio,color,talla):
        self.marca = marca
        self.precio = precio
        self.color = color
        self.talla = talla

    def inform(self):
        print(f'Marca:{self.marca}\nPrecio:{self.precio}\nColor:{self.color}\nTalla:{self.talla}\n')