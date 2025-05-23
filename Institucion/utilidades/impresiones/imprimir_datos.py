def mostrar_estudiantes_con_promedio(nombres: str, genero: str, legajo: int, promedio: float, calificaciones: list) -> None:
    """Imprime los datos de un estudiante en formato tabular."""
    if len(nombres) > 7:
        print(f"{nombres}\t{genero}\t{legajo}\t{promedio}\t\t{calificaciones}")
    else:
        print(f"{nombres}\t\t{genero}\t{legajo}\t{promedio}\t\t{calificaciones}")

def imprimir_estudiantes_sin_promedio(nombres, generos, legajos, calificaciones):
    """Muestra los datos de estudiantes en formato de tabla dependiendo de sus indices.
    
    Args:
        nombres(list): Lista de nombres
        generos(list): Lista de generos
        legajos(list): Lista de legajos 
        calificaciones(list): Lista de listas con notas
    """
    print("\nNOMBRE\t\tGENERO\tLEGAJO\tCALIFICACIONES")
    for i in range(len(nombres)):
        if len(nombres[i]) > 7:
            print(f"{nombres[i]}\t{generos[i]}\t{legajos[i]}\t{calificaciones[i]}")
        else:
            print(f"{nombres[i]}\t\t{generos[i]}\t{legajos[i]}\t{calificaciones[i]}")

def imprimir_estudiante_sin_promedio(nombre: str, genero: str, legajo: int, calificaciones: list) -> None:
    """Imprime los datos de un estudiante.
    
    Args:
        nombre(str): Nombre del estudiante
        genero(str): Genero del estudiante (F/M/X)
        legajo(int): Numero de legajo
        calificaciones(list): Lista de calificaciones
    """
    print(f"{nombre}\t{genero}\t{legajo}\t{calificaciones}")
