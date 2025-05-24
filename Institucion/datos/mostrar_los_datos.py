from validaciones.validar_legajos import validar_legajo_a_buscar
from utilidades.impresiones.imprimir_datos import mostrar_estudiantes_con_promedio

def devolver_indice_legajo(legajo_a_buscar: int, legajos: list) -> int:
    indice = -1
    for i in range(len(legajos)):
        if legajos[i] == legajo_a_buscar and indice == -1:
            indice = i
    return indice

def buscar_legajo(nombres: list, generos: list, legajos: list, promedios: list, calificaciones: list):
    """Busca un legajo en la lista y devuelve el estudiante.
    
    Args:
        nombres(list): Lista de nombres
        generos(list): Lista de generos
        legajos(list): Lista de legajos
        promedios(list): Lista de promedios
        calificaciones(list): Lista de calificaciones        
    """
    legajo_ingresado = input("Ingrese el numero de legajo a buscar: ")
    legajo_valido = validar_legajo_a_buscar(legajo_ingresado)
    legajo_a_buscar = int(legajo_valido)
    indice = devolver_indice_legajo(legajo_a_buscar, legajos)

    if indice != -1:
        print("\nNOMBRE\t\tGENERO\tLEGAJO\tPROMEDIO\tCALIFICACIONES")
        mostrar_estudiantes_con_promedio(nombres[indice], generos[indice], legajos[indice], promedios[indice], calificaciones[indice])
    else:
        print("\nLegajo inexistente.")

def buscar_legajos(nombres: list, generos: list, legajos: list, promedios: list, calificaciones: list) -> None:
    """Busca y muestra datos de estudiantes que tengan el mismo legajo.
    
    Args:
        nombres(list): Lista de nombres
        generos(list): Lista de generos
        legajos(list): Lista de legajos
        promedios(list): Lista de promedios
        calificaciones(list): Lista de calificaciones
    """
    legajo_ingresado = input("Ingrese el numero de legajo a buscar: ")
    legajo_valido = validar_legajo_a_buscar(legajo_ingresado)
    legajo_a_buscar = int(legajo_valido)

    encontrados = 0
    print("\nNOMBRE\t\tGENERO\tLEGAJO\tPROMEDIO\tCALIFICACIONES")
    for i in range(len(legajos)):
        if legajos[i] == legajo_a_buscar:
            mostrar_estudiantes_con_promedio(nombres[i], generos[i], legajos[i], promedios[i], calificaciones[i])
            encontrados += 1

    if encontrados == 0:
        print("\nLegajo inexistente.")








