import os

class Frases:
    def __init__(self):
        self.frases = {}

    def agregar_frase(self):
        id_frase = input("Ingrese el ID de la frase: ")
        if id_frase in self.frases:
            print("El ID de la frase ya está en uso.")
            return

        texto = input("Ingrese el texto de la frase: ")
        autor = input("Ingrese el autor de la frase: ")

        self.frases[id_frase] = {
            "texto": texto,
            "autor": autor,
            "calificaciones": []
        }

        print("Frase agregada correctamente.")

    def ver_frase(self):
        id_frase = input("Ingrese el ID de la frase: ")
        if id_frase not in self.frases:
            print("El ID de la frase no existe.")
            return

        frase = self.frases[id_frase]
        print("Texto:", frase["texto"])
        print("Autor:", frase["autor"])
        self.mostrar_calificaciones(frase["calificaciones"])

        opcion = input("¿Desea calificar esta frase? (s/n): ")
        if opcion.lower() == "s":
            calificacion = int(input("Ingrese su calificación (1-5 estrellas): "))
            if calificacion < 1 or calificacion > 5:
                print("Calificación inválida.")
            else:
                frase["calificaciones"].append(calificacion)
                print("Calificación agregada correctamente.")

    def mostrar_calificaciones(self, calificaciones):
        total_calificaciones = len(calificaciones)
        promedio = 0.0

        if total_calificaciones > 0:
            promedio = sum(calificaciones) / total_calificaciones

        print("Total de calificaciones:", total_calificaciones)
        print("Promedio de calificaciones:", promedio)

        for estrella in range(1, 6):
            cantidad = calificaciones.count(estrella)

            if total_calificaciones > 0:
                porcentaje = cantidad / total_calificaciones * 100
            else:
                porcentaje = 0.0

            print(f"Calificaciones de {estrella} estrellas: {cantidad} ({porcentaje:.2f}%)")

    def ver_frases(self):
        if not self.frases:
            print("No hay frases registradas.")
            return

        print("Frases registradas:")
        for id_frase, frase in self.frases.items():
            print(f"ID: {id_frase} - Autor: {frase['autor']}")

    def eliminar_frase(self):
        id_frase = input("Ingrese el ID de la frase a eliminar: ")
        if id_frase not in self.frases:
            print("El ID de la frase no existe.")
            return

        del self.frases[id_frase]
        print("Frase eliminada correctamente.")

    def modificar_frase(self):
        id_frase = input("Ingrese el ID de la frase a modificar: ")
        if id_frase not in self.frases:
            print("El ID de la frase no existe.")
            return

        frase = self.frases[id_frase]
        print("Frase actual:")
        print("Texto:", frase["texto"])
        print("Autor:", frase["autor"])

        nuevo_texto = input("Ingrese el nuevo texto de la frase: ")
        nuevo_autor = input("Ingrese el nuevo autor de la frase: ")

        frase["texto"] = nuevo_texto
        frase["autor"] = nuevo_autor

        print("Frase modificada correctamente.")

    def guardar_frases_archivo(self):
        with open("frases.txt", "w") as archivo:
            for id_frase, frase in self.frases.items():
                archivo.write(f"{id_frase},{frase['texto']},{frase['autor']}\n")

    def cargar_frases_archivo(self):
        self.frases = {}
        archivo_existente = os.path.isfile("frases.txt")

        if not archivo_existente:
            print("No se encontró el archivo 'frases.txt'. Se creará un nuevo archivo.")
            with open("frases.txt", "w") as archivo:
                pass
            return

        with open("frases.txt", "r") as archivo:
            for linea in archivo:
                linea = linea.strip()
                if linea:
                    partes = linea.split(",")
                    if len(partes) == 3:
                        id_frase, texto, autor = partes
                        self.frases[id_frase] = {
                            "texto": texto,
                            "autor": autor,
                            "calificaciones": []
                        }
                    else:
                        print("Error: línea inválida en el archivo 'frases.txt'.")

        print("Frases cargadas correctamente desde el archivo.")

    def mostrar_menu(self):
        print("1.- Agregar Frase")
        print("2.- Ver Frase")
        print("3.- Ver Frases")
        print("4.- Eliminar Frase")
        print("5.- Modificar frase")
        print("6.- Salir")

frases = Frases()
frases.cargar_frases_archivo()

while True:
    frases.mostrar_menu()
    opcion = input("Ingrese una opción: ")

    if opcion == "1":
        frases.agregar_frase()
    elif opcion == "2":
        frases.ver_frase()
    elif opcion == "3":
        frases.ver_frases()
    elif opcion == "4":
        frases.eliminar_frase()
    elif opcion == "5":
        frases.modificar_frase()
    elif opcion == "6":
        frases.guardar_frases_archivo()
        print("¡Hasta luego!")
        break
    else:
        print("Opción inválida. Por favor, ingrese una opción válida.")