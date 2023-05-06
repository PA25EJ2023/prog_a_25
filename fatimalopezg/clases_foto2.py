#clases foto 2 
class Camisa:
    def __init__(self,color,talla,marca,seccion_ropa,precio):
        self.color=color
        self.talla=talla
        self.marca=marca
        self.seccion_ropa=seccion_ropa
        self.precio=precio

    def info(self):
        print("--- CAMISA ---")
        print(f"Color: {self.color}")
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
        print("--- SUETER DE MEZCLILLA ---")
        print(f"Color: {self.color}")
        print(f"Talla: {self.talla}")
        print(f"Marca: {self.marca}")
        print(f"$ {self.precio}")
    
class Celular:
    def __init__(self,marca,color,num_tel,modelo,capacidad,precio):
        self.marca=marca
        self.color=color
        self.num_tel=num_tel
        self.modelo=modelo
        self.capacidad=capacidad
        self.precio=precio
       
    def info(self):
        print("--- CELULAR ---")
        print(f"Marca: {self.marca}")
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
        print("--- BOLSO/MALETIN ---")
        print(f"Color: {self.color}")
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
        print("--- LAPTOP ---")
        print(f"Marca: {self.marca}")
        print(f"Color: {self.color}")
        print(f"Modelo: {self.modelo}")
        print(f"$ {self.precio}")

class Revista:
    def __init__(self,titulo,banda,fecha_lanzamiento,precio):
        self.titulo=titulo
        self.banda=banda
        self.fecha_lanzamiento=fecha_lanzamiento
        self.precio=precio

    def info(self):
        print("--- REVISTA ---")
        print(f"Nombre: {self.titulo}")
        print(f"Banda musical: {self.banda}")
        print(f"Fecha de lanzamiento: {self.fecha_lanzamiento}")
        print(f"$ {self.precio}")

class Reloj:
    def __init__(self,color,marca,tipo,precio):
        self.color=color
        self.marca=marca
        self.tipo=tipo
        self.precio=precio
    
    def info(self):
        print("--- RELOJ DE CABALLERO ---")
        print(f"Color: {self.color}")
        print(f"Marca: {self.marca}")
        print(f"Tipo (analógico/digital/bolsillo): {self.tipo}")
        print(f"$ {self.precio}")

class Bateria:
    def __init__(self,color,tipo,medida,precio):
        self.color=color
        self.tipo=tipo
        self.medida=medida
        self.precio=precio
        
    def info(self):
        print("--- BATERIA PORTATIL ---")
        print(f"Color: {self.color}")
        print(f"Tipo: {self.tipo}")
        print(f"Medida: {self.medida}")
        print(f"$ {self.precio}")

class Marcador:
    def __init__(self,color,tipo,marca,precio):
        self.color=color
        self.tipo=tipo
        self.marca=marca
        self.precio=precio
        
    def info(self):
        print("--- MARCADOR ---")
        print(f"Color: {self.color}")
        print(f"Tipo (agua/permanente): {self.tipo}")
        print(f"Marca: {self.marca}")
        print(f"$ {self.precio}")

class Cable:
    def __init__(self,color,tipo,medida,precio):
        self.color=color
        self.tipo=tipo
        self.medida=medida
        self.precio=precio
        
    def info(self):
        print("--- CABLE ---")
        print(f"Color: {self.color}")
        print(f"Tipo: {self.tipo}")
        print(f"Medida: {self.medida}")
        print(f"$ {self.precio}")

class Zapato:
    def __init__(self,talla,color,marca,estilo,material,precio):
        self.talla=talla
        self.color=color
        self.marca=marca
        self.estilo=estilo
        self.material=material
        self.precio=precio

    def info(self):
        print("--- ZAPATOS ---")
        print(f"Talla: {self.talla}")
        print(f"Color: {self.color}")
        print(f"Marca: {self.marca}")
        print(f"Estilo: {self.estilo}")
        print(f"Material: {self.material}")
        print(f"$ {self.precio}")

class Tripie:
    def __init__(self,marca,material,tipo,precio):
        self.marca=marca
        self.material=material
        self.tipo=tipo
        self.precio=precio

    def info(self):
        print("--- TRIPIE ---")
        print(f"Marca: {self.marca}")
        print(f"Material: {self.material}")
        print(f"Tipo: {self.tipo}")
        print(f"$ {self.precio}")

class Lente_camara:
    def __init__(self,marca,material,color,precio):
        self.marca=marca
        self.material=material
        self.color=color
        self.precio=precio
    
    def info(self):
        print("--- LENTE DE LA CAMARA ---")
        print(f"Marca: {self.marca}")
        print(f"Material: {self.material}")
        print(f"Color: {self.color}")
        print(f"$ {self.precio}")

class Tapa:
    def __init__(self,material,color,tamaño,tipo):
        self.material=material
        self.color=color
        self.tamaño=tamaño
        self.tipo=tipo
    
    def info(self):
        print("--- TAPA DE LA CÁMARA ---")
        print(f"Material: {self.material}")
        print(f"Color: {self.color}")
        print(f"Tamaño: {self.tamaño}")
        print(f"Tipo tapa: {self.tipo}")

class Funda:
    def __init__(self,color,tipo,tamaño,precio):
        self.color=color
        self.tipo=tipo
        self.tamaño=tamaño
        self.precio=precio
    
    def info(self):
        print("--- FUNDA---")
        print(f"Color: {self.color}")
        print(f"Tipo: {self.tipo}")
        print(f"Tamaño: {self.tamaño}")
        print(f"$ {self.precio}")

class Lapiz:
    def __init__(self,color_punta,material,marca,precio):
        self.color_punta=color_punta
        self.material=material
        self.marca=marca
        self.precio=precio

    def info(self):
        print("--- LAPIZ ---")
        print(f"Color (punta lápiz): {self.color_punta}") 
        print(f"Tipo (madera/plástico): {self.material}")
        print(f"Marca: {self.marca}") 
        print(f"$ {self.precio}")   