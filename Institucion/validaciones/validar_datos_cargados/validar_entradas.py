from validaciones.validar_con_ascii import comparar_numero_con_ascii

def validar_numero(cadena:str) -> bool:
    """Valida si una cadena representa un numero entero del 1 al 10.

    Args:
        cadena (str): Cadena a validar.

    Returns:
        bool: True si es un numero entero entre 1 y 10, False si no lo es.
    """
    es_valido = True 

    if len(cadena) == 0:
        es_valido = False

    for caracter in cadena:
        if es_valido:
            es_valido = comparar_numero_con_ascii(caracter,1)

    if es_valido:
        numero = int(cadena)
        es_valido = (1 <= numero and numero <= 10)

    return es_valido

def validar_genero(genero: str) -> bool:
    """Valida si el genero ingresado es F, M o X (mayuscula o minuscula).

    Args:
        genero (str): Caracter que representa el genero.

    Returns:
        bool: True si es valido, False si no.
    """
    es_valido = False
    
    if len(genero) == 1:
        codigo = ord(genero)

        if (codigo == 70 or codigo == 77 or codigo == 88 or
            codigo == 102 or codigo == 109 or codigo == 120):
            es_valido = True
    
    return es_valido


def validar_nombre(cadena:str) -> bool:
    """Valida que una cadena sea un nombre valido (solo letras , al menos 3 caracteres y maximo 15).

    Args:
        cadena (str): Cadena de texto que representa un nombre.

    Returns:
        bool: True si el nombre es valido, False si no.
    """
    es_valido = True 

    if len(cadena) < 3:
        es_valido = False

    if len(cadena) > 15:
        es_valido = False

    for caracter in cadena:
        if es_valido: 
            es_valido = (65 <= ord(caracter) and ord(caracter) <= 90) or (97 <= ord(caracter) and ord(caracter) <= 122) 

    return es_valido 