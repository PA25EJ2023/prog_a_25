a_frases=open("frases.txt","r",encoding="utf8")
#Encabezado
print(f"{'Id':<5} {'Frase':<70}{'Autor':<20} ")
for frase in a_frases:
    datos=frase.strip().split("|")
    print(f"{datos[0]:<5} {datos[1]:<70}{datos[2]:<20} ")

a_frases.close()