from clasesfoto1 import Boligrafo,Cuaderno,Tijeras,Plumones,Esmalte,Regla,Resistol
print(f"{'*'*10} PLUMAS {'*'*10}")
#Clase de plumas
pluma1 = Boligrafo("rosa","bic","grande",17)
pluma2 = Boligrafo("azul","bic","grande",17)
pluma3 = Boligrafo("amarillo","bic","grande",20)
pluma4 = Boligrafo("naranja","bic","grande",14)
pluma1.inf()
print(f"{'-'*20}")
pluma2.inf()
print(f"{'-'*20}")
pluma3.inf()
print(f"{'-'*20}")
pluma4.inf()
print(f"{'*'*10} LIBRETAS {'*'*10}")
#Clase de libretas
libreta1 = Cuaderno("rosa","scribe","profesional","resorte")
libreta2 = Cuaderno("azul","scribe","profesional","cosida")
libreta3 = Cuaderno("naranja","scribe","profesional","resorte")

libreta1.inf()
print(f"{'-'*20}")
libreta2.inf()
print(f"{'-'*20}")
libreta3.inf()


print(f"{'*'*10} PLUMONES {'*'*10}")
#Clase de plumones
marcador1 = Plumones("rosa","sharpie","grande",25)
marcador2 = Plumones("naranja","sharpie","grande",25)
marcador3 = Plumones("morado","sharpie","grande",25)
marcador1.inf()
print(f"{'-'*20}")
marcador2.inf()
print(f"{'-'*20}")
marcador3.inf()



print(f"{'*'*10} TIJERAS {'*'*10}")
#Clase de tijeras
tijeras = Tijeras("azulez","barrilito","grandes",23)
tijeras.inf()

print(f"{'*'*10} ESMALTES {'*'*10}")
#Clase de esmaltes
esmalte1 = Esmalte("rosa","bissu","chicos","diamante",)
esmalte2 = Esmalte("brillos","bissu","chicos","diamante",)
esmalte3 = Esmalte("blanco","bissu","chicos","cubo",)
esmalte4 = Esmalte("crema","bissu","chicos","diamante",)
esmalte5 = Esmalte("rojo","bissu","chicos","cuadrado",)
esmalte6 = Esmalte("azul","bissu","chicos","cilindrico",)
esmalte7 = Esmalte("dorado","bissu","chicos","cilindrico",)

esmalte1.inf()
print(f"{'-'*20}")
esmalte2.inf()
print(f"{'-'*20}")
esmalte3.inf()
print(f"{'-'*20}")
esmalte4.inf
print(f"{'-'*20}")
esmalte5.inf()
print(f"{'-'*20}")
esmalte6.inf()
print(f"{'-'*20}")
esmalte7.inf()

print(f"{'*'*10} REGLA {'*'*10}")
#Clase de regla
regla = Regla("rosa",30,"triangular","scolari")
regla.inf()

print(f"{'*'*10} PEGAMENTO {'*'*10}")
#Clase de pegamento
pegamento = Resistol("rosa","mediano","prit","cilindrica")
pegamento.inf()