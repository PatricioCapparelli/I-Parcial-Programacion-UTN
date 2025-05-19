def imprimir_datos(nombres, generos, legajos, calificaciones):
    """Muestra los datos de estudiantes en formato de tabla dependiendo de su indices.
    
    Args:
        nombres(list): Lista de nombres
        generos(list): Lista de generos
        legajos(list): Lista de legajos 
        calificaciones(list): Lista de listas con notas
    """
    print("NOMBRE\t\tGENERO\tLEGAJO\tCALIFICACIONES")
    for i in range(len(nombres)):
        if len(nombres[i]) > 7:
            print(f"{nombres[i]}\t{generos[i]}\t{legajos[i]}\t{calificaciones[i]}")
        else:
            print(f"{nombres[i]}\t\t{generos[i]}\t{legajos[i]}\t{calificaciones[i]}")

def imprimir_dato(nombre: str, genero: str, legajo: int, calificaciones: list) -> None:
    """Imprime los datos de un estudiante.
    
    Args:
        nombre(str): Nombre del estudiante
        genero(str): Genero del estudiante (F/M/X)
        legajo(int): Numero de legajo
        calificaciones(list): Lista de calificaciones
    """
    print(f"{nombre}\t{genero}\t{legajo}\t{calificaciones}")


def buscar_legajo(legajo_buscado: int, legajos: list) -> int:
    """Busca un legajo en la lista y devuelve el estudiante.
    
    Args:
        legajo_buscado(int): Legajo ingresado a buscar
        legajos(list): Lista de legajos
        
    Returns:
        int: Indice del legajo o -1 si no existe.
    """
    legajo_encontrado = -1
    for index in range(len(legajos)):
        if legajos[index] == legajo_buscado:
            legajo_encontrado = index
    return legajo_encontrado 

def encontrar_legajos(nombres: list, generos: list, legajos: list, promedios:list, calificaciones: list) -> None:
    """Busca y muestra datos de un estudiante por su legajo.
    
    Args:
        nombres(list): Lista de nombres
        generos(list): Lista de generos
        legajos(list): Lista de legajos
        calificaciones(list): Lista de calificaciones
    """
    legajo_ingresado = int(input("Ingrese el número de legajo a buscar: "))
    encontrados = 0

    print("\nNOMBRE\t\tGENERO\tLEGAJO\tPROMEDIO\tCALIFICACIONES")
    for i in range(len(legajos)):
        if legajos[i] == legajo_ingresado:
            if len(nombres[i]) > 7:
                print(f"{nombres[i]}\t{generos[i]}\t{legajos[i]}\t{promedios[i]}\t{calificaciones[i]}")
            else:
                print(f"{nombres[i]}\t\t{generos[i]}\t{legajos[i]}\t{promedios[i]}\t\t{calificaciones[i]}")
            encontrados += 1

    if encontrados == 0:
        print("Legajo inexistente.")

