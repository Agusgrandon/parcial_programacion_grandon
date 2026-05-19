def reporte_estadistico(contrasenia:str) -> str:
    """Realiza un reporte estadistico de una contraseña. 
    La funcion saca un porcentaje de la cantidad de letras, numeros y caracteres especiales presentes en la contraseña, ademas de
    indicar la longitud y mostrar los caracteres que se repiten de forma consecutiva.

    Args: contrasenia (str): Contraseña ingresada por el usuario.

    Returns: str: Mensaje con el total de los porcentajes, la longitud y los caracteres repetidos. 
    """
    longitud = len(contrasenia)
    contador_letras = 0
    contador_numeros = 0
    contador_caracter_especial = 0
    caracteres_repetidos = ""

    for i in range(len(contrasenia)):
        if ((contrasenia[i] >= 'a' and contrasenia[i] <= 'z') or (contrasenia[i] >= 'A' and contrasenia[i] <= 'Z')):
            contador_letras += 1
        elif contrasenia[i] >= '0' and contrasenia[i] <= '9':
            contador_numeros += 1
        else:
            contador_caracter_especial += 1
    
    for i in range(len(contrasenia) - 1):
        if contrasenia[i] == contrasenia[i + 1]:
            caracteres_repetidos += f"1 repeticion de {contrasenia[i]}\n"

    porcentaje_letras = (contador_letras * 100) / longitud
    porcentaje_numeros = (contador_numeros * 100) / longitud
    porcentaje_caracteres_especiales = (contador_caracter_especial * 100) / longitud

    mensaje = (f"La longitud de la contraseña es de {longitud} caracteres.\n"
               f"El porcentaje de letras en la contraseña es del {porcentaje_letras}%.\n"
               f"El porcentaje de numeros en la contraseña es del {porcentaje_numeros}%.\n"
               f"El porcentaje de caracteres especiales en la contraseña es del {porcentaje_caracteres_especiales}%.\n"
               f"{caracteres_repetidos}")
    
    return mensaje