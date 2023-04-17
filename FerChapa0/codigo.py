def BuscarV(cadena):
    cont=0
    for vocal in cadena:
        if vocal[0].upper() in 'AEIOU':
            cont=cont+1
    print (f'Las vocales son: {cont}')

cadena=input("Hola ingresa una cadena")
BuscarV(cadena)

