# definir una clase con modificadores de acceso
# los modificadores seran public y private

class Cuenta:
    def __init__(self, id, cli, saldo, tipo_cuenta):
        self.__id = id
        self.cliente = cli
        self.__saldo = saldo
        self.__tipo_cuenta = tipo_cuenta

    # get = solicitar o para poder ver
    # set = para poner 

    # metodo para poder ver el id de la cuenta pero con asteriscos
    def get_id(self):
        return self.__id[0] + "*"*5 + self.__id[-1]

    # metodo para poder visulizar el saldo de la cuenta, es necesario ya que __saldo es privado
    def get_saldo(self):
        return self.__saldo

    def info_cuenta(self):
        print(f"No. cuenta: {self.__id}\nCliente: {self.cliente}\nSaldo: {self.__saldo}")
        
    def __secreto(self):
        print("hola")

    def depositar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad
        
    def retirar (self, cantidad):
        if cantidad > self.__saldo:
            print("Operación no válida")
        else:
            self.__saldo -= cantidad

# crear cuentas
cta1 = Cuenta("77777777777", "Grupo 25", 500, 1)
cta2 = Cuenta("88888888", "Grupo 24", 1500, 1)

cta1.depositar(500)
cta1.info_cuenta()

# depositar la misma cantidad que tiene cuenta 1 a la cuenta 2
cta2.depositar(cta1.get_saldo())

print(cta1.get_id())