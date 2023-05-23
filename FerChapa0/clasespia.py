class Frases:
    def __init__(self):
        self.frases = {}

    def agregar_frase(self):
        id_frase = input("Ingrese el ID de la frase: ")
        if id_frase in self.frases:
            print("El ID de la frase ya está en uso.")
            return

        texto_frase = input("Ingrese el texto de la frase: ")
        autor = input("Ingrese el autor de la frase: ")
        stars_calif = []

        self.frases[id_frase] = {
            "texto": texto_frase,
            "autor": autor,
            "calificaciones": stars_calif
        }

        print("Frase agregada correctamente.")

    def ver_frase(self):
        id_frase = input("Ingrese el ID de la frase: ")
        if id_frase not in self.frases:
            print("La frase no existe.")
            return

        frase = self.frases[id_frase]
        calificaciones = frase["calificaciones"]

        print("Texto: ", frase["texto"])
        print("Autor: ", frase["autor"])
        print("Calificaciones totales: ", len(calificaciones))

        if len(calificaciones) > 0:
            promedio = sum(calificaciones) / len(calificaciones)
            print("Promedio de calificaciones: ", promedio)

            for i in range(1, 6):
                count = calificaciones.count(i)
                percentage = (count / len(calificaciones)) * 100
                print("Calificaciones de", i, "estrellas: ", percentage, "%")

        calificar = input("¿Desea calificar esta frase? (s/n): ")
        if calificar.lower() == "s":
            calificacion = int(input("Ingrese su calificación (1-5 estrellas): "))
            if calificacion >= 1 and calificacion <= 5:
                calificaciones.append(calificacion)
                print("Calificación agregada correctamente.")
            else:
                print("La calificación debe estar entre 1 y 5 estrellas.")

    def ver_frases(self):
        if len(self.frases) == 0:
            print("No hay frases registradas.")
            return

        for id_frase, frase in self.frases.items():
            print("ID: ", id_frase)
            print("Texto: ", frase["texto"])
            print("Autor: ", frase["autor"])
            print("")

    def eliminar_frase(self):
        id_frase = input("Ingrese el ID de la frase a eliminar: ")
        if id_frase not in self.frases:
            print("La frase no existe.")
            return

        del self.frases[id_frase]
        print("Frase eliminada correctamente.")

    def modificar_frase(self):
        id_frase = input("Ingrese el ID de la frase a modificar: ")
        if id_frase not in self.frases:
            print("La frase no existe.")
            return

        frase = self.frases[id_frase]
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
        try:
            with open("frases.txt", "r") as archivo:
                for linea in archivo:
                    linea = linea.strip()
                    if linea:
                        id_frase, texto, autor = linea.split(",")
                        self.frases[id_frase] = {
                            "texto": texto,
                            "autor": autor,
                            "calificaciones": []
                        }
            print("Frases cargadas correctamente desde el archivo.")
        except FileNotFoundError:
            print("No se encontró el archivo 'frases.txt'.")
