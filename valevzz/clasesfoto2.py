class Bateria_Portatil:
    def __init__(self,numero,color,marca,tamaño):
        self.numero = numero
        self.color = color
        self.marca = marca
        self.tamaño = tamaño

    def info (self):
        print(f"Numero bateria: {self.numero} \nColor: {self.color} \nMarca: {self.marca} \nTamaño:{self.tamaño}")

class Celular:
    def __init__(self,numero,color,modelo,marca):
        self.numero = numero
        self.color = color
        self.modelo = modelo
        self.marca = marca

    def info (self):
        print(f"Numero celular: {self.numero} \nColor: {self.color} \nMarca: {self.marca} \nModelo:{self.modelo}")

class Camisas:
    def __init__(self,numero,color,marca,tela):
        self.numero = numero
        self.color = color
        self.marca = marca
        self.tela = tela

    def info (self):
        print(f"Numero camisa: {self.numero} \nColor: {self.color} \nMarca: {self.marca} \nTipo de tela:{self.tela}")

class Cables:
    def __init__(self,numero,color,dispo, marca):
        self.numero = numero
        self.color = color
        self.dispo = dispo
        self.marca = marca

    def info(self):
        print(f"Numero cable: {self.numero} \nColor: {self.color} \nDispositivo al que pertenece: {self.dispo} \nMarca: {self.marca}")

class Maletin:
    def __init__(self,numero,color,marca,tamaño):
        self.numero = numero
        self.color = color
        self.marca = marca
        self.tamaño = tamaño

    def info (self):
        print(f"Numero maletin: {self.numero} \nColor: {self.color} \nMarca: {self.marca} \nTamaño:{self.tamaño}")

class Lente_Camara:
    def __init__(self,numero,color,marca,tamaño):
        self.numero = numero
        self.color = color
        self.marca = marca
        self.tamaño = tamaño

    def info (self):
        print(f"Numero Lente: {self.numero} \nColor: {self.color} \nMarca: {self.marca} \nTamaño:{self.tamaño}")

class Tapa_Lente:
    def __init__(self,numero,color,marca,tamaño):
        self.numero = numero
        self.color = color
        self.marca = marca
        self.tamaño = tamaño
       
    def info (self):
        print(f"Numero Tapa: {self.numero} \nColor: {self.color} \nMarca: {self.marca} \nTamaño:{self.tamaño}")

class Revista:
    def __init__(self,numero,nombre,titulo,fecha_publicacion):
        self.numero = numero
        self.nombre = nombre
        self.titulo = titulo
        self.fecha_publicacion = fecha_publicacion

    def info (self):
        print(f"Numero Revista: {self.numero} \nNombre: {self.nombre} \nTitulo: {self.titulo} \nFecha de publicacion: {self.fecha_publicacion} ")

class Mac:
    def __init__(self,numero,color,marca,modelo):
        self.numero = numero
        self.color = color
        self.modelo = modelo
        self.marca = marca

    def info (self):
        print(f"Numero Mac: {self.numero} \nColor: {self.color} \nMarca: {self.marca} \nModelo:{self.modelo}")

class Reloj:
    def __init__(self,numero,color,modelo,marca):
        self.numero = numero
        self.color = color
        self.modelo = modelo
        self.marca = marca

    def info (self):
        print(f"Numero Reloj: {self.numero} \nColor: {self.color} \nMarca: {self.marca} \nModelo:{self.modelo}")

class Tripoide:
    def __init__(self,numero,color,marca,modelo):
        self.numero = numero
        self.color = color
        self.marca = marca
        self.modelo = modelo

    def info (self):
        print(f"Numero Tripoide: {self.numero} \nColor: {self.color} \nMarca: {self.marca} \nModelo: {self.modelo}")

class Zapatos:
    def __init__(self,numero,color,marca,modelo):
        self.numero = numero
        self.color = color
        self.marca = marca
        self.modelo = modelo

    def info (self):
        print(f"Numero Zapatos: {self.numero} \nColor: {self.color} \nMarca: {self.marca} \nModelo: {self.modelo}")

class Plumones:
      def __init__(self,numero,color,marca,tipo_punta):
            self.numero = numero 
            self.color = color
            self.marca = marca
            self.tipo_punta = tipo_punta

      def info (self):
            print(f"Numero plumon: {self.numero} \nColor: {self.color} \nMarca: {self.marca} \nTipo punta: {self.tipo_punta}")

class Lapices:
      def __init__(self,numero,color,marca,tipo_punta):
            self.numero = numero 
            self.color = color
            self.marca = marca
            self.tipo_punta = tipo_punta

      def info (self):
            print(f"Numero lapiz: {self.numero} \nColor: {self.color} \nMarca: {self.marca} \nTipo punta: {self.tipo_punta}")


class Estuche:
    def __init__(self,numero,color,marca,modelo):
        self.numero = numero
        self.color = color
        self.marca = marca
        self.modelo = modelo

    def info (self):
        print(f"Numero estuche: {self.numero} \nColor: {self.color} \nMarca: {self.marca} \nModelo: {self.modelo}")

class Bateria_Camara:
    def __init__(self,numero,color,modelo,tipo_duracion):
        self.numero = numero
        self.color = color
        self.modelo = modelo
        self.tipo_duracion = tipo_duracion

    def info (self):
        print(f"Numero bateria de camara: {self.numero} \nColor: {self.color} \nModelo: {self.modelo} \nDuracion de la pila: {self.tipo_duracion}")
