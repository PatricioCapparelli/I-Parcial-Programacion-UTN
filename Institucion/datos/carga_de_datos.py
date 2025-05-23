from validaciones.validar_legajos import validar_legajo
from validaciones.validar_datos_cargados.validar_entradas import validar_genero,validar_nombre,validar_numero

def inicializar_matriz(cantidad_filas:int, cantidad_columnas:int, valor_inicial:any) -> list:
    """Crea una matriz con los mismos datos.
    
    Args:
        cantidad_filas(int): Numero de filas 
        cantidad_columnas(int): Numero de columnas 
        valor_inicial(any): Valor de cualquier tipo para llenar la matriz 
        
    Returns:
        list:Lista de listas.
    """
    matriz = []
    for i in range(cantidad_filas):
        fila = [valor_inicial] * cantidad_columnas
        matriz += [fila]
    return matriz

def crear_lista(cantidad: int, valor_inicial:any):
    """Crea una lista con los mismos datos.
    
    Args:
        cantidad(int): Numero de columnas
        valor_inicial(any): Valor de cualquier tipo para llenar la lista 
        
    Returns:
        list:Lista. 
    """
    lista = [valor_inicial] * cantidad

    return lista

def cargar_datos(nombres, generos, legajos, calificaciones):
    """Carga datos de estudiantes en las listas.
    
    Args:
        nombres(list): Lista para guardar nombres
        generos(list): Lista para guardar generos
        legajos(list): Lista para guardar legajos
        calificaciones(list): Lista para guardar notas
        
    Returns:
        list: Lista con los datos cargados
    """
    for i in range(len(nombres)):
        print(f"\nEstudiante {i+1}:")

        while True:
            nombre = input("Nombre: ")
            if validar_nombre(nombre):
                nombres[i] = nombre
                break
            print("Error: El nombre debe tener solo letras, mas de 2 caracteres , menos de 16 y sin espacios.")

        while True:
            generos[i] = input("Genero (F/M/X): ")
            if validar_genero(generos[i]):
                break
            print("Error: Genero debe ser F, M o X y debe estar escrito en Mayuscula.")

        while True:
            legajo = input("Legajo (5 digitos): ")
            if validar_legajo(legajo, 5):
                legajos[i] = int(legajo)
                break

        for j in range(len(calificaciones[i])):  #longitud 5
            while True:
                calif = input(f"Calificacion materia {j+1} (1-10): ")
                if validar_numero(calif):
                    calificaciones[i][j] = int(calif)
                    break
                print("Error: La calificacion debe estar entre 1 y 10, debe ser de caracter numerico.")

