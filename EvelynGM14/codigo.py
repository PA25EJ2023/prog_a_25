 #Solicitar al usuario una cadena y mandar a la pantalla el total de vocales que contiene la cadena.

def ContadorVocales(texto):
     totalVocales=0

     for i in texto:
         if i == "A":
             totalVocales+=1
         elif i == "E":
             totalVocales+=1
         elif i == "I":
             totalVocales+=1
         elif i == "O":
             totalVocales+=1
         elif i == "U":
             totalVocales+=1

     print(f"El total de vocales es: {totalVocales}")

texto = input("Escriba un texto: ").upper()
ContadorVocales(texto)