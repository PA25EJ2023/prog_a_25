from clasesfoto2 import Camisetas,Maletin,Cargadores,Lapices,Celular,Zapatos,Lentes,Tripie,Revista

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
zapatos = Zapatos("naranjas",7.5,"cuero")
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

print(f"{'*'*10} TRIPIE {'*'*10}")
revista = Revista("Blanco","Deportes,Musica","Juice","12 dolares")
revista.inf()