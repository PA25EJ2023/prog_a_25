#programa que solicita al usuario una cadena y manda a pantalla el total de vocales que
#contiene la cadena
def ContadorVocal(cadena):
    cont=0
    vocales="aeiouAEIOU"
    for letra in cadena:
        if letra in vocales:
            cont+=1
    return cont

texto=(input("Ingrese una cadena de texto: "))
totalVocal=ContadorVocal(texto)
print(f"Total de vocales: {totalVocal}")