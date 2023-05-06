from clasesfoto2 import Revista, Portafolio, Zapatos, Laptop, Flash, Tripie
from clasesfoto2 import Celular, Pila, Reloj, Camisa, Lente_camara, Protector
from clasesfoto2 import Estuche_camara, Marcador, Lapices, Cargador_lap

revista1 = Revista("Juice","Jovenes",80)
print("Revista ")
revista1.info()

portafolio = Portafolio("Cafe", "Grande", 2400)
print("Portafolio ")
portafolio.info()

zapatos = Zapatos("Guess", "Veish", "Piel")
print("Zapatos ")
portafolio.info()

laptop = Laptop("Appel","Macbook","Plateada",15000)
print("Laptop")
laptop.info()

flash1 = Flash("Canon", "negro", "Retractil", 1700)
print("Flash 1")
flash1.info()

flash2 = Flash("Canon", "negro", "Retractil", 1700)
print("Flash 2")
flash2.info()

tripie = Tripie("RabbitStorm", "Negro", "125cm", 400)
print("Tripie ")
tripie.info()

celular = Celular("Bmobile", "AX687", "Azul", 700)
print("Celular ")
celular.info()

pila = Pila("Power bank","Recargable","Negro",500)
print("Pila del Celular")
pila.info()

