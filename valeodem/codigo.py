texto = input("ingrese el texto")
vocales = 0 
for letra in texto:
    if letra in 'AEIOU' or 'aeiou':
        vocales+=1
print("total vocales",vocales)



