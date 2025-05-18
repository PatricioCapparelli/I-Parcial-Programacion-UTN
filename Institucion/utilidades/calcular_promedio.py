def calcular_promedios(calificaciones: list) -> list:
    promedios = [0] * len(calificaciones)
    for i in range(len(calificaciones)):
        suma = 0
        for j in range(len(calificaciones[i])):
            suma += calificaciones[i][j]
        promedio = suma / len(calificaciones[i])
        promedios[i] = promedio
    return promedios

def ver_promedios_de_estudiantes(calificaciones:list) -> None:
    promedios = calcular_promedios(calificaciones)
    print(promedios)


def calcular_promedios_por_materia(calificaciones: list) -> list:
    cantidad_materias = len(calificaciones[0])
    cantidad_estudiantes = len(calificaciones)
    promedios_materias = [0] * cantidad_materias

    for j in range(cantidad_materias):  # recorrer columnas (materias)
        suma = 0
        for i in range(cantidad_estudiantes):  # recorrer filas (estudiantes)
            suma += calificaciones[i][j]
        promedio = suma / cantidad_estudiantes
        promedios_materias[j] = promedio
    
    return promedios_materias
