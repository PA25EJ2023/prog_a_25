class Cadena:
    def __init__(self,valor):
        self.valor=valor

    def contar_vocales(self):
       cont=0
       for vocal in self.valor:
           if vocal[0].upper() in "AEIOU":
             cont=cont+1
        return cont       

cad=input("Ingresa una cadena:")
print("total vocales:",Cadena(cad).contar_vocales())
