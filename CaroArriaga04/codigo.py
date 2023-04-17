cadena=input("Ingresa una cadena: ")
vocal=0
for letra in cadena:
    if letra[0].upper() in "AEIOU":
        vocal=vocal+1
print(f"En total tu cadena tiene {vocal} vocales")