def imprimir_datos(nombres, generos, legajos, calificaciones):
    for i in range(len(nombres)):
        imprimir_dato(nombres[i], generos[i], legajos[i], calificaciones[i])  

def imprimir_dato(nombre: str, genero: str, legajo: int, calificaciones: list) -> None:
    print(f"{nombre}\t{genero}\t{legajo}\t{calificaciones}")


def buscar_datos(legajo_buscado: int, legajos: list) -> int:
    for index in range(len(legajos)):
        if legajos[index] == legajo_buscado:
            return index
    return -1  # no encontrado

def encontrar_dato(nombres: list, generos: list, legajos: list, calificaciones: list) -> None:
    while True:
        legajo_ingresado = int(input("Ingrese el numero de legajo a buscar: "))
        indice = buscar_datos(legajo_ingresado, legajos)

        if indice == -1:
            print("Legajo inexistente.")
        else:
            print("\nNOMBRE\t\tGENERO\tLEGAJO\t\tCALIFICACIONES")
            print(f"{nombres[indice]}\t\t{generos[indice]}\t{legajos[indice]}\t\t{calificaciones[indice]}")

        continuar = input("¿Desea buscar otro estudiante? (si/no): ")
        if continuar == "no":
            break
