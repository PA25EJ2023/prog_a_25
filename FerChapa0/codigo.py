def BuscarV(cadena):
    for vocal in cadena:
        if vocal[0].upper() in 'AEIOU':
            print (f'Las vocales son: {vocal}')

cadena=input("Hola ingresa una cadena")
BuscarV(cadena)

