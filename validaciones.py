from utilidades import verificar_letra, verificar_numero, verificar_caracter_especial

def solicitar_contrasenia() -> str:
    """solicita el ingreso de una contraseña y valida su contenido. 

    Returns: str: contraseña ingresada por el usuario.
    """
    contrasenia = input("Ingresa tu contraseña: ")
    letra = verificar_letra(contrasenia)
    while len(contrasenia) == 0 or contrasenia[0] == ' ' or len(contrasenia) < 8 or letra == False: 
        contrasenia = input("Error, reingresa tu contraseña: ")
        letra = verificar_letra(contrasenia)

    return contrasenia

def nivel_de_seguridad(contrasenia: str) -> str:
    """Determina el nivel de seguridad de la contraseña ingresada por el usuario.

    Args: contrasenia (str): Contraseña ingresada por el usuario.

    Returns: str: mensaje indicando el nivel de seguridad de la contraseña (segura, media o debil).
    """
    verificar_letras = verificar_letra(contrasenia)
    verificar_numeros = verificar_numero(contrasenia)
    verificar_caracter = verificar_caracter_especial(contrasenia)

    if verificar_numeros == True and verificar_letras ==  True and verificar_caracter == True and len(contrasenia) >= 12:
        mensaje = "contraseña muy segura"
    elif verificar_letras == True and verificar_numeros == True:
        mensaje = "contraseña media"
    elif (len(contrasenia) >= 8 and len(contrasenia) <= 9) and verificar_letras == True:
        mensaje = "Contraseña debil"

    return mensaje