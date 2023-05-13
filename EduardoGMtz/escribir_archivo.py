

frase = input("Cual es la frase nueva")

archivo = open("frases.txt","a")

archivo.write("\n" + frase)

archivo.close()