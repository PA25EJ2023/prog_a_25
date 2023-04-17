texto = input("Introduce una cadena de texto: ")
vocales = 0

for letra in texto:
    if letra in "AEIOUaeiou":
        vocales += 1

print("Total de vocales:", vocales)
