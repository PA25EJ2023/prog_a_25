class Boligrafo:
    def __init__(self,color,tamaño,precio,marca):
        self.color = color
        self.tamaño = tamaño
        self.precio = precio
        self.marca = marca
    
    def info(self):
        print(f"1 BOLIGRAFO\nColor: {self.color}\nTamaño: {self.tamaño}\nPrecio: {self.precio}\nMarca: {self.marca}")
        print("-"*25)


class Marcador:
    def __init__(self,color,tamaño,precio,marca):
        self.color = color
        self.tamaño = tamaño
        self.precio = precio
        self.marca = marca

    def info(self):
        print(f"1 MARCADOR\nColor: {self.color}\nTamaño: {self.tamaño}\nPrecio: {self.precio}\nMarca: {self.marca}")
        print("-"*25)


class Cinta_Adhesiva:
    def __init__(self,color,ancho,longitud,marca):
        self.color = color
        self.ancho = ancho
        self.longitud =longitud
        self.marca = marca

    def info(self):
        print(f"1 CINTA ADHESIVA\nColor: {self.color}\nAncho: {self.ancho}\nLongitud: {self.longitud}\nMarca: {self.marca}")
        print("-"*25)


class Portaretrato:
    def __init__(self,tamaño,color_marco,material,precio):
        self.tamaño = tamaño
        self.color_marco = color_marco
        self.material = material
        self.precio = precio

    def info(self):
        print(f"1 PORTARETRATO\nTamaño: {self.tamaño}\nColor del marco: {self.color_marco}\nMaterial: {self.material}\nPrecio: {self.precio}")
        print("-"*25)


class Esmalte:
    def __init__(self,color,marca,forma,gramaje):
        self.color = color
        self.marca = marca
        self.forma = forma
        self.gramaje = gramaje

    def info(self):
        print(f"1 ESMALTE\nColor: {self.color}\nMarca: {self.marca}\nForma: {self.forma}\nGramaje: {self.gramaje}")
        print("-"*25)


class Espejo:
    def __init__(self,color,forma,tamaño,precio):
        self.color = color
        self.forma = forma
        self.tamaño = tamaño
        self.precio = precio

    def info(self):
        print(f"1 ESPEJO\nColor: {self.color}\nForma: {self.forma}\nTamaño: {self.tamaño}\nPrecio: {self.precio}")
        print("-"*25)


class Pinza:
    def __init__(self,color,forma, tamaño, marca):
        self.color = color
        self.forma = forma
        self.tamaño = tamaño
        self.marca = marca

    def info(self):
        print(f"1 PINZA\nColor: {self.color}\nForma: {self.forma}\nTamaño: {self.tamaño}\nMarca: {self.marca}")
        print("-"*25)


class Brillo_labial:
    def __init__(self,color,marca,tamaño,precio):
        self.color = color
        self.marca = marca
        self.tamaño = tamaño
        self.precio = precio

    def info(self):
        print(f"1 BRILLO LABIAL\nColor: {self.color}\nMarca: {self.marca}\nTamaño: {self.tamaño}\nPrecio: {self.precio}")
        print("-"*25)


class Cuaderno:
    def __init__(self,color,tamaño,no_hojas,marca):
        self.color = color
        self.tamaño = tamaño
        self.no_hojas = no_hojas
        self.marca = marca

    def info(self):
        print(f"1 CUADERNO\nColor: {self.color}\nTamaño: {self.tamaño}\nNúmero de hojas: {self.no_hojas}\nMarca: {self.marca}")
        print("-"*25)


class Regla:
    def __init__(self,color,tamaño,forma,material):
        self.color = color
        self.tamaño = tamaño
        self.forma = forma
        self.material = material

    def info(self):
        print(f"1 REGLA\nColor: {self.color}\nTamaño: {self.tamaño}\nForma: {self.forma}\nMaterial: {self.material}")
        print("-"*25)


class Pegamento:
    def __init__(self,color,tamaño,marca,precio):
        self.color = color
        self.tamaño = tamaño
        self.marca = marca
        self.precio = precio

    def info(self):
        print(f"1 PEGAMENTO\nColor: {self.color}\nTamaño: {self.tamaño}\nMarca: {self.marca}\nPrecio: {self.precio}")
        print("-"*25)


class Diario:
    def __init__(self,color,tamaño,no_hojas,precio):
        self.color = color
        self.tamaño = tamaño
        self.no_hojas = no_hojas
        self.precio = precio

    def info(self):
        print(f"1 DIARIO\nColor: {self.color}\nTamaño: {self.tamaño}\nNúmero de hojas: {self.no_hojas}\nPrecio: {self.precio}")
        print("-"*25)


class Lapicero:
    def __init__(self,color,material,precio, marca):
        self.color = color
        self.material = material
        self.precio = precio
        self.marca = marca

    def info(self):
        print(f"1 LAPICERO\nColor: {self.color}\nMaterial: {self.material}\nPrecio: {self.precio}\nMarca: {self.marca}")
        print("-"*25)


class Telefono:
    def __init__(self,color,tipo,medida,modelo):
        self.color = color
        self.tipo = tipo
        self.medida = medida
        self.modelo = modelo

    def info(self):
        print(f"1 TELEFONO\nColor: {self.color}\nTipo: {self.tipo}\nMedida: {self.medida}\nModelo: {self.modelo}")
        print("-"*25)


class Tijeras:
    def __init__(self,color,tamaño,marca,forma_punta):
        self.color = color
        self.tamaño = tamaño
        self.marca = marca
        self.forma_punta = forma_punta

    def info(self):
        print(f"1 TIJERAS\nColor: {self.color}\nTamaño: {self.tamaño}\nMarca: {self.marca}\nForma de la punta: {self.forma_punta}")
        print("-"*25)


class Paleta_sombras:
    def __init__(self,color,cantidad_sombras,marca,precio):
        self.color = color
        self.cantidad_sombras = cantidad_sombras
        self.marca = marca
        self.precio = precio

    def info(self):
        print(f"1 PALETA DE SOMBRAS\nColor: {self.color}\nCantidad de sombras: {self.cantidad_sombras}\nMarca: {self.marca}\nPrecio: {self.precio}")
        print("-"*25)


class Poster:
    def __init__(self,color,tamaño,diseño,material):
        self.color = color
        self.tamaño = tamaño
        self.diseño = diseño
        self.material = material

    def info(self):
        print(f"1 POSTER\nColor: {self.color}\nTamaño: {self.tamaño}\nDiseño: {self.diseño}\nMaterial: {self.material}")
        print("-"*25)


class Pulsera:
    def __init__(self,color,diseño,medida,categoria):
        self.color = color
        self.diseño = diseño
        self.medida = medida
        self.categoria = categoria

    def info(self):
        print(f"1 PULSERA\nColor: {self.color}\nDiseño: {self.diseño}\nMedida: {self.medida}\nMaterial: {self.categoria}")
        print("-"*25)

class Nota_adhesiva:
    def __init__(self,color,tamaño,marca,material):
        self.color = color
        self.tamaño = tamaño
        self.marca = marca
        self.material = material

    def info(self):
        print(f"1 NOTA ADHESIVA\nColor: {self.color}\nTamaño: {self.tamaño}\nMarca: {self.marca}\nPrecio: {self.material}")
        print("-"*25)

class Tarjeta:
    def __init__(self,color,diseño,medida,material):
        self.color = color
        self.diseño = diseño
        self.medida = medida
        self.material = material

    def info(self):
        print(f"1 TARJETA\nColor: {self.color}\nDiseño: {self.diseño}\nMedida: {self.medida}\nMaterial: {self.material}")
        print("-"*25)


class Fotografía:
    def __init__(self,color,tamaño,diseño,material):
        self.color = color
        self.tamaño = tamaño
        self.diseño = diseño
        self.material = material

    def info(self):
        print(f"1 FOTOGRAFÍA\nColor: {self.color}\nTamaño: {self.tamaño}\nDiseño: {self.diseño}\nMaterial: {self.material}")
        print("-"*25)


class Serie_cuentas:
    def __init__(self,color,cantidad,material,tamaño):
        self.color = color
        self.cantidad = cantidad
        self.material = material
        self.tamaño = tamaño

    def info(self):
        print(f"1 SERIE DE CUENTAS\nColor: {self.color}\nCantidad: {self.cantidad}\nMaterial: {self.material}\nTamaño: {self.tamaño}")
        print("-"*25)


class Serie_stickers:
    def __init__(self,estado,cantidad,forma,material):
        self.estado = estado
        self.cantidad = cantidad
        self.forma = forma
        self.material = material

    def info(self):
        print(f"1 SERIE DE STICKERS\nEstado: {self.estado}\nCantidad: {self.cantidad}\nForma: {self.forma}\nMaterial: {self.material}")
        print("-"*25)

        

    







    



