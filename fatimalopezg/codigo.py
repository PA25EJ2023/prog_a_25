#craer un archivo llamado codigo.py dentro de tu carpeta.
#Realizar en ese archivo el siguiente programa:
#Solicitar al usuario una cadena y mandar a la pantalla
# el total de vocales que contiene la cadena

class Cadena:
    def __init__ (self,valor):
        self.valor=valor

    def contar_vocales(self):
        cont=0
        for vocal in self.valor:
            if vocal[0].upper() in 'AEIOU':
                cont=cont+1
        return cont
        

cad=input("Ingresa una cadena: ")
print ("total vocales: ",Cadena(cad).contar_vocales())