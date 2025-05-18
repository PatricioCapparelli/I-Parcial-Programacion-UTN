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
def validar_calificacion(cadena: str) -> bool:
    valor = False
    if len(cadena) == 1 and (ord(cadena) >= 49 and ord(cadena) <= 57):
        valor = True

    elif len(cadena) == 2 and cadena[0] == 49 and cadena[1] == 48:
        valor = True
    return valor

