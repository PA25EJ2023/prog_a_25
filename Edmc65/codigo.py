texto = input("Ingrese un texto: ")
vocales= ["a", "e", "i", "o", "u","A", "E", "I", "O", "U"]
contador = 0 
for letra in texto:
    if letra in vocales:
        contador+=1
print(f"Total Vocales: {contador}")