
archivo_frases = open("frases.txt","r",encoding="utf8")

print(f"{'id':.<5}{'Frase':.<80}{'Autor':.<20}")
for frase in archivo_frases:
    datos = frase.strip().split("|")
    print(f"{datos[0]:<5}{datos[1]:<80}{datos[2]:<20}")

archivo_frases.close()

