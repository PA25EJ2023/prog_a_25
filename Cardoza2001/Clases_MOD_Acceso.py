
class cuenta:
    def __init__(self,id,cliente,saldo,tipo_cuenta):
        self.id= id
        self.cliente= cliente
        self.__saldo= saldo
        self.__tipo_cuenta= tipo_cuenta

    def get_saldo(self):
        return self.__saldo
    
    def info_cuenta (self):
        print (f"N.Cuenta {self.id}, cliente {self.cliente}")

        
    def __secreto (self):
        print ("Metodo secreto")

    def depositar(self, cantidad):
        if cantidad >0:
            self.__saldo += cantidad    

    def retirar(self, cantidad):
        if cantidad>self.__saldo:
            print ("Operación no valida")
        else:
            self.__saldo-=cantidad


#Crear cuentas

cta1= cuenta(1111122,"Grupo 25",500, 1)
cta2= cuenta(222225,"Grupo 24",1500,1)

cta1.depositar(500)
cta1.info_cuenta()