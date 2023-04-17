def contador_vocales(cadena):
    vocales = "aeiouAEIOU"
    contador = 0

    for letra in cadena: 
        if letra in vocales:
            contador += 1
    return contador

cadena = input("Ingrese una cadena cualquiera: ")
total_de_vocales = contador_vocales(cadena)

print(f"La cantidad de vocales son: {total_de_vocales}")