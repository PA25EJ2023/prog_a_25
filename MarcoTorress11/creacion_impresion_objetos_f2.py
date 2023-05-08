from clasesfoto2 import (Celular, Camisa, Portafolio, Lentes, Tapas, Computadora, Pila_camara, Pila_portatil, Tripode, Zapatos, Plumas, Lapiz, Estuche, Cable, Reloj, Revista)

cel1 = Celular(1, "negro","25", "Sony", "Xperia")
cel1.atributos_cel()
print("")

camisa1 = Camisa(1, "Blanca", "M", "All saints", "Algodon")
camisa1.atributos_camisa()
camisa2 = Camisa(1, "Negro", "M", "All saints", "Mezclilla")
camisa2.atributos_camisa()
print("")

portafolio1 = Portafolio(1, "Café", "Mediano", "Ralph Lauren", "Cuero")
portafolio1.info()
print("")

lente1 = Lentes(1, "Negro", "12", "Canon","Plástico y vidrio", "30")
lente1.info_cam()
lente2 = Lentes(2, "Negro", "15", "Canon","Plástico y vidrio", "50")
lente2.info_cam()
print("")

tapa1 = Tapas(1, "Negro", "6", "Canon", "Plástico")
tapa1.info_tapa()
tapa2 = Tapas(2, "Negro", "7", "Canon", "Plástico")
tapa2.info_tapa()
tapa3 = Tapas(3, "Negro", "8", "Canon", "Plástico")
tapa3.info_tapa()
print("")

compu1 = Computadora(1, "Gris", "16", "Apple", "Aluminio","4")
compu1.info_compu()
print("")

pilap1 = Pila_portatil(1, "Negro", "10", "Adata", "Plástico y metal", "200", "10,000")
pilap1.info_pilaP()
print("")

pilac1 = Pila_camara(1, "Negro", "7", "Sony", "Plástico y metal", "300", "6,000")
pilac1.info_pilaC()
pilac2 = Pila_camara(2, "Negro", "7", "Sony", "Plástico y metal", "300", "6,000")
pilac2.info_pilaC()
print("")

tri1 = Tripode(1, "Negro", "20", "80", "Canon", "Metal", "200", "2")
tri1.info_tri()
print("")

zapatos1 = Zapatos(1, "Negro", "27", "Zara", "Piel", "Casual")
zapatos1.info_zapato()
print("")

pluma1 = Plumas(1, "Negro", "1", "Bic", "Plástico")
pluma1.info_plumas()
print("")

lpz1 = Lapiz(1, "Negro", "2", "Lyra", "Madera")
lpz1.info_lapiz()
lpz2 = Lapiz(2, "Negro", "2", "Lyra", "Madera")
lpz2.info_lapiz()
lpz3 = Lapiz(3, "Negro", "2", "Lyra", "Madera")
lpz3.info_lapiz()
lpz4 = Lapiz(4, "Amarillo", "3", "Lyra", "Madera")
lpz4.info_lapiz()
print("")

estuche1 = Estuche(1, "Negro", "Mediano", "Canon", "Tela")
estuche1.info_estuche()
print("")

cbl1 = Cable(1, "Negro", "20", "Samsung", "Cargador")
cbl1.info_cable()
cbl2 = Cable(2, "Blanco", "100", "Apple", "Cargador")
cbl2.info_cable()
cbl3 = Cable(3, "Blanco", "100", "Apple", "Conector")
cbl3.info_cable()
print("")

rlj1 = Reloj(1, "Negro", "44", "Fossil", "Analógico", "Metal y safiro")
rlj1.info_reloj()
print("")

revista1 = Revista(1, "Blanco", "Juice", "Juvenil", "Papel")
revista1.info_revista()