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
