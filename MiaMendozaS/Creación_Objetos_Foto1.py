from Clases_Foto1 import Boligrafo,Marcador,Cinta

#BOLÍGRAFOS
boligrafo1 = Boligrafo("12 cm","Rosa","Bic","$10")
boligrafo2 = Boligrafo("12 cm","Azul","Bic","$10")
boligrafo3 = Boligrafo("12 cm","Amarillo","Bic","$10")
boligrafo4 = Boligrafo("12 cm","Naranja","Bic","$10")

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
marcador1 = Marcador("15.5 cm","Naranja","Crayola","$20")
marcador2 = Marcador("15.5 cm","Rosa","Crayola","$20")
marcador3 = Marcador("15.5 cm","Morado","Crayola","$20")
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
cinta3 = Cinta("Verde","1.50 cm","1 cm","Miniso")
print("")
print(f"{'-'*30} CINTAS {'-'*30} \n")
print(f"{'-'*5} Cinta 1 {'-'*5}")
cinta1.mostrar_info()
print(f"{'-'*5} Cinta 2 {'-'*5}")
cinta2.mostrar_info()
print(f"{'-'*5} Cinta 3 {'-'*5}")
cinta3.mostrar_info()






