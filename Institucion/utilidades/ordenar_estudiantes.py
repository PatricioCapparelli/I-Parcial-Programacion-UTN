def ordenar(nombres: list, generos: list, legajos: list, promedios: list, calificaciones: list, orden: int = 2) -> None:
    for i in range(len(nombres) - 1):
        for j in range(i + 1, len(nombres)):
            # Condicion para ordenar asc o desc segun 'orden' (1=asc, 2=desc)
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

def mostrar_datos_ordenados(nombres: list, generos: list, legajos: list, promedios: list, calificaciones: list, orden: int = 2) -> None:
    ordenar(nombres, generos, legajos, promedios, calificaciones, orden)
    print("NOMBRE\t\tGENERO\tLEGAJO\tPROMEDIO\tCALIFICACIONES")
    for i in range(len(nombres)):
        print(f"{nombres[i]}\t\t{generos[i]}\t{legajos[i]}\t{promedios[i]}\t\t{calificaciones[i]}")
