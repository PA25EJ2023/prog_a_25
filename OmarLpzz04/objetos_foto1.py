from clasesfoto1 import Boligrafo,Cuaderno,Tijeras,Plumones
print(f"{'*'*10} PLUMAS {'*'*10}")
#Clase de plumas
pluma = Boligrafo("rojo","bic","grande",10)
pluma.escribir()
print(f"{'*'*10} LIBRETAS {'*'*10}")
#Clase de libretas
libreta = Cuaderno("rosa","scribe","chica",18)
libreta.escribir()
print(f"{'*'*10} PLUMONES {'*'*10}")
#Clase de plumnoes
marcador = Plumones("pastel","sharpie","grande",25)
marcador.escribir()

