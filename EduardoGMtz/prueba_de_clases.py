class Pila_portatil:
    def __init__(self, color, tamaño):
          self.color = color
          self.tamaño = tamaño

    def atributos_pila_P(self):
        print(f"La pila portatil es de color {self.color} y el tamaño es de {self.tamaño}")

pila_p = Pila_portatil("negro", "5")
pila_p.atributos_pila_P()