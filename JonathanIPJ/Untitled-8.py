print("  ")
print("  ")

while True:
    print("1.-Suma de numeros")
    print("2.-Total de divisores de un numero")
    print("3.-Salir")
    opcion = int(input("¿Cual opcion quiere elegir?       "))
    
    if opcion == 1:
        cantidad = int(input("¿Cuantos numeros quieres sumar?    "))
        suma = 0
        cont = 0
        while cont < cantidad:
            numero = int(input("Ingrese un numero     "))
            suma += numero
            cont += 1
            print("La suma es:", suma)

    elif opcion == 2:
        numero = int(input("Ingresa un numero     "))
        divisor = 1
        total_div = 0
        while divisor <= numero:
            if numero % divisor == 0:
                total_div += 1
                divisor += 1
                print("total divisores ", total_div)
    
    elif opcion == 3:
        break
    
    else:
        print("ERROR")
        break












