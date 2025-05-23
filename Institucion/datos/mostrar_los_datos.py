from validaciones.validar_legajos import validar_legajo_a_buscar
from utilidades.impresiones.imprimir_datos import mostrar_estudiantes_con_promedio

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

    encontrados = 0
    print("\nNOMBRE\t\tGENERO\tLEGAJO\tPROMEDIO\tCALIFICACIONES")
    for i in range(len(legajos)):
        if legajos[i] == legajo_a_buscar:
            mostrar_estudiantes_con_promedio(nombres[i], generos[i], legajos[i], promedios[i], calificaciones[i])
            encontrados += 1
            if encontrados == 1:
                break

    if encontrados == 0:
        print("Legajo inexistente.")

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
        print("Legajo inexistente.")






