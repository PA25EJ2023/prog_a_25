class Camisa:
    def __init__(self, color, marca, precio, material):
        self.color = color 
        self.marca = marca 
        self.precio = precio 
        self.material = material

    def imprimir(self):
        print(f"Camisas- Color:{self.color}, Marca:{self.marca}, Precio:{self.precio}, Material:{self.material}")


class Laptop:
    def __init__(self, marca, precio, color, modelo):
        self.marca = marca
        self.precio = precio 
        self.color = color 
        self. modelo = modelo 

    def imprimir(self):
        print(f"Laptop- Marca:{self.marca}, Precio:{self.precio}, Color:{self.color}, Modelo:{self.modelo}")


class Reloj:
    def __init__(self, marca, color, tipo, precio):
        self.marca = marca 
        self.color = color 
        self.tipo = tipo 
        self.precio = precio

    def imprimir(self):
        print(f"Reloj- Marca:{self.marca}, Color{self.color}, Tipo:{self.tipo}, Precio:{self.precio}")


class Lente:
    def __init__(self, color, marca, capacidad, precio):
        self.color = color 
        self.marca = marca 
        self.capacidad = capacidad
        self.precio = precio 

    def imprimir(self):
        print(f"Lente de Camara- Color:{self.color}, Marca:{self.marca}, Capacidad:{self.capacidad}, Precio:{self.precio}")


class Revista:
    def __init__(self, precio, titulo, num_pagina, edicion):
        self.precio = precio 
        self.titulo = titulo 
        self.num_pagina = num_pagina
        self.edicion = edicion 

    def imprimir(self):
        print(f"Revista - Precio:{self.precio}, Titulo:{self.titulo}, Numero de Paginas:{self.num_pagina}, Edicion:{self.edicion}")


class Maletin:
    def __init__(self, color, marca, precio, medida):
        self.color = color 
        self.marca = marca 
        self.precio = precio 
        self.medida = medida 

    def imprimir(self):
        print(f"Maletin- Color:{self.color}, Marca:{self.marca}, Precio:{self.precio}, Medida:{self.medida}")


class Cargador:
    def __init__(self, color, marca, precio, tipo_camara):
        self.color = color 
        self.marca = marca 
        self.precio = precio 
        self.tipo_camara = tipo_camara

    def imprimir(self):
        print(f"Cargador de camara: Color:{self.color}, Marca:{self.marca}, Precio:{self.precio}, Cargador para camara:{self.tipo_camara}")


class Microfono:
    def __init__(self, marca, precio, prdoucto_compatible, tamano):
        self.marca = marca 
        self.precio = precio 
        self.producto_compatible = prdoucto_compatible
        self.tamano = tamano 

    def imprimir(self):
        print(f"Microfono- Marca:{self.marca}, Precio:{self.precio}, Producto:{self.producto_compatible}, Longitud:{self.tamano}")


class Pluma:
    def __init__(self, marca, precio, color, tamano):
        self.marca = marca 
        self.precio = precio 
        self.color = color 
        self.tamano = tamano 

    def imprimir(self):
        print(f"Pluma- Marca:{self.marca}, Precio:{self.precio}, Color:{self.color}, Tamaño:{self.tamano}")


class Lapiz:
    def __init__(self, marca, precio, tamano, color):
        self.marca = marca 
        self.precio = precio 
        self.tamano = tamano 
        self.color = color 

    def imprimir(self):
        print(f"Lapiz- Marca:{self.marca}, Precio:{self.precio}, Tamaño:{self.tamano}, Color:{self.color}")


class Zapato:
    def __init__(self, marca, precio, color, talla):
        self.marca = marca 
        self.precio = precio 
        self.color = color 
        self.talla = talla 

    def imprimir(self):
        print(f"Zapatos- Marca:{self.marca}, Precio:{self.precio}, Color:{self.color}, Talla:{self.talla}")


class Telefono:
    def __init__(self, marca, precio, color, modelo):
        self.marca = marca 
        self.precio = precio 
        self.color = color 
        self.modelo = modelo 

    def imprimir(self):
        print(f"Telefono- Marca:{self.marca}, Precio:{self.precio}, Color:{self.color}, Modelo:{self.modelo}")


class Inalambrico:
    def __init__(self, marca, tipo, precio, tipo_entrada):
        self.marca = marca 
        self.tipo = tipo 
        self.precio = precio 
        self.tipo_entrada = tipo_entrada

    def imprimir(self):
        print(f"Cargador de Telefono- Marca:{self.marca}, Tipo de cargador:{self.tipo}, Precio:{self.precio}, Tipo de entrada:{self.tipo_entrada}")


class Tripode:
    def __init__(self, color, tamano, marca, precio):
        self.color = color 
        self.tamano = tamano 
        self.marca = marca 
        self.precio = precio

    def imprimir(self):
        print(f"Tripode- Color:{self.color}, Tamaño:{self.tamano}, Marca:{self.marca}, Precio:{self.precio}")


class Cable:
    def __init__(self, color, marca, precio, num_camaras):
        self.color = color 
        self.marca = marca 
        self.precio = precio 
        self.num_camaras = num_camaras

    def imprimir(self):
        print(f"Cable de alimentacion- Color:{self.color}, Marca:{self.marca}, Precio:{self.precio}, Numero de camaras que se pueden conectar:{self.num_camaras}") 