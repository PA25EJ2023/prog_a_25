from Clases_Foto2 import Laptop,Reloj_Muñeca,Tripode_Camara,Par_Zapatos,Lapiz,Boligrafo,Funda_Camara,Cargador,Disparador_Flash

#LAPTOP
laptop = Laptop("Color Plata","Grosor.1.56cm Ancho.30.41cm Profundidad.21.24cm","13.3 pulgadas","Apple")
print(f"{'-'*30} LAPTOP {'-'*30}")
laptop.mostrar_info()

#RELOJ DE MUÑECA
reloj = Reloj_Muñeca("Negro","22x5.1 cm","51 mm","Acero inoxidable ")
print(f"{'-'*30} RELOJ DE MUÑECA {'-'*30}")
reloj.mostrar_info()

#TRÍPODE CAMARA
tripode_cam = Tripode_Camara("Negro","144 cm","44.1 cm","47.6 cm","Aluminio y Plástico")
print("")
print(f"{'-'*30} TRÍPODE DE CÁMARA {'-'*30}")
tripode_cam.mostrar_info()

#ZAPATOS
zapatos = Par_Zapatos("Café","26","Piel","Redonda","Cordones")
print("")
print(f"{'-'*30} ZAPATOS {'-'*30}")
zapatos.mostrar_info()

#LAPIZ
lapiz1 = Lapiz("Negro","12 cm","Hexagonal","Lyra")
lapiz2 = Lapiz("Negro","12 cm","Hexagonal","Lyra")
lapiz3 = Lapiz("Negro","12 cm","Hexagonal","Lyra")
print("")
print(f"{'-'*30} LÁPICES {'-'*30}")
print(f"{'-'*5} Lápiz 1 {'-'*5}")
lapiz1.mostrar_info()
print(f"{'-'*5} Lápiz 2 {'-'*5}")
lapiz2.mostrar_info()
print(f"{'-'*5} Lápiz 3 {'-'*5}")
lapiz3.mostrar_info()

#BOLÍGARFO
boligrafo = Boligrafo("Negro","12 cm","2 mm","Artline Ergoline ")
print("")
print(f"{'-'*30} BOLÍGRAFO {'-'*30}")
boligrafo.mostrar_info()

#FUNDA CÁMARA
funda_cam = Funda_Camara("Negro","6.5 x 6.2 x 3 pulgadas","Neopreno","USA Gear")
print("")
print(f"{'-'*30} FUNDA CÁMARA {'-'*30}")
funda_cam.mostrar_info()

#CARGADOR
cargador = Cargador("Blanco","3 m","96 W","Apple")
print("")
print(f"{'-'*30} CARGADOR {'-'*30}")
cargador.mostrar_info()

#DISPARADOR FLASH
disparador_flash1 = Disparador_Flash("Negro","10x5x5 cm","100 m","Pixel King Wireless")
disparador_flash2= Disparador_Flash("Negro","10x5x5 cm","100 m","Pixel King Wireless")
print("")
print(f"{'-'*30} DISPARADOR DE FLASH {'-'*30}")
print(f"{'-'*5} Disparador 1 {'-'*5}")
disparador_flash1.mostrar_info()
print(f"{'-'*5} Disparador 2 {'-'*5}")
disparador_flash2.mostrar_info()







