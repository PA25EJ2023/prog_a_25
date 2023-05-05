from clasesfoto1 import Boligrafo,Cuaderno,Tijeras,Plumones,Esmalte,Regla,Resistol,Fotos,Labiales,Cintas
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
esmalte4.inf()
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

print(f"{'*'*10} FOTOS {'*'*10}")
#Clase de fotos
foto1 = Fotos("grande","visible","cuadrada","flores y estrellas")
foto2 = Fotos("grande","visible","cuadrada","estrellas y lunas")

foto1.inf()
print(f"{'-'*20}")
foto2.inf()

print(f"{'*'*10} BRILLOS LABIALES {'*'*10}")
#Clase de labiales
labial1 = Labiales("blanco","mediano","cilindrico","AVON")
labial2 = Labiales("naranja","mediano","cilindrico","AVON")
labial3 = Labiales("rosa","mediano","cilindrico","AVON")

labial1.inf()
print(f"{'-'*20}")
labial2.inf()
print(f"{'-'*20}")
labial3.inf()

print(f"{'*'*10} CINTAS {'*'*10}")
#Clase de cintas
cinta1 = Cintas("rosa","gloria",1.5,1)
cinta2 = Cintas("crema","maboto",1.5,1)
cinta3 = Cintas("verde","gloria",1.5,1)

cinta1.inf()
print(f"{'-'*20}")
cinta1.inf()
print(f"{'-'*20}")
cinta3.inf()
