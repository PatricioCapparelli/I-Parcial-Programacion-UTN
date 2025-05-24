from utilidades.calcular_materias import calcular_promedios_por_materia

def mostrar_materias_mayor_promedio(calificaciones: list) -> None:
    """Muestra todas las materias que tienen el mayor promedio.

    Args:
        calificaciones (list): Matriz de calificaciones donde cada fila representa a un estudiante y cada columna una materia.
    """
    promedios = calcular_promedios_por_materia(calificaciones)
    mayor = promedios[0]

    print("\nMateria\s con mayor promedio: ")
    for i in range(1, len(promedios)):
        if promedios[i] > mayor:
            mayor = promedios[i]

    for i in range(len(promedios)):
        if promedios[i] == mayor:
            print(f"MATERIA_{i+1} con promedio {round(promedios[i],2)}%")

def mostrar_una_materia_mayor_promedio(calificaciones:list) -> None:
    """Muestra la primera materia que tiene el mayor promedio.

    Args:
        calificaciones (list): Matriz de calificaciones donde cada fila representa a un estudiante y cada columna una materia.
    """
    promedios = calcular_promedios_por_materia(calificaciones)
    mayor = promedios[0]
    
    print("\nMateria con mayor promedio: ")
    for i in range(1, len(promedios)):
        if promedios[i] > mayor:
            mayor = promedios[i]

    for i in range(len(promedios)):
        if promedios[i] == mayor:
            print(f"MATERIA_{i+1} con promedio {round(promedios[i],2)}%")
            break # sale del bucle porque encontro la primera con mayor promedio

