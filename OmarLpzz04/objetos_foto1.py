from clasesfoto1 import Boligrafo,Cuaderno,Tijeras,Plumones,Esmalte,Regla,Resistol,Fotos,Labiales,Cintas,Broches,Espejo,Telefono,Cuentas,Stickers
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

print(f"{'*'*10} BROCHES PARA CABELLO {'*'*10}")
#Clase de broches
broche1 = Broches("azul","chico","pinza","LIEB")
broche2 = Broches("rosa","chico","pinza","LIEB")
broche3 = Broches("amarillo","chico","pinza","LIEB")
broche4 = Broches("crema","chico","pinza","LIEB")
broche5 = Broches("rojo","chico","pinza","LIEB")
broche6 = Broches("naranja","chico","pinza","LIEB")
broche1.inf()
print(f"{'-'*20}")
broche2.inf()
print(f"{'-'*20}")
broche3.inf()
print(f"{'-'*20}")
broche4.inf()
print(f"{'-'*20}")
broche5.inf()
print(f"{'-'*20}")
broche6.inf()

print(f"{'*'*10} ESPEJO {'*'*10}")
#Clase de espejo
espejo = Espejo("rosa","grande","corazon",70)
espejo.inf()


print(f"{'*'*10} TELEFONO {'*'*10}")
#Clase de telefono
telefono = Telefono("crema","grande","200","telmex")
telefono.inf()

print(f"{'*'*10} CUENTAS {'*'*10}")
#Clase de cuentas
cuenta1 = Cuentas("Rojo","2","plastico","5mm")
cuenta2 = Cuentas("Rosa","5","plastico","5mm")
cuenta3 = Cuentas("Blanco","2","plastico","5mm")
cuenta4 = Cuentas("Naranja","4","plastico","5mm")
cuenta5 = Cuentas("Aqua","2","plastico","5mm")
cuenta6 = Cuentas("Lima","6","plastico","5mm")
cuenta1.info()
print(f"{'-'*20}")
cuenta2.info()
print(f"{'-'*20}")
cuenta3.info()
print(f"{'-'*20}")
cuenta4.info()
print(f"{'-'*20}")
cuenta5.info()
print(f"{'-'*20}")
cuenta6.info()

print(f"{'*'*10} STICKERS {'*'*10}")
#Clase de stickers 
sticker1 = Stickers("Nuevo",25,"Gota","Plastico")
sticker2 = Stickers("Nuevo",26,"Estrella","Plastico")
sticker3 = Stickers("Usado",15,"Estrella","Plastico")
sticker4 = Stickers("Nuevo",8,"Corazón","Papel")
sticker5 = Stickers("Usado",12,"Estrella","Papel")
sticker6 = Stickers("Usado",15,"Flor","Papel")

sticker1.info()
print(f"{'-'*20}")
sticker2.info()
print(f"{'-'*20}")
sticker3.info()
print(f"{'-'*20}")
sticker4.info()
print(f"{'-'*20}")
sticker5.info()
print(f"{'-'*20}")
sticker6.info()
