def vocales (texto):
    vocales = "aeiou"
    resultado = ""
    for letra in texto:
        if letra in vocales:
            resultado = resultado + letra
    print(resultado)

txt = input("Ingresa la cadena: ").lower()

vocales(txt) 