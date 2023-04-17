texto = input("ingrese un texto para detectar la cantidad de vocales: ")
vocales = "aeioouAEIOU"
contador = 0
for voc in texto :
    if voc in vocales:
        contador = contador + 1

print ("el texto ",texto," tiene ", contador," vocales")    

