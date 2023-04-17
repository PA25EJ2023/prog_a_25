cadena = input("Ingresa una cadena de texto: ")
vocales = ['a', 'e', 'i', 'o', 'u']
cantidad_vocales = 0

for letra in cadena:
    if letra.lower() in vocales:
        print(letra.lower())
        cantidad_vocales += 1

print (f"En la cadena ingresada hay {cantidad_vocales} vocales")
