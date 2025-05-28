def comparar_numero_con_ascii(caracter, length:int, primer_ascii: int = 48, ultimo_ascii: int = 57) -> bool:
    '''Devuelve True si el caracter (o numero convertido a caracter) esta dentro del rango especificado por parametros.

    Args:
        cadena (str): Cadena a validar.

    Returns:
        bool: True si esta en el rango especificado, False si no lo esta.
    '''
    
    caracter = str(caracter)  
    valido = False
    if len(caracter) == length:
        if ord(caracter) >= primer_ascii and ord(caracter) <= ultimo_ascii:
            valido = True
    return valido


def pedir_numero_de_materia(n_de_materia:int) -> int:
    '''Valida que el numero de la materia este en el rango especificado y lo devuelve convertido a entero.

    Args:
        n_de_materia (int): Numero a validar.

    Returns:
        int: Numero de la materia valido.
    '''
    valido = False

    while valido == False:
        if comparar_numero_con_ascii(n_de_materia, 1, 49, 53):
            n_de_materia = int(n_de_materia)
            valido = True
        else:
            n_de_materia = input("Error: Seleccione opcion valida (1-5): ")

    return n_de_materia
