from Clases_Foto1 import Boligrafo,Marcador,Cinta,Libreta,Esmalte_Uñas,Brillo_labial,Pinza_Pelo,Paleta_Maquillaje,Barra_Pegamento,Tijera,Regla,Lapicero_Pompon,Portaretrato,Espejo,Telefono,Pulsera,Imagen,Cuenta,Pegatina,Stiker

#BOLÍGRAFOS
boligrafo1 = Boligrafo("Rosa","12 cm","Bic","$10")
boligrafo2 = Boligrafo("Azul","12 cm","Bic","$10")
boligrafo3 = Boligrafo("Amarillo","12 cm","Bic","$10")
boligrafo4 = Boligrafo("Naranja","12 cm","Bic","$10")

print(f" {'-'*30} BOLÍGRAFOS {'-'*30} \n")
print(f"{'-'*5} Bolígrafo 1 {'-'*5}")
boligrafo1.mostrar_info()
print(f"{'-'*5} Bolígrafo 2 {'-'*5}")
boligrafo2.mostrar_info()
print(f"{'-'*5} Bolígrafo 3 {'-'*5}")
boligrafo3.mostrar_info()
print(f"{'-'*5} Bolígrafo 4 {'-'*5}")
boligrafo4.mostrar_info()

#MARCADORES
marcador1 = Marcador("Naranja","15.5 cm","Crayola","$20")
marcador2 = Marcador("Rosa","15.5 cm","Crayola","$20")
marcador3 = Marcador("Morado","15.5 cm","Crayola","$20")
print("")
print(f"{'-'*30} MARCADORES {'-'*30} \n")
print(f"{'-'*5} Marcador 1 {'-'*5}")
marcador1.mostrar_info()
print(f"{'-'*5} Marcador 2 {'-'*5}")
marcador2.mostrar_info()
print(f"{'-'*5} Marcador 3 {'-'*5}")
marcador3.mostrar_info()

#CINTAS
cinta1 = Cinta("Morado","1.50 cm","1 cm","Miniso")
cinta2 = Cinta("Rosa","1.50 cm","1 cm","Miniso")
cinta3 = Cinta("Rosa","1.50 cm","1 cm","Miniso")
cinta4 = Cinta("Verde","1.50 cm","1 cm","Miniso")
print("")
print(f"{'-'*30} CINTAS {'-'*30} \n")
print(f"{'-'*5} Cinta 1 {'-'*5}")
cinta1.mostrar_info()
print(f"{'-'*5} Cinta 2 {'-'*5}")
cinta2.mostrar_info()
print(f"{'-'*5} Cinta 3 {'-'*5}")
cinta3.mostrar_info()
print(f"{'-'*5} Cinta 4 {'-'*5}")
cinta4.mostrar_info()

#LIBRETAS
libreta1 = Libreta("Rosa","20x26 cm","100","Con resorte")
libreta2 = Libreta("Azul","20x26 cm","150","Cocida")
libreta3 = Libreta("Lila","20x26 cm","100","Con resorte")
print("")
print(f"{'-'*30} LIBRETAS {'-'*30}")
print(f"{'-'*5} Libreta 1 {'-'*5}")
libreta1.mostrar_info()
print(f"{'-'*5} Libreta 2 {'-'*5}")
libreta2.mostrar_info()
print(f"{'-'*5} Libreta 3 {'-'*5}")
libreta3.mostrar_info()

#ESMALTE_UÑAS
esmalte1 = Esmalte_Uñas("Lila","20 ml","Cilíndrica","Bissú")
esmalte2 = Esmalte_Uñas("Blanco","15 ml","Cilíndrica","Bissú")
esmalte3 = Esmalte_Uñas("Brillos Rosas","15 ml","Circular","Bissú")
esmalte4 = Esmalte_Uñas("Rosa","9 ml","Cuadrada","Bissú")
esmalte5 = Esmalte_Uñas("Rosa Fuerte","15 ml","Diamante","Bissú")
esmalte6 = Esmalte_Uñas("Rojo","17 ml","Ovalada","Bissú")
esmalte7 = Esmalte_Uñas("Dorado","10 ml","Cilíndrica","Bissú")
print("")
print(f"{'-'*30} ESMALTES PARA UÑAS {'-'*30}")
print(f"{'-'*5} Esmalte para Uñas 1 {'-'*5}")
esmalte1.mostrar_info()
print(f"{'-'*5} Esmalte para Uñas 2 {'-'*5}")
esmalte2.mostrar_info()
print(f"{'-'*5} Esmalte para Uñas 3 {'-'*5}")
esmalte3.mostrar_info()
print(f"{'-'*5} Esmalte para Uñas 4 {'-'*5}")
esmalte4.mostrar_info()
print(f"{'-'*5} Esmalte para Uñas 5 {'-'*5}")
esmalte5.mostrar_info()
print(f"{'-'*5} Esmalte para Uñas 6 {'-'*5}")
esmalte6.mostrar_info()
print(f"{'-'*5} Esmalte para Uñas 7 {'-'*5}")
esmalte7.mostrar_info()

#BRILLO_LABIAL
brillo1 = Brillo_labial("Rosa","15 g","Cilíndrica"," L’Oréal")
brillo2 = Brillo_labial("Rojo","15 g","Cilíndrica"," L’Oréal")
brillo3 = Brillo_labial("Blanco","15 g","Cilíndrica"," L’Oréal")
print("")
print(f"{'-'*30} BRILLO PARA LABIOS {'-'*30}")
print(f"{'-'*5} Brillo 1 {'-'*5}")
brillo1.mostrar_info()
print(f"{'-'*5} Brillo 2 {'-'*5}")
brillo2.mostrar_info()
print(f"{'-'*5} Brillo 3 {'-'*5}")
brillo3.mostrar_info()

#PINZA_PELO
pinza1 = Pinza_Pelo("Rosa","2x2 cm","Plástico","Ormromra")
pinza2 = Pinza_Pelo("Azul","2x2 cm","Plástico","Ormromra")
pinza3 = Pinza_Pelo("Rosa","2x2 cm","Plástico","Ormromra")
pinza4 = Pinza_Pelo("Amarillo","2x2 cm","Plástico","Ormromra")
pinza5 = Pinza_Pelo("Naranja","2x2 cm","Plástico","Ormromra")
pinza6 = Pinza_Pelo("Morado","2x2 cm","Plástico","Ormromra")
pinza7 = Pinza_Pelo("Salmón","2x2 cm","Plástico","Ormromra")
print("")
print(f"{'-'*30} PINZAS PARA EL PELO {'-'*30}")
print(f"{'-'*5} Pinza 1 {'-'*5}")
pinza1.mostrar_info()
print(f"{'-'*5} Pinza 2 {'-'*5}")
pinza2.mostrar_info()
print(f"{'-'*5} Pinza 3 {'-'*5}")
pinza3.mostrar_info()
print(f"{'-'*5} Pinza 4 {'-'*5}")
pinza4.mostrar_info()
print(f"{'-'*5} Pinza 5 {'-'*5}")
pinza5.mostrar_info()
print(f"{'-'*5} Pinza 6 {'-'*5}")
pinza6.mostrar_info()
print(f"{'-'*5} Pinza 7 {'-'*5}")
pinza7.mostrar_info()

#PALETA_MAQUILLAJE
paleta_maquillaje = Paleta_Maquillaje("Multicolor","10x10 cm","34 g","Bissú")
print("")
print(f"{'-'*30} PALETA DE MAQUILLAJE {'-'*30}")
paleta_maquillaje.mostrar_info()

#BARRA_PEGAMENTO
barra_pegamento = Barra_Pegamento("Rosa","12x2 cm","43 g","Pritt")
print("")
print(f"{'-'*30} BARRA DE PEGAMENTO {'-'*30}")
barra_pegamento.mostrar_info()

#TIJERA
tijera = Tijera("Azul","15 cm","Dos cuchillas de acero y plástico","Barrilito")
print("")
print(f"{'-'*30} TIJERA {'-'*30}")
tijera.mostrar_info()

#REGLA
regla = Regla("Morado","30 cm","Plástico","Maped")
print("")
print(f"{'-'*30} REGLA {'-'*30}")
regla.mostrar_info()

#LAPICERO CON POMPÓN
lapicerp_pom= Lapicero_Pompon("Naranja","14 cm","5 cm","Paper Mate")
print("")
print(f"{'-'*30} LAPICERO CON POMPÓN {'-'*30}")
lapicerp_pom.mostrar_info()

#PORTARETRATOS
portaretrato1 = Portaretrato("Blanco","20x13 cm","Madera","17x10 cm")
portaretrato2 = Portaretrato("Blanco","20x13 cm","Madera","17x10 cm")
print("")
print(f"{'-'*30} PORTARETRATOS {'-'*30}")
print(f"{'-'*5} Portaretato 1{'-'*5}")
portaretrato1.mostrar_info()
print(f"{'-'*5} Portaretato 2{'-'*5}")
portaretrato2.mostrar_info()

#ESPEJO
espejo = Espejo("Rosa","25 cm","Plástico","Corazón")
print("")
print(f"{'-'*30} ESPEJO{'-'*30}")
espejo.mostrar_info()

#TELEFONO
telefono = Telefono("Rosa","23x20x12 cm","Máximo 60cm","Plástico","GPO")
print("")
print(f"{'-'*30} TELÉFONO {'-'*30}")
telefono.mostrar_info()

#PULCERA
pulcera = Pulsera("Blanco, Amarillo, Rojo, Negro y Vino","12 cm","Circular y Cuadrada","Color sólido y Letras")
print("")
print(f"{'-'*30} PULCERA {'-'*30}")
pulcera.mostrar_info()

#IMAGEN
imagen1 = Imagen("Azul, rosa, blanco y negro","Telefono","10x7 cm","Papel Bond")
imagen2 = Imagen("Blanco y lila","Una oración repetida","14x15 cm","Papel Bond")
imagen3 = Imagen("Café","Persona posando","18x14 cm","Papel")
imagen4 = Imagen("Azul, celeste, café y blanco","Personas en la playa","24x19 cm","Papel Bond")
print("")
print(f"{'-'*30} IMÁGENES {'-'*30}")
print(f"{'-'*5} Imágen 1 {'-'*5}")
imagen1.mostrar_info()
print(f"{'-'*5} Imágen 2 {'-'*5}")
imagen2.mostrar_info()
print(f"{'-'*5} Imágen 3 {'-'*5}")
imagen3.mostrar_info()
print(f"{'-'*5} Imágen 4 {'-'*5}")
imagen4.mostrar_info()

#CUENTAS
cuentas1 = Cuenta("Verde","5 mm","6","Plástico")
cuentas2 = Cuenta("Blanco","5 mm","2","Plástico")
cuentas3 = Cuenta("Salmón","5 mm","4","Plástico")
cuentas4 = Cuenta("Rosa claro","5 mm","5","Plástico")
cuentas5 = Cuenta("Rosa fuerte","5 mm","2","Plástico")
cuentas6 = Cuenta("Menta","5 mm","2","Plástico")
print("")
print(f"{'-'*30} CUENTAS {'-'*30}")
print(f"{'-'*5} Grupo de Cuentas 1 {'-'*5}")
cuentas1.mostrar_info()
print(f"{'-'*5} Grupo de Cuentas 2 {'-'*5}")
cuentas2.mostrar_info()
print(f"{'-'*5} Grupo de Cuentas 3 {'-'*5}")
cuentas3.mostrar_info()
print(f"{'-'*5} Grupo de Cuentas 4 {'-'*5}")
cuentas4.mostrar_info()
print(f"{'-'*5} Grupo de Cuentas 5 {'-'*5}")
cuentas5.mostrar_info()
print(f"{'-'*5} Grupo de Cuentas 6 {'-'*5}")
cuentas6.mostrar_info()

#PEGATINAS
pegatina1 = Pegatina("Azul","Estrella","1 cm","11")
pegatina2 = Pegatina("Lila","Circular","1 cm","7")
pegatina3 = Pegatina("Rosa","Flores","1 cm","14")
pegatina4 = Pegatina("Blanco","Estrellas","1 cm","11")
pegatina5 = Pegatina("Naranja","Corazón","1 cm","1")
pegatina4 = Pegatina("Blanco","Luna","1 cm","4")
print("")
print(f"{'-'*30} PEGATINAS {'-'*30}")
print(f"{'-'*5} Grupo de Pegatinas 1 {'-'*5}")
pegatina1.mostrar_info()
print(f"{'-'*5} Grupo de Pegatinas 2 {'-'*5}")
pegatina2.mostrar_info()
print(f"{'-'*5} Grupo de Pegatinas 3 {'-'*5}")
pegatina3.mostrar_info()
print(f"{'-'*5} Grupo de Pegatinas 4 {'-'*5}")
pegatina4.mostrar_info()

#STIKERS
stiker1 = Stiker("Dorado","Estrellas","2 cm","10","Hoja")
stiker2 = Stiker("Dorado","Corazones","2 cm","8","Hoja")
print("")
print(f"{'-'*30} STIKERS {'-'*30}")
print(f"{'-'*5} Grupo de Stikers 1 {'-'*5}")
stiker1.mostrar_info()
print(f"{'-'*5} Grupo de Stikers 2 {'-'*5}")
stiker2.mostrar_info()


