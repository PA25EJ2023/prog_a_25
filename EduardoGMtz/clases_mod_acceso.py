# Definir  una clase con modificaciones de acceso
# Las modificaciones serán public y private

class Cuenta:
    def __init__(self, id, cli, saldo, tipo_cuenta):
        self.__id = id
        self.cliente = cli
        self.__saldo = saldo
        self.__tipo_cuenta = tipo_cuenta

    def get_id(self):
        return self.__id[0] + "*"*5 + self.__id[-1]
 
    def get_saldo(self):
        return self.__saldo

    def info_Cuenta(self):
        print(f"No. Cuenta {self.__id}, cliente {self.cliente}, saldo: {self.__saldo}")

    def __secreto(self):
        print("metodo secreto")

    def depositar(self,cantidad):
        if cantidad > 0:
            self.__saldo += cantidad

    def retirar(self,cantidad):
        if cantidad > self.__saldo:
            print("Operación no valida")
        else: 
            self.__saldo -= cantidad
# Crear unas cuentas

cta1 = Cuenta("1234567891011121","Grupo 25",500,1)
cta2 = Cuenta("2345678910111213","Grupo 24",1500,1)

cta1.depositar(500)
cta1.info_Cuenta()

# Depositar lo que se tenga en la cuenta 1, en la cuenta 2

cta2.depositar( cta1.get_saldo() )

print(cta1.get_id())