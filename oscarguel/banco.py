def Crear_cuenta():
    

    pass






print("BIENVENIDO AL BANCO")
print("OPCIONES")
print("1.Crear cuenta\n2.Mostrar informacion de cuenta\n3.Mostrar todas las cuentas\n4.Salir")
opcion=int(input("Elige una opcion 1-2-3-4:"))


if opcion ==1 :
    nom_cliente= str(input("Ingrese su nombre:"))
    num_cuenta= int(input("Ingrese numero de cuenta:"))
    sal_inicial= int(input("Ingrese monto del saldo inicial:"))
    cuenta= nom_cliente + num_cuenta + sal_inicial
    print ("tu cuenta es:" ,cuenta )
if opcion == 2:
    cuenta= int(input("Cual es la cuenta de donde desea otener la informacion "))


    pass

if opcion ==3:

    pass
