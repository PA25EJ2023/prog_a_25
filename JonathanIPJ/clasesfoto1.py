class Pluma:
    def __init__(self, color, precio, tamano, marca):
        self.color = color
        self.precio = precio 
        self.tamano = tamano
        self.marca = marca 
    
    def imprimir(self):
        print(f"Pluma- Color: {self.color}, Precio: {self.precio}, Tamano: {self.tamano}, Marca: {self.marca}")


class Tijera:
    def __init__(self, color, tamano, precio, marca):
        self.color = color
        self.tamano = tamano
        self.precio = precio
        self.marca = marca 

    def imprimir(self):
        print(f"Tijeras- Color: {self.color}, Tamano: {self.tamano}, Precio: {self.precio}, Marca: {self.marca}") 


class Libreta:
    def __init__(self, color, num_hojas, marca, precio):
        self.color = color
        self.num_hojas = num_hojas
        self.marca = marca
        self.precio = precio

    def imprimir(self):
        print(f"Libreta- Color: {self.color}, Numero de Hojas: {self.num_hojas}, Marca: {self.marca}, Precio: {self.precio}")


class Espejo:
    def __init__(self,forma,color,precio):
        self.forma = forma 
        self.color = color 
        self.precio = precio 

    def imprimir(self):
        print(f"Espejo- Forma: {self.forma}, Color: {self.color}, Precio: {self.precio}")

class Pegamento:
    def __init__(self,tipo,marca,precio,tamano):
        self.tipo = tipo
        self.marca = marca 
        self.precio = precio 
        self.tamano = tamano 

    def imprimir(self):
        print(f"Pegamento- Tipo: {self.tipo}, Marca: {self.marca}, Precio: {self.precio}, Tamano:{self.tamano}")


class Marco:
    def __init__(self, tamano, color, forma, imagen):
        self.tamano = tamano 
        self.color = color 
        self.forma = forma 
        self.imagen = imagen

    def imprimir(self):
        print(f"Marco Para Fotos- Tamano: {self.tamano}, Color: {self.color}, Forma: {self.forma}, Imagen: {self.imagen}") 


class Esmalte:
    def __init__(self, color, marca, precio):
        self.color = color 
        self.marca = marca 
        self.precio = precio

    def imprimir(self):
        print(f"Esmalte- Color: {self.color} Marca: {self.marca} Precio: {self.precio}")


class Labial:
    def __init__(self, color, marca, precio):
        self.color = color 
        self.marca = marca 
        self.precio = precio

    def imprimir(self):
        print(f"Labial- Color: {self.color} Marca: {self.marca} Precio: {self.precio}")

class Cuenta:
    def __init__(self, cantidad, color, forma):
        self.cantidad = cantidad 
        self.color = color 
        self.forma = forma 

    def imprimir(self):
        print(f"Cuentas para pulseras- Cantidad: {self.cantidad} Color: {self.color} forma: {self.forma}")


class Marcador:
    def __init__(self, color, marca, precio):
        self.color = color 
        self.marca = marca 
        self.precio = precio 

    def imprimir(self):
        print(f"Marcadores- Color: {self.color}, Marca: {self.marca}, Precio: {self.precio}")

class Cinta:
    def __init__(self, color, longitud, precio):
        self.color = color 
        self.longitud = longitud 
        self.precio = precio

    def imprimir(self):
        print(f"Cintas- Color: {self.color}, Longitud: {self.longitud}, Precio: {self.precio}")

