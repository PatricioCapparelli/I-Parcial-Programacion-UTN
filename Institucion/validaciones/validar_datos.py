def pedir_numero_entero() -> int:
    '''Funcion que le pide un numero entero al usuario.
    Returns:
        int: Numero entero que ingreso el usuario.
    '''
    numero = int(input("Ingrese un numero: "))
    return numero

def pedir_cadena_texto() -> str:
    '''Funcion que le pide al usuario que ingrese un texto.
        Returns:
            str: Devuelve la cadena de texto ingresada por el usuario.
    '''
    cadena = input("Ingrese una cadena de texto: ")
    return cadena

# testeadas
def validar_calificacion(nota:int):
    """Valida que la calificacion este entre 1 y 10"""
    valido = False
    
    nota = int(nota)
    if nota >= 1 and nota <= 10:
        valido = True
    
    return valido

def validar_genero(genero): #validar
    """Valida que el genero sea F, M o X"""
    return genero == 'F' or genero == 'M' or genero == 'X'

def validar_legajo(legajo): #validar
    """Valida que el legajo sea un entero de 5 dígitos"""
    try:
        legajo = int(legajo)
        return legajo >= 10000 and legajo <= 99999
    except:
        return False
