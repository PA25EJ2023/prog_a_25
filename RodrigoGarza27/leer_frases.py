a_frases = open("frases.txt","r",encoding="utf8")

print (f"{'id':.<5}{'Frase':.<100}{'Autor':.<20}")
for frase in a_frases:
    datos = frase.strip().split("|")
    print(f"{datos[0]:<5}{datos[1]:<100}{datos[2]:<10}")
    
a_frases.close()
