archivo = open ("datos.txt", "r")

for linea in archivo:
    print(linea,end='')

    archivo.close

