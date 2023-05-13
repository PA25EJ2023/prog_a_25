class Computadora:
    def __init__(self,marca,tamaño,color,capacidad,precio):
        self.marca = marca
        self.tamaño = tamaño
        self.color = color 
        self.capacidad = capacidad 
        self.precio = precio 

    def info(self):
        print(f'marca: {self.marca}\n tamaño: {self.tamaño}\n color: {self.color}\n capacidad: {self.capacidad}\n precio: {self.precio}')

class Maletin:
    def __init__(self,color,marca,tamaño,precio):
        self.color = color 
        self.marca = marca 
        self.tamaño = tamaño 
        self.precio = precio 

    def info(self):
        print(f'color: {self.color}\n marca: {self.marca}\n tamaño: {self.tamaño}\n precio: {self.precio}')

class Lente_camara:
    def __init__(self,marca,color,zoom,precio):
        self.marca = marca 
        self:color = color
        self.zoom = zoom 
        self.precio = precio
    
    def info(self):
        print(f'marca: {self.marca}\n color: {self.color}\n zoom: {self.zoom}\n precio: {self.precio}')

class Revista: 
    def __init__(self,nombre,artistas_portada,precio,lugar):
        self.nombre = nombre
        self.artistas_portada = artistas_portada
        self.precio = precio
        self.lugar = lugar

    def info(self):
        print(f'nombre: {self.nombre}\n artista en la portada: {self.artistas_portada}\n precio: {self.precio}\n lugar que se vende: {self.lugar}')

class Zapatos:
     def __init__(self,color,marca,tamaño,precio):
        self.color = color 
        self.marca = marca 
        self.tamaño = tamaño 
        self.precio = precio

     def info(self):
        print(f'color: {self.color}\n marca: {self.marca}\n tamaño: {self.tamaño}\n precio: {self.precio}') 

class Cargador:
    def __init__(self,marca,color,largo,tipo_cargador,precio):
        self.marca = marca 
        self.color = color 
        self.largo = largo 
        self.tipo_cargador = tipo_cargador 
        self.precio = precio 

    def info(self):
        print(f'color: {self.color}\n marca: {self.marca}\n largo: {self.largo}\n tipo de cargador: {self.tipo_cargador}\n precio: {self.precio}')

class Reloj:
    def __init__(self,marca,color,tipo,precio):
        self.marca = marca 
        self.color = color 
        self.tipo = tipo 
        self.precio = precio 

    def info(self):
        print(f'color: {self.color}\n marca: {self.marca}\n tipo: {self.tipo}\n precio: {self.precio}')

class Pila_camara:
    def __init__(self,marca,color,tipo_camara,precio):
        self.marca = marca 
        self.color = color 
        self.tipo_camara = tipo_camara 
        self.precio = precio 
    
    def info(self):
        print(f'color: {self.color}\n marca: {self.marca}\n tipo de camara: {self.tipo_camara}\n precio: {self.precio}')

class Celular:
    def __init__(self,marca,color,camara,pantalla,precio):
        self.marca = marca 
        self.color = color 
        self.camara = camara 
        self.pantalla = pantalla 
        self.precio = precio 

    def info(self):
        print(f'color: {self.color}\n marca: {self.marca}\n camara: {self.camara}\n pantalla: {self.pantalla}\n precio: {self.precio}')

class Camisas:
    def __init__(self,marca,color,talla,material,precio):
        self.marca = marca 
        self.color = color 
        self.talla = talla 
        self.material = material 
        self.precio = precio 

    def info(self):
        print(f'color: {self.color}\n marca: {self.marca}\n talla: {self.talla}\n material: {self.material}\n precio: {self.precio}')

class Lapices:
    def __init__(self,marca,color,tamaño,precio):
        self.marca = marca 
        self.color = color 
        self.tamaño = tamaño 
        self.precio = precio 

    def info(self):
        print(f'color: {self.color}\n marca: {self.marca}\n tamaño: {self.tamaño}\n precio: {self.precio}')

class Marcador:
    def __init__(self,marca,color,tamaño,precio):
        self.marca = marca 
        self.color = color 
        self.tamaño = tamaño 
        self.precio = precio 

    def info(self):
        print(f'color: {self.color}\n marca: {self.marca}\n tamaño: {self.tamaño}\n precio: {self.precio}')

class Tripie:
    def __init__(self,marca,color,tamaño,precio):
        self.marca = marca 
        self.color = color 
        self.tamaño = tamaño 
        self.precio = precio 

    def info(self):
        print(f'color: {self.color}\n marca: {self.marca}\n tamaño: {self.tamaño}\n precio: {self.precio}')