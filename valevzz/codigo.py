#Solicitar al usuario una cadena y mandar a la pantalla el total de vocales



txt =input("Ingrese una cadena:")
numtxt = 0
for i in txt:
    if i == "A":
        numtxt=numtxt+1
    elif i == "E":
        numtxt=numtxt+1
    elif i == "I":
        numtxt=numtxt+1
    elif i == "O":
        numtxt=numtxt+1
    elif i == "U":
        numtxt=numtxt+1
    elif i == "a":
        numtxt=+1
    elif i == "e":
        numtxt=numtxt+1
    elif i == "i":
        numtxt=numtxt+1
    elif i == "o":
        numtxt=numtxt+1
    elif i == "u":
        numtxt=numtxt+1

    

print("El numero de vocales es:",numtxt)