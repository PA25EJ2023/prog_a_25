

class Cuenta:
    def __init__(self,id,cli,saldo,tipo_cuenta):
        self.__id =id
        self.cliente = cli
        self.__saldo =saldo
        self.__tipo_cuenta= tipo_cuenta


    def info_cuenta(self):
        print(f"No.cuenta {self.__id},cliente {self.cliente}")

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

    def get_saldo(self):
        return self.__saldo
    
    def get_id(self):
        return self.__id[0]+"***" + self.__id[-1]

    


#crear unas cuentas

cta1 = Cuenta(1111111,"Grupo 25",500,1)
cta2 = Cuenta(2,"Grupo 24",1500,1)

cta1.depositar(500)
cta1.retirar(1000)
cta1.info_cuenta()

#depositar lo que se tenga en la cuenta 1 a la 2
cta1.depositar(cta1.get_saldo())
print(cta1.get_id)

