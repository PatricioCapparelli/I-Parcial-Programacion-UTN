from utilidades.impresiones.imprimir_datos import mostrar_estudiantes_con_promedio

def ordenar(nombres:list, generos:list, legajos:list, promedios:list, calificaciones:list, orden:int = 2) -> None:
    """Ordena los datos de los estudiantes segun su promedio.

    Args:
        nombres (list): Lista de nombres de estudiantes.
        generos (list): Lista de generos de estudiantes.
        legajos (list): Lista de legajos de estudiantes.
        promedios (list): Lista de promedios de estudiantes.
        calificaciones (list): Matriz de calificaciones por estudiante.
        orden (int): Tipo de orden (1=ASC/2=DESC).
    """
    for i in range(len(nombres) - 1):
        for j in range(i + 1, len(nombres)):
            if (orden == 1 and promedios[i] > promedios[j]) or (orden == 2 and promedios[i] < promedios[j]):
                
                aux_genero = generos[i]
                generos[i] = generos[j]
                generos[j] = aux_genero

                aux_nombre = nombres[i]
                nombres[i] = nombres[j]
                nombres[j] = aux_nombre

                aux_legajo = legajos[i]
                legajos[i] = legajos[j]
                legajos[j] = aux_legajo

                aux_promedio = promedios[i]
                promedios[i] = promedios[j]
                promedios[j] = aux_promedio

                aux_calif = calificaciones[i]
                calificaciones[i] = calificaciones[j]
                calificaciones[j] = aux_calif

def mostrar_datos_ordenados(nombres:list, generos:list, legajos:list, promedios:list, calificaciones:list, orden:int = 2) -> None:
    """Ordena y muestra los datos de los estudiantes según su promedio.

    Args:
        nombres (list): Lista de nombres de estudiantes.
        generos (list): Lista de géneros de estudiantes.
        legajos (list): Lista de legajos de estudiantes.
        promedios (list): Lista de promedios de estudiantes.
        calificaciones (list): Matriz de calificaciones por estudiante.
        orden (int): Tipo de orden (ASC/DESC).
    """
    ordenar(nombres, generos, legajos, promedios, calificaciones, orden)
    
    print("\nNOMBRE\t\tGENERO\tLEGAJO\tPROMEDIO\tCALIFICACIONES")
    
    for i in range(len(nombres)):
        mostrar_estudiantes_con_promedio(nombres[i], generos[i], legajos[i], promedios[i], calificaciones[i])

