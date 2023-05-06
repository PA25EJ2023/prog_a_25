#clases foto 2 
class Camisa:
    def __init__(self,color,talla,marca,seccion_ropa,precio):
        self.color=color
        self.talla=talla
        self.marca=marca
        self.seccion_ropa=seccion_ropa
        self.precio=precio

    def info(self):
        print(f"Color de la camisa: {self.color}")
        print(f"Talla: {self.talla}")
        print(f"Marca: {self.marca}")
        print(f"Sección/área ropa: {self.seccion_ropa}")
        print(f"$ {self.precio}")

class Sueter_mezclilla:
    def __init__(self,color,talla,marca,precio):
        self.color=color
        self.talla=talla
        self.marca=marca
        self.precio=precio
        
    def info(self):
        print(f"Color de la mezclilla: {self.color}")
        print(f"Talla: {self.talla}")
        print(f"Marca: {self.marca}")
        print(f"$ {self.precio}")
    
class Celular:
    def __init__(self,marca,color,num_tel,modelo,precio,capacidad):
        self.marca=marca
        self.color=color
        self.num_tel=num_tel
        self.modelo=modelo
        self.capacidad=capacidad
        self.precio=precio
       
    def info(self):
        print(f"Marca del celular: {self.marca}")
        print(f"Color: {self.color}")
        print(f"Número de teléfono: {self.num_tel}")
        print(f"Modelo: {self.modelo}")
        print(f"Capacidad de almacenamiento: {self.capacidad}")
        print(f"$ {self.precio}")

class Bolso:
    def __init__(self,color,material,marca,precio):
        self.color=color
        self.material=material
        self.marca=marca
        self.precio=precio

    def info(self):
        print(f"Color del bolso: {self.color}")
        print(f"Material: {self.material}")
        print(f"Marca: {self.marca}")
        print(f"$ {self.precio}")

class Laptop:
    def __init__(self,marca,color,modelo,precio):
        self.marca=marca
        self.color=color
        self.modelo=modelo
        self.precio=precio
        
    def info(self):
        print(f"Marca de la laptop: {self.marca}")
        print(f"Color: {self.color}")
        print(f"Modelo: {self.modelo}")
        print(f"$ {self.precio}")

class Libro:
    def __init__(self,titulo,autor,fecha_lanzamiento,precio):
        self.titulo=titulo
        self.autor=autor
        self.fecha_lanzamiento=fecha_lanzamiento
        self.precio=precio

    def info(self):
        print(f"Titulo del libro: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Fecha de lanzamiento: {self.fecha_lanzamiento}")
        print(f"$ {self.precio}")

class Reloj:
    def __init__(self,color,marca,tipo,precio):
        self.color=color
        self.marca=marca
        self.tipo=tipo
        self.precio=precio
    
    def info(self):
        print(f"Color del reloj: {self.color}")
        print(f"Marca: {self.marca}")
        print(f"Tipo (analógico/digital/bolsillo): {self.tipo}")
        print(f"$ {self.precio}")

