texto = input("Ingresa la cadena de texto: ")
cantidad_vocales = 0

vocales = ['A','a','E','e','I','i','O','o','U','u']

for vocal in texto:
    if vocal in vocales:
        cantidad_vocales+=1
        print ("Vocal: ",cantidad_vocales,vocal)

print (f"En el texto hay {cantidad_vocales} vocales")

