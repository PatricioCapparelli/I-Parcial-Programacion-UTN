from validaciones.validar_datos import *

def inicializar_matriz(cantidad_filas:int, cantidad_columnas:int, valor_inicial:any) -> list:
    matriz = []
    for i in range(cantidad_filas):
        fila = [valor_inicial] * cantidad_columnas
        matriz += [fila]
    return matriz

def cargar_datos(nombres, generos, legajos, calificaciones):
    for i in range(len(nombres)):
        print(f"\nEstudiante {i+1}:")

        # Cargar nombre
        nombres[i] = input("Nombre: ")

        # Cargar genero con validación
        while True:
            generos[i] = input("Genero (F/M/X): ")
            if validar_genero(generos[i]):
                break
            print("Error: Género debe ser F, M o X.")

        # Cargar legajo con validación
        while True:
            legajo = input("Legajo (5 digitos): ")
            if validar_legajo(legajo):
                legajos[i] = int(legajo)
                break
            print("Error: El legajo debe tener 5 dígitos.")

        # Cargar 5 calificaciones
        for j in range(len(calificaciones[i])):  #longitud 5
            while True:
                calif = input(f"Calificación materia {j+1} (1-10): ")
                if validar_calificacion(calif):
                    calificaciones[i][j] = int(calif)
                    break
                print("Error: La calificacion debe estar entre 1 y 10, debe ser de caracter numerico.")

