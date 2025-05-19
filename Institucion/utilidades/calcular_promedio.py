def calcular_promedios(calificaciones: list) -> list:
    """Calcula el promedio de calificaciones por estudiante.
    
    Args:
        calificaciones (list): Matriz de calificaciones donde cada fila representa un estudiante y cada columna una materia.
        
    Returns:
        list: Lista con el promedio de cada estudiante.
    """
    promedios = [0] * len(calificaciones)
    for i in range(len(calificaciones)):
        suma = 0
        for j in range(len(calificaciones[i])):
            suma += calificaciones[i][j]
        promedio = suma / len(calificaciones[i])
        promedios[i] = promedio
    return promedios

def ver_promedios_de_estudiantes(calificaciones:list) -> None:
    """Muestra los promedios de todos los estudiantes.
    
    Args:
        calificaciones (list): Matriz de calificaciones por estudiante.
    """
    promedios = calcular_promedios(calificaciones)
    print(promedios)
    return promedios


def calcular_promedios_por_materia(calificaciones: list) -> list:
    """Calcula el promedio de calificaciones por materia.
    
    Args:
        calificaciones (list): Matriz de calificaciones donde cada fila es un estudiante y cada columna una materia.
        
    Returns:
        list: Lista con el promedio de cada materia.
    """
    cantidad_materias = len(calificaciones[0])
    cantidad_estudiantes = len(calificaciones)
    promedios_materias = [0] * cantidad_materias

    for i in range(cantidad_materias):  # recorre columnas (materias)
        suma = 0
        for j in range(cantidad_estudiantes):  # recorre filas (estudiantes)
            suma += calificaciones[j][i]
        promedio = suma / cantidad_estudiantes
        promedios_materias[i] = promedio
    
    return promedios_materias
