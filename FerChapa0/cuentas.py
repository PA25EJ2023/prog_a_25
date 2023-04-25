def crear_cuenta(ncuenta,nombre,saldo):
    cuentapersonal.append(ncuenta)
    cuentapersonal.append(nombre)
    cuentapersonal.append(saldo)
    return cuentapersonal
def mostrar_cuenta(bcuenta,cuentas):
    for cuenta in cuentas:
            if bcuenta == bcuenta:
                print (cuenta)
            break
        
def todas_cuentas(cuentas):
    return cuentas
op=1
cuentapersonal=[]
cuentas=[]
while op<4:   
     
    print("Bienvenido al Banco")
    print("Opciones disponibles")
    op=int(input("1.Crear Cuenta\n2.Mostrar informacion de una cuenta\n3.Mostrar todas las cuentas\n4.Salir: "))
    if op==1:
        ncuenta=int(input("Deme su numero de cuenta: "))
        nombre=input("Deme su nombre: ")
        saldo=float(input("Deme su saldo inicial: "))
        cuentap=crear_cuenta(ncuenta,nombre,saldo)
        cuentas.append(cuentap) 
        
    elif op==2:
        bcuenta=int(input("Cual es su numero de cuenta: "))
        mostrar_cuenta(bcuenta,cuentas)
    elif op == 3:
        todas=todas_cuentas(cuentas)
        print(f'Las cuentas guardadas son: {todas}')


