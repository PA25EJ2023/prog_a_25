class Pluma:
    def __init__(self, color, precio, tamano, marca):
        self.color = color
        self.precio = precio 
        self.tamano = tamano
        self.marca = marca 
    
    def imprimir(self):
        print(f"Pluma- Color: {self.color}, Precio: {self.precio}, Tamaño: {self.tamano}, Marca: {self.marca}")


class Tijera:
    def __init__(self, color, tamano, precio, marca):
        self.color = color
        self.tamano = tamano
        self.precio = precio
        self.marca = marca 

    def imprimir(self):
        print(f"Tijeras- Color: {self.color}, Tamaño: {self.tamano}, Precio: {self.precio}, Marca: {self.marca}") 


class Libreta:
    def __init__(self, color, num_hojas, marca, precio):
        self.color = color
        self.num_hojas = num_hojas
        self.marca = marca
        self.precio = precio

    def imprimir(self):
        print(f"Libreta- Color: {self.color}, Numero de Hojas: {self.num_hojas}, Marca: {self.marca}, Precio: {self.precio}")


class Espejo:
    def __init__(self, forma, color, precio, tamano):
        self.forma = forma 
        self.color = color 
        self.precio = precio 
        self.tamano = tamano

    def imprimir(self):
        print(f"Espejo- Forma: {self.forma}, Color: {self.color}, Precio: {self.precio}, Tamaño: {self.tamano}")

class Pegamento:
    def __init__(self,tipo,marca,precio,tamano):
        self.tipo = tipo
        self.marca = marca 
        self.precio = precio 
        self.tamano = tamano 

    def imprimir(self):
        print(f"Pegamento- Tipo: {self.tipo}, Marca: {self.marca}, Precio: {self.precio}, Tamaño:{self.tamano}")


class Marco:
    def __init__(self, tamano, color, forma, imagen):
        self.tamano = tamano 
        self.color = color 
        self.forma = forma 
        self.imagen = imagen

    def imprimir(self):
        print(f"Marco Para Fotos- Tamaño: {self.tamano}, Color: {self.color}, Forma: {self.forma}, Imagen: {self.imagen}") 


class Esmalte:
    def __init__(self, color, marca, precio, tamano):
        self.color = color 
        self.marca = marca 
        self.precio = precio
        self.tamano = tamano 

    def imprimir(self):
        print(f"Esmalte- Color: {self.color} Marca: {self.marca} Precio: {self.precio}, Tamaño: {self.tamano}")


class Labial:
    def __init__(self, color, marca, precio, tamano):
        self.color = color 
        self.marca = marca 
        self.precio = precio
        self.tamano = tamano

    def imprimir(self):
        print(f"Labial- Color: {self.color}, Marca: {self.marca}, Precio: {self.precio}, Tamaño: {self.tamano}")

class Cuenta:
    def __init__(self, cantidad, color, forma, tamano):
        self.cantidad = cantidad 
        self.color = color 
        self.forma = forma 
        self.tamano = tamano

    def imprimir(self):
        print(f"Cuentas para pulseras- Cantidad: {self.cantidad} Color: {self.color} forma: {self.forma}, Tamaño: {self.tamano}")


class Marcador:
    def __init__(self, color, marca, precio, tipo):
        self.color = color 
        self.marca = marca 
        self.precio = precio 
        self.tipo = tipo

    def imprimir(self):
        print(f"Marcadores- Color: {self.color}, Marca: {self.marca}, Precio: {self.precio}, Tipo: {self.tipo}")

class Cinta:
    def __init__(self, color, longitud, precio, marca):
        self.color = color 
        self.longitud = longitud 
        self.precio = precio
        self.marca = marca 

    def imprimir(self):
        print(f"Cintas- Color: {self.color}, Longitud: {self.longitud}, Precio: {self.precio}, Marca: {self.marca}")

class Telefono:
    def __init__(self, color, tipo, precio, color_numero):
        self.color = color 
        self.tipo = tipo 
        self.precio = precio 
        self.color_numero = color_numero

    def imprimir(self):
        print(f"Telefono- Color: {self.color}, Tipo: {self.tipo}, Precio: {self.precio}, Color de Numeros: {self.color_numero}")


class Sticker:
    def __init__(self, forma, color, cantidad, precio):
        self.forma = forma
        self.color = color 
        self.cantidad = cantidad 
        self.precio = precio 

    def imprimir(self):
        print(f"Stickers- Forma: {self.forma}, Color: {self.color}, Cantidad: {self.cantidad}, Precio {self.precio}")


class Pinzas:
    def __init__(self, color, forma, precio, tamano):
        self.color = color 
        self.forma = forma 
        self.precio = precio 
        self.tamano = tamano 

    def imprimir(self):
        print(f"Pinzas para el pelo- Color: {self.color}, Forma: {self.forma}, Precio: {self.precio}, Tamaño: {self.tamano}")


class Imagen:
    def __init__(self, tamano, contenido, material, forma):
        self.tamano = tamano 
        self.contenido = contenido 
        self.material = material 
        self.forma = forma 

    def imprimir(self):
        print(f"Imagen- Tamano: {self.tamano}, Contenido: {self.contenido}, Material: {self.material}, Forma: {self.forma}")


class Brillantina:
    def __init__(self, color, lug_donde_guarda, division_de_caja, precio):
        self.color = color 
        self.lug_donde_guarda = lug_donde_guarda
        self.division_de_caja = division_de_caja
        self.precio = precio 

    def imprimir(self):
        print(f"Brillantina- Color: {self.color}, Lugar donde se Guarda: {self.lug_donde_guarda}, Forma de la Caja: {self.division_de_caja}, Precio: {self.precio}")


class Libro:
    def __init__(self, color, num_pagina, titulo, precio):
        self.color = color
        self.num_pagina = num_pagina
        self.titulo = titulo 
        self.precio = precio 

    def imprimir(self):
        print(f"Color: {self.color}, Numero de Paginas: {self.num_pagina}, Titulo: {self.titulo}, Precio: {self.precio}")
