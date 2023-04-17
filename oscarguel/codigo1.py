frase = input("Introduce un texto: ")
vocales = 0

for letra in frase:
    if letra.upper() in "AEIOU":
        vocales += 1

print("Total de vocales:", vocales)

