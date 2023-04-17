cadena = input("Ingrese Texto: ")
vocales = 0

for caracter in cadena:
    if caracter in "aeiouAEIOU":
        vocales += 1

print(f"El numero de vocales de la cadena es: {vocales}")
