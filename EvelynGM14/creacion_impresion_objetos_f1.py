from clasesfoto1 import Boligrafo,Marcador,Cinta_Adhesiva,Retrato,Esmalte,Espejo,Pinza,Brillo_labial,Cuaderno,Regla,Pegamento,Diario,Lapicero,Telefono,Tijeras,Paleta_sombras,Poster,Pulsera,Nota_adhesiva,Tarjeta

print("*"*50)
print("Estos son los bolígrafos")
print("*"*50)

boligrafo1 = Boligrafo("Rosa",15.3,12,"Bic")
boligrafo2 = Boligrafo("Azul",15.3,12,"Bic")
boligrafo3 = Boligrafo("Amarillo",15.3,12,"Bic")
boligrafo4 = Boligrafo("Rojo",15.3,12,"Bic")

boligrafo1.info()
boligrafo2.info()
boligrafo3.info()
boligrafo4.info()

print("*"*50)
print("Estos son los marcadores")
print("*"*50)

marcador1 = Marcador("Morado",13,20,"Crayola")
marcador2 = Marcador("Rosa",13,20,"Crayola")
marcador3 = Marcador("Naranja",13,20,"Crayola")

marcador1.info()
marcador2.info()
marcador3.info()

print("*"*50)
print("Estas son las cintas adhesivas")
print("*"*50)

cinta1 = Cinta_Adhesiva("Lila","1cm","2mts","Tuk")
cinta2 = Cinta_Adhesiva("Rosa","1cm","2mts","Tuk")
cinta3 = Cinta_Adhesiva("Verde","1cm","2mts","Tuk")
cinta4 = Cinta_Adhesiva("Azul","1cm","2mts","Tuk")

cinta1.info()
cinta2.info()
cinta3.info()

print("*"*50)
print("Estos son los portaretratos")
print("*"*50)

retrato1 = Retrato("20cm")
retrato2 = Retrato("18cm")

retrato1.info()
retrato2.info()

print("*"*50)
print("Estos son los esmaltes")
print("*"*50)

esmalte1 = Esmalte("Celeste","Bissu","Cilindrico")
esmalte2 = Esmalte("Rosa","Bissu","Cuadrado")
esmalte3 = Esmalte("Blanco","Bissu","Cilindrico")
esmalte4 = Esmalte("Con Brillos","Bissu","Rombo")
esmalte5 = Esmalte("Fiusha","Bissu","Diamante")
esmalte6 = Esmalte("Rojo","Bissu","Ovalado")
esmalte7 = Esmalte("Plateado","Bissu","Circular")

esmalte1.info()
esmalte2.info()
esmalte3.info()
esmalte4.info()
esmalte5.info()
esmalte6.info()
esmalte7.info()

print("*"*50)
print("Este es el espejo")
print("*"*50)

espejo1 = Espejo("rosa","corazón","15cm",65)

espejo1.info()

print("*"*50)
print("Estas son las pinzas")
print("*"*50)

pinza1 = Pinza("celeste","mariposa","2cm","Goody")
pinza2 = Pinza("rosa","mariposa","2cm","Goody")
pinza3 = Pinza("amarillo","mariposa","2cm","Goody")
pinza4 = Pinza("rosa claro","mariposa","2cm","Goody")
pinza5 = Pinza("fiusha","mariposa","2cm","Goody")
pinza6 = Pinza("naranja","mariposa","2cm","Goody")

pinza1.info()
pinza2.info()
pinza3.info()
pinza4.info()
pinza5.info()
pinza6.info()

print("*"*50)
print("Estos son los brillos labiales")
print("*"*50)

brillo_labial1 = Brillo_labial("rosa","Bissu","10cm",40)
brillo_labial2 = Brillo_labial("rojo","Bissu","10cm",40)
brillo_labial3 = Brillo_labial("plateado","Bissu","10cm",40)

brillo_labial1.info()
brillo_labial2.info()
brillo_labial3.info()

print("*"*50)
print("Estos son los cuadernos")
print("*"*50)

cuaderno1 = Cuaderno("rosa","22cm","80 hojas","norma")
cuaderno2 = Cuaderno("rosa claro","28cm","100 hojas","norma")

cuaderno1.info()
cuaderno2.info()

print("*"*50)
print("Esta es la regla metrica")
print("*"*50)

regla1 = Regla("rosa","30cm","triangular","aluminio")

regla1.info()

print("*"*50)
print("Este es el pegamento")
print("*"*50)

pegamento1 = Pegamento("rosa claro","14cm","Pritt",66)

pegamento1.info()

print("*"*50)
print("Este es el diario")
print("*"*50)

diario1 = Diario("celeste","24cm","100 hojas",180)

diario1.info()

print("*"*50)
print("Este es el lapicero")
print("*"*50)

lapicero1 = Lapicero("naranja","plastico",72,"Bic")

lapicero1.info()

print("*"*50)
print("Este es el telefono")
print("*"*50)

telefono1 = Telefono("salmon","Retro, con cable","24x21x12cm","Telpal")

telefono1.info()

print("*"*50)
print("Estas son las tijeras")
print("*"*50)

tijeras1 = Tijeras("celeste","13cm","Pelikan","Redondeada")

tijeras1.info()

print("*"*50)
print("Esta es la paleta de sombras")
print("*"*50)

paleta_sombras1 = Paleta_sombras("Fiusha",9,"MAC",740)

paleta_sombras1.info()

print("*"*50)
print("Estos son los posters")
print("*"*50)

poster1 = Poster("Celeste","25cm","Imagen de la playa","Papel estucado")
poster2 = Poster("Azul","18cm","Palabras repetidas","Papel estucado")

poster1.info()
poster2.info()

print("*"*50)
print("Esta es la pulsera")
print("*"*50)

pulsera1 = Pulsera("Vino,rojo,amarillo y blanco","Letras y cuentas","16cm","bisutería")

pulsera1.info()

print("*"*50)
print("Esta es la nota adhesiva")
print("*"*50)

nota1 = Nota_adhesiva("rosa claro","38x51mm","Post-It","Papel reciclado")

nota1.info()

print("*"*50)
print("Estas son las tarjetas")
print("*"*50)

tarjeta1 = Tarjeta("celeste,rosa","flores","61.5x95mm","cartón")
tarjeta2 = Tarjeta("celeste,blanco","rombos","61.5x95mm","cartón")
tarjeta3 = Tarjeta("celeste","liso","61.5x95mm","cartón")
tarjeta4 = Tarjeta("amarillo,rosa","donas","61.5x95mm","cartón")

tarjeta1.info()
tarjeta2.info()
tarjeta3.info()
tarjeta4.info()











