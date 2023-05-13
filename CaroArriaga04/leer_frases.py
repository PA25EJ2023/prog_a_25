a_frases=open("frases.txt","r",encoding="utf8")

#encabezado
print(f"{'Id':.<5}{'Frase':.<80}{'Autor':.<20}")
for frase in a_frases:
    datos = frase.strip().split("|")
    print(f"{datos[0]:<5}{datos[1]:<80}{datos[2]:<20}")

a_frases.close()

