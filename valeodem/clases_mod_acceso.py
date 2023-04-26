#Definir una clase con modificaciones de acceso 
#Los modificadores seran public y private

class Cuenta: 
    def __init__(self,id,cli,saldo,tipo_cuenta):
        self.id = id
        self.cliente = cli
        self.__saldo = saldo
        self.__tipo_cuenta = tipo_cuenta

    def get_id(self):
        return self.__id[0] + "*"*5 + self.__id[-1]
    
    def get_saldo(self):
        return self.__saldo
   
    def info_cuenta(self):
        print(f"No.cuenta: {self.id}, cliente: {self.cliente}, saldo: {self.__saldo}")

    def __secreto(self):
        print("metodo secreto")

    def depositar(self,cantidad):
        self.__saldo += cantidad

    def retirar(self, cantidad):
        if cantidad > self.__saldo: 
            print("operacion no valida")
        else:
            self.__saldo -= cantidad
    

#crear cuentas

cta1 = Cuenta(1237267262711,"Grupo 25",500,1)
cta2 = Cuenta(2,"Grupo 24",1500,1)

cta1.depositar(500)
cta1.info_cuenta()

#depositar lo que tenga cuenta 1 en cuenta 2
cta2.depositar(cta1.get_saldo())

print(cta1.get_id())


       