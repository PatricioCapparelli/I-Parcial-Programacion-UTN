# testeadas
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
            es_valido = (48 <= ord(caracter) and ord(caracter) <= 57)

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
def validar_legajo(dato: str, longitud: int) -> bool:
    """Valida que el legajo tenga una longitud exacta, que solo tenga numeros y no empiece con 0.

    Args:
        dato (str): Cadena que representa el legajo a validar.
        longitud (int): Longitud exacta que debe tener el legajo.

    Returns:
        bool: True si el legajo es valido, False si tiene errores.
    """
    valor = True
    errores = [""] * 3
    
    if len(dato) != longitud:
        errores[0] = f"Error: la cadena debe tener exactamente {longitud} caracteres. (Ingresaste {len(dato)})"
        valor = False

    if validar_numero_legajo(dato) == False:
        errores[1] = "Error: el legajo debe contener solo caracteres numericos."
        valor = False

    if ord(dato[0]) == 48:
        errores[2] = "Error: el legajo no puede comenzar con 0."
        valor = False

    for i in range(len(errores)):
        if errores[i] != "":
            print(errores[i])

    return valor

def validar_nombre(cadena:str) -> bool:
    """Valida que una cadena sea un nombre valido (solo letras y al menos 3 caracteres).

    Args:
        cadena (str): Cadena de texto que representa un nombre.

    Returns:
        bool: True si el nombre es valido, False si no.
    """
    es_valido = True 

    if len(cadena) < 3:
        es_valido = False

    for caracter in cadena:
        if es_valido: 
            es_valido = (65 <= ord(caracter) and ord(caracter) <= 90) or (97 <= ord(caracter) and ord(caracter) <= 122) 

    return es_valido 

def validar_numero_legajo(cadena: str) -> bool:
    """Valida si una cadena tiene solo numeros.

    Args:
        cadena (str): Cadena a validar.

    Returns:
        bool: True si todos los caracteres son numeros, False si hay otros caracteres.
    """
    cantidad_validos = 0
    for i in range(len(cadena)):
        if 48 <= ord(cadena[i]) and ord(cadena[i]) <= 57:
            cantidad_validos += 1
    es_valido = False
    if cantidad_validos == len(cadena):
        es_valido = True
    return es_valido
