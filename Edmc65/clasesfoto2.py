class Camisa:
    def __init__(self, Color, Tipo, Marca):
        self.Color= Color
        self.Tipo= Tipo
        self.Marca= Marca
        
    def Descripcion(self):
        print(f"Color de la camisa: {self.Color}")
        print(f"Tipo de camisa: {self.Tipo}")
        print(f"Marca de la camisa: {self.Marca}")

class Celular:
    def __init__(self, Color, Marca) :
        self.Color = Color
        self.Marca = Marca

    def Descripcion(self):
        print(f"Color del celular: {self.Color}")
        print(f"Marca del celular: {self.Marca}")

class DiscoDuro:
    def __init__(self, Capacidad, Proteccion):
        self.Capacidad= Capacidad
        self.Proteccion= Proteccion

    def Descripcion(self):
        print(f"Capacidad del Disco Duro: {self.Capacidad}")
        print(f"Tipo de protecicion: {self.Proteccion}")


class Cable:
    def __init__(self, Tipo, Color):
        self.Tipo= Tipo
        self.Color= Color

    def Descripcion(self):
        print(f"Tipo de cable: {self.Tipo}")
        print(f"Color de cable: {self.Color}")

class Bolsa:
    def __init__(self, Tipo, Color, Material):
        self.Tipo= Tipo
        self.Color= Color
        self.Material= Material
    
    def Descripcion(self):
        print(f"Tipo de bolsa: {self.Tipo}")
        print(f"Color de bolsa: {self.Color}")
        print(f"Material de bolsa: {self.Material}")

class BateriaCam:
    def __init__(self, Marca, Capacidad):
        self.Marca= Marca
        self.Capacidad= Capacidad

    def Descripcion(self):
        print(f"Marca de la bateria: {self.Marca}")
        print(f"Capacidad de la bateria: {self.Capacidad}")

class LenteCam:
    def __init__(self, Marca, Distancia_Focal):
        self.Marca= Marca
        self.Distancia_Focal= Distancia_Focal

    def Descripcion(self):
        print(f"Marca del lente: {self.Marca}")
        print(f"Distancia Focal de la Cam: {self.Distancia_Focal} mm")

class Laptop:
    def __init__(self, Marca, Color):
        self.Marca= Marca
        self.Color= Color

    def Descripcion(self):
        print(f"Marca de la laptop: {self.Marca}")
        print(f"Color de la laptop: {self.Color}")

class Revista:
    def __init__(self, Nombre, Tema):
        self.Nombre= Nombre
        self.Tema= Tema

    def Descripcion(self):
        print(f"Nombre de la revista: {self.Nombre}")
        print(f"Tema de la revista: {self.Tema}")

class Tripie:
    def __init__(self, Marca, Tipo, Color):
        self.Marca= Marca
        self.Tipo= Tipo
        self.Color= Color

    def Descripcion(self):
        print(f"Marca del tripie: {self.Marca}")
        print(f"Tipo de tripie: {self.Tipo}")
        print(f"Color del tripie: {self.Color}")

class Reloj:
    def __init__(self, Marca, Color):
        self.Marca= Marca
        self.Color= Color

    def Descripcion(self):
        print(f"Marca del reloj: {self.Marca}")
        print(f"Color del reloj: {self.Color}")

class Zapatos:
    def __init__(self, Color, Talla):
        self.Color= Color
        self.Talla= Talla

    def Descripcion(self):
        print(f"Color de los zapatos: {self.Color}")
        print(f"Talla de los zapatos: {self.Talla}")

class Pluma:
    def __init__(self, Marca, Color, Tamaño) -> None:
        self.Marca= Marca
        self.Color= Color
        self.Tamaño= Tamaño

    def Descripcion(self):
        print(f"Marca de la pluma: {self.Marca}")
        print(f"Color de la pluma: {self.Color}")
        print(f"Tamaño de punta: {self.Tamaño} mm")

class Lapiz:
    def __init__(self, Marca, Tamaño, Color):
        self.Marca= Marca
        self.Tamaño= Tamaño
        self.Color= Color

    def Descripcion(self):
        print(f"Marca del lapiz: {self.Marca}")
        print(f"Tamaño de punta: {self.Tamaño} mm")
        print(f"Color del lapiz: {self.Color}")
