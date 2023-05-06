class Espejo:
    def __init__(self, Color, Forma):
        self.Color= Color
        self.Forma= Forma
        
    def Descripcion(self):
        print(f"Forma del espejo: {self.Forma}")
        print(f"Color del espejo: {self.Color}")

class Pluma:
    def __init__(self, Color, Diseño):
        self.Color= Color
        self.Diseño= Diseño

    def Descripcion(self):
        print(f"Color de tinta de la pluma: {self.Color}")
        print(f"Diseño de la pluma: {self.Diseño}")
        

class Plumon:
    def __init__(self, Color, Diseño):
        self.Color= Color
        self.Diseño= Diseño

    def Descripcion(self):
        print(f"Diseño del plumon: {self.Diseño}")
        print(f"Color de la tinta del plumon: {self.Color}")


class Libreta:
    def __init__(self, Color, Tamaño):
        self.Color= Color 
        self.Tamaño= Tamaño

    def Descripcion(self):
        print(f"Tamaño de la libreta: {self.Tamaño}")
        print(f"Color de la libreta: {self.Color}")


class Pinza:
    def __init__(self, Color, Tamaño):
        self.Color= Color
        self.Tamaño= Tamaño

    def Descripcion(self):
        print(f"Tamaño de la pinza: {self.Tamaño}")
        print(f"Color del pinza: {self.Color}")


class Tijera:
    def __init__(self, Color, Tamaño, Marca):
        self.Color= Color
        self.Tamaño= Tamaño
        self.Marca= Marca

    def Descripcion(self):
        print(f"Tamaño de las tijeras: {self.Tamaño}")
        print(f"Color de las tijeras: {self.Color}")
        print(f"Marca de las tijeras: {self.Marca}")


class Marco:
    def __init__(self, Color, Decoracion, Tamaño):
        self.Color= Color
        self.Decoracion= Decoracion
        self.Tamaño= Tamaño

    def Descripcion(self):
        print(f"Color del marco: {self.Color}")
        print(f"Decoracion del marco: {self.Decoracion}")
        print(f"Tamaño del espejo: {self.Tamaño}")

class Foto:
    def __init__(self, Tamaño, Tipo):
        self.Tamaño= Tamaño
        self.Tipo= Tipo

    def Descripcion(self):
        print(f"Tamaño de la foto: {self.Tamaño}")
        print(f"Tipo de foto: {self.Tipo}")

class Cinta:
    def __init__(self, Color, Tamaño):
        self.Color= Color
        self.Tamaño= Tamaño

    def Descripcion(self):
        print(f"Tamaño de la cinta: {self.Tamaño}")
        print(f"Color del cinta: {self.Color}")


class Piedrita:
    def __init__(self,Diseño,Color,Cantidad) :
        self.Diseño= Diseño
        self.Color= Color
        self.Cantidad= Cantidad

    def Descripcion(self):
        print(f"Diseño de la piedrita: {self.Diseño}")
        print(f"Color de las piedritas: {self.Color}")
        print(f"Cantidad de piedritas: {self.Cantidad}")

class Sticker:
    def __init__(self, Diseño, Color, Cantidad):
        self.Diseño= Diseño
        self.Color= Color
        self.Cantidad= Cantidad

    def Descripcion(self):
        print(f"Diseño del sticker: {self.Diseño}")
        print(f"Color del sticker: {self.Color}")
        print(f"Cantidad de stickers: {self.Cantidad}")


class Cuenta:
    def __init__(self, Color, Forma, Cantidad):
        self.Color= Color
        self.Forma= Forma
        self.Cantidad= Cantidad

    def Descripcion(self):
        print(f"Color del cuenta: {self.Color}")
        print(f"Forma de la cuenta: {self.Forma}")
        print(f"Cuentas con ese mismo color: {self.Forma}")
        

class Esmalte:
    def __init__(self, Tipo, Color):
        self.Tipo= Tipo
        self.Color= Color

    def Descripcion(self):
        print(f"Tipo de esmalte: {self.Tipo}")
        print(f"Color del esmalte: {self.Color}")


class Pegamento:
    def __init__(self, Tamaño, Diseño, Tipo):
        self.Tamaño= Tamaño
        self.Diseño= Diseño
        self.Tipo= Tipo

    def Descripcion(self):
        print(f"Tamaño el pegamento: {self.Tamaño}")
        print(f"Diseño del pegamento: {self.Diseño}")
        print(f"Tipo de pegamento: {self.Tipo}")

class Gloss:
    def __init__(self, Diseño, Color, Tamaño):
        self.Diseño= Diseño
        self.Color= Color
        self.Tamaño= Tamaño

    def Descripcion(self):
        print(f"Diseño del gloss: {self.Diseño}")
        print(f"Color del gloss: {self.Color}")
        print(f"Tamaño del gloss: {self.Tamaño}")

class Regla:
    def __init__(self, Diseño, Tamaño, Color):
        self.Diseño= Diseño
        self.Tamaño= Tamaño
        self.Color= Color

    def Descripcion(self):
        print(f"Diseño de la regla: {self.Diseño}")
        print(f"Tamaño de la regla: {self.Tamaño}")
        print(f"Color de la regla: {self.Color}")


class Telefono:
    def __init__(self, Diseño, Color):
        self.Diseño= Diseño
        self.Color= Color

    def Descripcion(self):
        print(f"Color del telefono: {self.Color}")
        print(f"Diseño del telefono: {self.Diseño}")