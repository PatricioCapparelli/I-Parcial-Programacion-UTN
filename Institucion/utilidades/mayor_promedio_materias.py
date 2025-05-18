from utilidades.calcular_promedio import calcular_promedios_por_materia

def mostrar_materias_mayor_promedio(calificaciones: list) -> None:
    promedios = calcular_promedios_por_materia(calificaciones)

    # Buscar el mayor promedio
    mayor = promedios[0]
    for i in range(1, len(promedios)):
        if promedios[i] > mayor:
            mayor = promedios[i]

    # Mostrar todas las materias con ese promedio
    for i in range(len(promedios)):
        if promedios[i] == mayor:
            print(f"MATERIA_{i+1} con promedio {promedios[i]}%")

def mostrar_una_materia_mayor_promedio(calificaciones:list) -> None:
    promedios = calcular_promedios_por_materia(calificaciones)

    # Mayor
    mayor = promedios[0]
    for i in range(1, len(promedios)):
        if promedios[i] > mayor:
            mayor = promedios[i]

    # Mostrar la primera materia con ese promedio
    for i in range(len(promedios)):
        if promedios[i] == mayor:
            print(f"MATERIA_{i+1} con promedio {promedios[i]}%")
            break

