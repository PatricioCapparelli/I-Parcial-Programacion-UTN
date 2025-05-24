from validaciones.validar_con_ascii import comparar_numero_con_ascii

def menu(cadena: str) -> int:
    '''Muestra el menu y valida que se seleccion sea valida.

    Args:
        cadena (str): opcion ingresada.
    Returns:
        int: opcion numerica valida.
    '''
    valido = False
    print(cadena)
    opcion = input("Seleccione opcion: ")

    while valido == False:
        if comparar_numero_con_ascii(opcion, 1, 49, 56):  # 1 a 8
            valido = True
        else:
            opcion = input("Error: Seleccione opcion valida (1-8): ")
            
    opcion_elegida = int(opcion)
    return opcion_elegida


