def contar_caracteres(contrasenia:str) -> str:
    """Cuenta la cantidad de letras, numeros, caracteres especiales y espacios que tiene la contraseña del usuario. 

    Args: contrasenia (str): Contraseña ingresada por el usuario.

    Returns: str: Mensaje con el total de letras, numeros, caracteres especiales y espacios.
    """
    contador_letras = 0
    contador_numeros = 0
    contador_caracter_especial = 0
    contador_espacio = 0

    for i in range(len(contrasenia)):
        if ((contrasenia[i] >= 'a' and contrasenia[i] <= 'z') or (contrasenia[i] >= 'A' and contrasenia[i] <= 'Z')):
            contador_letras += 1
        elif contrasenia[i] >= '0' and contrasenia[i] <= '9':
            contador_numeros += 1
        elif contrasenia[i] >= '!' and contrasenia[i] <= '/':
            contador_caracter_especial += 1
        elif contrasenia[i] == " ":
            contador_espacio += 1
    
    mensaje = f"La contraseña tiene {contador_letras} letras, {contador_numeros} numeros, {contador_caracter_especial} caracteres especiales y {contador_espacio} espacios.\n"

    return mensaje

def buscar_caracter(contrasenia:str) -> str:
    """Busca un caracter ingresado por el usuario dentro de la contraseña.
    Recorre la contraseña y verifica cuantas veces aparece el caracter solicitado, además de guardar las posiciones en las que se encuentra.

    Args: contrasenia (str): Contraseña ingresada por el usuario.

    Returns: str: Mensaje con el total de veces que el caracter especial aparece y su posicion, o mensaje que el caracter no existe.
    """
    solicitar_caracter = input("Ingresa el caracter que queres buscar ( ! “ # $ % & ‘( ) * + , - . / ): ")
    contador_caracter = 0
    posiciones = []

    for i in range(len(contrasenia)):
        if contrasenia[i] == solicitar_caracter:
            contador_caracter += 1
            posiciones += [i]

        if contador_caracter == 1:
            mensaje = f"El caracter aparece {contador_caracter} vez, y se encuentra en la posicion {posiciones}.\n"
        elif contador_caracter >= 2:
            mensaje = f"El caracter aparece {contador_caracter} veces, y se encuentra en las posiciones {posiciones}.\n"
        else:
            mensaje = f"El caracter ingresado no existe en la contraseña.\n"

    return mensaje

def mostrar_invertida(contrasenia:str) -> str:
    """Invierte el orden de la contraseña.

    Args: contrasenia (str): Contraseña ingresada por el usuario.

    Returns: str: Muestra la contraseña invertida.
    """
    invertida = ""

    for i in range(len(contrasenia) - 1, -1, -1):
        invertida += contrasenia[i]

    mensaje = f"Contraseña invertida: {invertida}.\n"

    return mensaje

def verificar_palindromo(contrasenia:str) -> str:
    """Verifica si una contraseña es un palindromo.
    La funcion invierte el orden de la contraseña, y luego compara si el orden invertido es igual a la contraseña.

    Args: contrasenia (str): Contraseña ingresada por el usuario.

    Returns: str: Mensaje indicando si la contraseña es palindromo o no.
    """
    invertida = ""

    for i in range(len(contrasenia) - 1, -1, -1):
        invertida += contrasenia[i]

    if invertida == contrasenia:
        mensaje = f"La palabra es palíndromo.\n"
    else:
        mensaje = f"La palabra no es palíndromo.\n"

    return mensaje

def ordenar_contraseña_ascendente(contrasenia:str) -> str:
    """Ordena de forma ascendente una contraseña. 

    Args: contrasenia (str): Contraseña ingresada por el usuario.

    Returns: str: Mensaje indicando la contraseña ordenada de forma ascendente.
    """
    lista_caracteres = []

    for i in range(len(contrasenia)):
        lista_caracteres += [contrasenia[i]]

    longitud = len(lista_caracteres)

    for i in range(longitud):
        for j in range(longitud - i - 1):
            if lista_caracteres[j] > lista_caracteres[j +1]:
                auxiliar = lista_caracteres[j] 
                lista_caracteres[j] = lista_caracteres[j +1] 
                lista_caracteres[j +1] = auxiliar

    resultado = ""
    for i in range(longitud):
        resultado += lista_caracteres[i]
    
    mensaje = f"Contraseña ordenada de forma ascendente: {resultado}\n"

    return mensaje

def ordenar_contraseña_descendente(contrasenia:str) -> str:
    """Ordena de forma descendente una contraseña. 

    Args: contrasenia (str): Contraseña ingresada por el usuario.

    Returns: str: Mensaje indicando la contraseña ordenada de forma descendente.
    """
    lista_caracteres = []

    for i in range(len(contrasenia)):
        lista_caracteres += [contrasenia[i]]

    longitud = len(lista_caracteres)

    for i in range(longitud):
        for j in range(longitud - i - 1):
            if lista_caracteres[j] < lista_caracteres[j +1]:
                auxiliar = lista_caracteres[j] 
                lista_caracteres[j] = lista_caracteres[j +1] 
                lista_caracteres[j +1] = auxiliar

    resultado = ""
    for i in range(longitud):
        resultado += lista_caracteres[i]

    mensaje = f"Contraseña ordenada de forma descendente: {resultado}\n"

    return mensaje