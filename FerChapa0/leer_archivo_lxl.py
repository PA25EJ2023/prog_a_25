archivo=open('datos.txt','r',encoding='utf8')
for linea in archivo:
	print(linea,end="")

archivo.close

