from clasesfoto2 import Camisetas,Maletin,Cargadores

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