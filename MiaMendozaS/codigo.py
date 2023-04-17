def contar_vocales(texto):
    total_vocales= 0
    for i in texto:
        if texto == "A":
            total_vocales += 1
        elif texto == "E":
            total_vocales += 1
        elif texto == "I":
            total_vocales += 1
        elif texto == "O":
            total_vocales += 1
        elif texto == "U":
            total_vocales += 1 
    return total_vocales
    


texto = input("Ingrese un texto \n>>").upper()
print(f"La cantidad de vocales en su texto es: \n>> {contar_vocales(texto)}")



