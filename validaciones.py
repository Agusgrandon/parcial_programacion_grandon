def verificar_letra(contrasenia:str) -> bool:
    """analiza si la frase recibida contiene una letra

    Args: contrasenia (str): Contraseña ingresada por el usuario.

    Returns: bool: True si la contraseña contiene una letra, False en caso contrario.
    """
    letra = False

    for i in range(len(contrasenia)):
        if ((contrasenia[i] >= 'a' and contrasenia[i] <= 'z') or (contrasenia[i] >= 'A' and contrasenia[i] <= 'Z')):
            letra = True

    return letra

def verificar_numero(contrasenia:str) -> bool:
    """analiza si la frase recibida contiene un numero

    Args: contrasenia (str): Contraseña ingresada por el usuario.

    Returns: bool: True si la contraseña contiene un numero, False en caso contrario.
    """
    numero = False

    for i in range(len(contrasenia)):
        if contrasenia[i] >= '0' and contrasenia[i] <= '9':
            numero = True

    return numero

def verificar_caracter_especial(contrasenia:str) -> bool:
    """analiza si la frase recibida contiene un caracter especial

    Args: contrasenia (str): Contraseña ingresada por el usuario.

    Returns: bool: True si la contraseña contiene un caracter especial, False en caso contrario.
    """
    caracter = False

    for i in range(len(contrasenia)):
        if contrasenia[i] >= '!' and contrasenia[i] <= '/':
            caracter = True
    
    return caracter

def solicitar_contrasenia() -> str:
    """solicita el ingreso de una contraseña y valida su contenido. 

    Returns: str: contraseña ingresada por el usuario.
    """
    contrasenia = input("Ingresa tu contraseña, debe contener al menos 1 letra y tener al menos 8 caracteres: ")
    letra = verificar_letra(contrasenia)
    while len(contrasenia) == 0 or contrasenia[0] == ' ' or len(contrasenia) < 8 or letra == False: 
        contrasenia = input("La contraseña ingresada no tiene los requisitos basicos, intentalo nuevamente: ")
        letra = verificar_letra(contrasenia)

    return contrasenia

def nivel_de_seguridad(contrasenia:str) -> str:
    """Determina el nivel de seguridad de la contraseña ingresada por el usuario.

    Args: contrasenia (str): Contraseña ingresada por el usuario.

    Returns: str: mensaje indicando el nivel de seguridad de la contraseña (segura, media o debil).
    """
    verificar_letras = verificar_letra(contrasenia)
    verificar_numeros = verificar_numero(contrasenia)
    verificar_caracter = verificar_caracter_especial(contrasenia)

    if verificar_numeros and verificar_letras and verificar_caracter and len(contrasenia) >= 12:
        mensaje = "La contraseña es muy segura 😀\n"
    elif verificar_letras and verificar_numeros:
        mensaje = "La contraseña tiene un nivel de seguridad media, te sugerimos agregarle un caracter especial.\n"
    elif (len(contrasenia) >= 8 and len(contrasenia) <= 9) and verificar_letras:
        mensaje = "Tu contraseña es debil, te sugerimos agregarle un numero y un caracter especial.\n"

    return mensaje