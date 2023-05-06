from clasesfoto2 import Camisetas,Maletin,Cargadores,Lapices,Celular,Zapatos,Lentes,Tripie,Revista,Reloj,Plumon,Estuche,Cargadores_camaras

print(f"{'*'*10} CAMISAS {'*'*10}")
camisa1 = Camisetas("blanca","mediana","abotonada")
camisa2 = Camisetas("gris","grande","chaqueta")
camisa1.inf()
print("-"*20)
camisa2.inf()

print(f"{'*'*10} MALETIN {'*'*10}")
maletin = Maletin("Cafe","grande","cuero")
maletin.inf()

print(f"{'*'*10} CARGADORES {'*'*10}")
cargador1 = Cargadores("blanco","30cmm","para laptop","apple")
cargador2 = Cargadores("negro","12cmm","para celular","android")
cargador1.inf()
print("-"*20)
cargador2.inf()

print(f"{'*'*10} LAPICES {'*'*10}")
lapiz1 = Lapices("negro","10 cm","LYRA")
lapiz2 = Lapices("negro","10 cm","LYRA")
lapiz3 = Lapices("blanco","10 cm","LYRA")
lapiz1.inf()
print("-"*20)
lapiz2.inf()
print("-"*20)
lapiz3.inf()

print(f"{'*'*10} CELULAR {'*'*10}")
celular = Celular("negro","alcatel","android","touch")
celular.inf()

print(f"{'*'*10} ZAPATOS {'*'*10}")
zapatos = Zapatos(7.5,"naranjas","cuero")
zapatos.inf()

print(f"{'*'*10} LENTES DE CAMARA {'*'*10}")
lente1 = Lentes("grande","zoom",70,"Canon")
lente2 = Lentes("mediana","vision nocturna",30,"Canon")
lente1.inf()
print("-"*20)
lente2.inf()

print(f"{'*'*10} TRIPIE {'*'*10}")
tripie = Tripie(40,"negro","EXCELL")
tripie.inf() 

print(f"{'*'*10} REVISTA {'*'*10}")
revista = Revista("Blanco","Deportes,Musica","Juice","12 dolares")
revista.inf()

print(f"{'*'*10} RELOJ {'*'*10}")
reloj = Reloj("casio","negro",200,"moderno")
reloj.inf()

print(f"{'*'*10} MARCADOR {'*'*10}")
plumon = Plumon("negro","Calligraphy Pen",3.0)
plumon.inf()

print(f"{'*'*10} ESTUCHE {'*'*10}")
estuche = Estuche("Negro","Tela textil y plastico",300,"Camara")
estuche.inf()

print(f"{'*'*10} CARGADORES DE CAMARAS {'*'*10}")
cargador1_cam = Cargadores_camaras("King","Negro","Camaras",500)
cargador2_cam = Cargadores_camaras("King","Negro","Camaras",500)
cargador1_cam.inf()
print("-"*20)
cargador2_cam.inf()