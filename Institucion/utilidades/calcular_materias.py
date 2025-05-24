from datos.carga_de_datos import crear_lista

def calcular_promedios(calificaciones: list) -> list:
    """Calcula el promedio de calificaciones por estudiante.
    
    Args:
        calificaciones (list): Matriz de calificaciones donde cada fila representa un estudiante y cada columna una materia.
        
    Returns:
        list: Lista con el promedio de cada estudiante.
    """
    promedios = crear_lista(len(calificaciones), 0)
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
    print(f"\nPromedios de estudiantes: \n{promedios}")
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
    promedios_materias = crear_lista(cantidad_materias, 0)

    for i in range(cantidad_materias):  # recorre columnas (materias)
        suma = 0
        for j in range(cantidad_estudiantes):  # recorre filas (estudiantes)
            suma += calificaciones[j][i]
        promedio = suma / cantidad_estudiantes
        promedios_materias[i] = promedio
    
    return promedios_materias


def calcular_calificaciones_repetidas(calificaciones: list, n_de_materia: int) -> list:
    """Calcula las repeticiones de las calificaciones en una determinada asignatura.
    
    Args:
        calificaciones (list): Matriz de calificaciones donde cada fila es un estudiante y cada columna una materia.
        n_de_materia (int): posicion de la materia.
        
    Returns:
        list: Lista del 1 al 10 con la suma de las repeticiones que se encontraron en una asignatura.
    """
    repetidas = crear_lista(10, 0)
    indice_materia = n_de_materia - 1
    print("\nNotas repetidas: ")
    for estudiante in calificaciones:
        nota = estudiante[indice_materia]
        if 1 <= nota and nota <= 10:
            indice_nota = nota - 1
            repetidas[indice_nota] += 1 
    print(repetidas)
    
    return repetidas



