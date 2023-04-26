# definir una clase con modificadores de accesos
# los modificadores seran public y private

class Cuenta:
    def __init__(self,id,cli,saldo,tipo_cuenta):
        self.__id=id #lo dejamos publico
        self.cliente=cli #cuando ya se el atributo ya puedo escribr 'cliente' commpleto
        self.__saldo=saldo #privado
        self.__tipo_cuenta=tipo_cuenta

    def get_id(self):
        return self.__id[0] + "*"*5 + self.__id[-1]

    def get_saldo(self): #la palabra GET se encuentra mucho en programacion 
        return self.__saldo

    def info_cuenta(self):
        print(f"No. cuenta {self.__id}, cliente {self.cliente}, saldo{self.__saldo}")

    def __secreto(self): #cueando alguien haga una cuenta no lo puede ver el usuario
        print("metodo secreto")

    def depositar(self,cantidad):
        if cantidad>0:
            self.__saldo+=cantidad

    def retirar(self,cantidad):
        if cantidad>self.__saldo:
            print("Operacion no valida")

        else:
            self.__saldo-=cantidad
            

#para no hacer otro archivo, crear el otro codigo aqui 
#crear unas cuentas
cta1=Cuenta("111122","Grupo 25",500,1)
cta2=Cuenta("222225","Grupo 24",1500,1)

cta1.depositar(500)
cta1.info_cuenta()

#depositar lo que se tenga en la cta1, en la cta2
cta2.depositar(cta1.get_saldo())

print(cta1.get_id())