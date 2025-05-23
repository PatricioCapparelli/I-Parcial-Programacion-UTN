from validaciones.validar_con_ascii import comparar_numero_con_ascii

def validar_legajo(dato: str, longitud: int) -> bool:
    """Valida que el legajo tenga una longitud exacta, que solo tenga numeros y no empiece con 0.

    Args:
        dato (str): Cadena que representa el legajo a validar.
        longitud (int): Longitud exacta que debe tener el legajo.

    Returns:
        bool: True si el legajo es valido, False si tiene errores.
    """
    valor = True
    largo = len(dato)
    
    if largo == 0:
        print("Error: El legajo esta vacio.")
        valor = False

    if largo != longitud:
        print(f"Error: El legajo debe tener exactamente {longitud} caracteres, ingresaste: {largo}")
        valor = False

    if valor:
        if validar_numero_legajo(dato) == False:
            print(f"Error: El legajo debe ser de caracter numerico.")
            valor = False

    if valor and largo > 0:
        if ord(dato[0]) == 48 or ord(dato[0]) == 32:
            print(f"Error: El legajo '{dato}' empieza con un 0 o un espacio.")
            valor = False

    return valor

def validar_numero_legajo(cadena: str) -> bool:
    """Valida si una cadena tiene solo numeros.

    Args:
        cadena (str): Cadena a validar.

    Returns:
        bool: True si todos los caracteres son numeros, False si hay otros caracteres.
    """
    cantidad_validos = 0
    for i in range(len(cadena)):
        if comparar_numero_con_ascii(cadena[i],1):
            cantidad_validos += 1
    es_valido = False
    if cantidad_validos == len(cadena):
        es_valido = True
    return es_valido


def validar_legajo_a_buscar(legajo_ingresado: str) -> str:
    """Valida si un legajo es valido.

    Args:
        cadena (str): Cadena a validar.

    Returns:
        str: Devuelve el legajo ingresado.
    """
    legajo_valido = validar_legajo(legajo_ingresado, 5)
    
    while legajo_valido != True:
        legajo_ingresado = input("Error: Ingrese nuevamente el numero de legajo a buscar: ")
        legajo_valido = validar_legajo(legajo_ingresado, 5)
    
    return legajo_ingresado
