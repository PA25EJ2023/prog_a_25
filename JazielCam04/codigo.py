def contar_vocales():
    global palabra
    palabra = input("Dime la frase que deseas: ")
    vocal = ["a", "e", "i", "o", "u", "á", "é", "í", "ó", "ú"]
    cont = 0
    for i in vocal:
        for j in palabra:
            if(i==j):
                cont += 1
    print(f"El numero de vocales es: {cont}")

