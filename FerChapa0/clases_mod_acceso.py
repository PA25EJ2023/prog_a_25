#definir una calse con modificaciones de acceso
#los modificadores de acceso seran public y privado

class Cuenta:
    def __init__(self, id, cli, saldo, tipo_cuenta,):
        self._id = id
        self.cliente = cli
        self._saldo = saldo
        self._tipo_cuenta = tipo_cuenta
    
    def get_id(self):
        return self._id[0]+'***'*5 + self._id[-1]
    def get_saldo(self):
        return self._saldo    

    def info_cuenta(self):
        print(f'No.cuenta {self._id}, cliente {self.cliente}, saldo {self._saldo}')

    def __secreto(self):
        print("Metodo secreto")
    
    def depositar(self, cantidad):
        if cantidad>0:
            self._saldo+= cantidad

    def retirar(self, cantidad):
        if cantidad>self._saldo:
            print("operacion no valida")
        else:
            self._saldo-=cantidad

#crear cuentas
cta1 = Cuenta("121455464843843878514548","Grupo 25",500,1)
cta2 = Cuenta("115486434531356584846846","Grupo 24",1500,1)

cta1.depositar(500)
cta1.info_cuenta()
#depositar lo que tenga la cuenta 1 en la cuenta 2
cta2.depositar(cta1.get_saldo())
cta2.info_cuenta()

print(cta1.get_id())