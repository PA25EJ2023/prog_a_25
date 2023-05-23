frase=input("Dame una frase nueva")

archivo=open("frases.txt","a",encoding="utf8")#a escribir agregar w=sobre escribir
archivo.write("\n"+ frase)
archivo.close