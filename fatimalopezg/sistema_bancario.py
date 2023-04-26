# Escribir un programa que simule un sistema bancario, el prog debe tener el sig menu:
# 1. Crear cuenta
# 2. Mostrar info cuenta
# 3. Mostrar todas las cuentas
# 4. Salir
# Para crear una cuenta solicitar num de cuenta, nombre del cliente y saldo inicial
# puedo usar while, se ocupa una lista para ir metiendo las cuentas
#EL OBJETIVO ES USAR POO


class Cuentas:
#lista=[]
    def __init__(self,num_cuenta,nombre_cliente,saldo_ini):
        self.num_cuenta=num_cuenta
        self.nombre_cliente=nombre_cliente
        self.saldo_ini=saldo_ini

    def crear_cuenta(self):
        return num_cuenta,nombre_cliente,saldo_ini

    def mostar_info_cuenta(self):
        pass

    def mostrar_cuentas(self):
        for i in crear_cuenta:
            return crear_cuenta


#from sistema_bancario import Cuentas

print("SISTEMA BANCARIO") *50
print("1. Crear cuenta")
print("2. Mostrar info cuenta")
print("3. Mostrar todas las cuentas")
print("4. Salir")
opciones=int(input("¿Qué desea realizar?"))


if opcion==1:
    num_cuenta=input("Ingrese su numero de cuenta: ")
    nombre_cliente=input("Ingrese su nombre completo: ")
    saldo_ini=float(input("Ingrese su saldo inicial: ")
    objeto=Cuentas(num_cuenta,nombre_cliente,saldo_ini)
    print(f"Su cuenta fue creado con los sig datos: {objeto.crear_cuenta}")


"""elif opcion==2:
    print(f"Numero de cuenta {num_cuenta}")
    print(f"Nombre: {nombre_cliente}")
    print(f"Saldo inicial: {saldo_ini}")
    objeto==Cuentas(num_cuenta,nombre_cliente,saldo_ini)"""


#elif opcion==3:


elif opcion==4:
    print("Salir del programa")