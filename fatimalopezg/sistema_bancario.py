# Escribir un programa que simule un sistema bancario, el prog debe tener el sig menu:
# 1. Crear cuenta
# 2. Mostrar info cuenta
# 3. Mostrar todas las cuentas
# 4. Salir
# Para crear una cuenta solicitar num de cuenta, nombre del cliente y saldo inicial
# -- puedo usar while, se ocupa una lista para ir metiendo las cuentas
# -- EL OBJETIVO ES USAR POO

class Cuenta:
    def __init__(self,num_cuenta,nombre_cliente,saldo_ini):
        self.num_cuenta=num_cuenta
        self.nombre_cliente=nombre_cliente
        self.saldo_ini=saldo_ini

    def mostrar_info_cuenta(self):
        print(f"Numero de cuenta: {self.num_cuenta}")
        print(f"Nombre cliente {self.nombre_cliente}")
        print(f"Saldo inicial: {self.saldo_ini}")
        

#from sistema_bancario import Cuenta
cuentas=[] #crear lista vacia
print(" **** SISTEMA BANCARIO ****") 
while True:
    print("1. Crear cuenta")
    print("2. Mostrar info cuenta")
    print("3. Mostrar todas las cuentas")
    print("4. Salir")
    opcion=int(input("Buen día, ¿qué movimiento desea realizar? "))

    if opcion==1:
        num_cuenta=int(input("Ingrese su numero de cuenta: "))
        nombre_cliente=input("Ingrese su nombre completo: ")
        saldo_ini=float(input("Ingrese su saldo inicial: "))
    
        objeto=Cuenta(num_cuenta,nombre_cliente,saldo_ini)
        cuentas.append(objeto)
        #print(f"Su cuenta fue creado con los sig datos: {objeto.crear_cuenta}")

    elif opcion==2:
        num_cuenta=int(input("Ingrese numero de cuenta de quien desea obtener información: "))
        for objeto in cuentas:
            if objeto.num_cuenta==num_cuenta: #para que solo muestre la info de esa cuenta en especifico
                objeto.mostrar_info_cuenta()

    elif opcion==3:
        print("Total cuentas creadas")
        for objeto in cuentas:
            objeto.mostrar_info_cuenta()

    elif opcion==4:
        print("Saliste del programa")
        break #para finalizar el ciclo while
    
   