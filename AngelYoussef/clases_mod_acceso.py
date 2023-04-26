#Definir una clase con modificaciones de acceso
#Los modificadores seran public y private
#si es privado tendra __, y si es publico no tendra nada 

class Cuenta:
    def __init__(self,id,cli,saldo,tipo_cuenta):
        self.__id =id
        self.cliente = cli
        self.__saldo = saldo
        self.__tipo_cuenta = tipo_cuenta

    def get_id(self):
        return self.__id[0] + "*"*5 + self.__id[-1]

    def get_saldo(self):
        return self.__saldo

    def info_cuenta(self):
        print(f"No.cuenta {self.__id} \ncliente {self.cliente} \nSaldo {self.__saldo}")

    def __secreto(self):
        print("Metodo secreto")

    def depositar(self,cantidad):
        if cantidad > 0:
            self.__saldo += cantidad

    def retirar(self,cantidad):
        if cantidad > self.__saldo:
            print("Operacion no valida")
        else:
            self.__saldo -= cantidad

#Crear mas cuentas

cta1 = Cuenta("111121","Grupo 25",500,1)
cta2 = Cuenta("22232","Grupo 24",1500,1)

cta1.depositar(500)
cta1.info_cuenta()

#Depositar lo que se tenga en la cuenta 1, en la cuenta 2
cta2.depositar(cta1.get_saldo())

print(cta1.get_id())