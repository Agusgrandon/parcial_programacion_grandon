from analisis import ordenar_contraseña_ascendente, ordenar_contraseña_descendente

def titulo_del_programa():
    """Muestra por pantalla el titulo del programa."""

    print("Bienvenido al sistema de procesamiento de contraseñas 👨‍💻.\n")

def menu_de_opciones():
    """Muestra por pantalla el menú principal de opciones del programa."""

    print("1) Ingresar contraseña")
    print("2) Validar nivel de seguridad")
    print("3) Contar tipos de caracteres")
    print("4) Buscar caracter especifico")
    print("5) Mostrar contraseña invertida")
    print("6) Generar reporte estadistico")
    print("7) Verificar si es palindromo")
    print("8) Ordenar caracteres de la contraseña")
    print("9) Salir.\n")

def menu_opcion_de_orden(contrasenia:str) -> str:
    """Muestra un menu de opciones para ordenar la contraseña. 
    Segun la opcion ingresada por el usuario, la contraseña se ordena de forma ascendente o de forma descendente.

    Args: contrasenia (str): Contraseña ingresada por el usuario.

    Returns: str: retorna la contraseña ordenada de forma ascendente o descendente, o mensaje de error si la opcion no es correcta. 
    """
    print("Ingresa la opcion de como queres ordenar la contraseña")
    print("A: De forma ascendente")
    print("B: De forma descendente")
    opcion = input("Opcion: ")

    if opcion == "a" or opcion == "A":
        ordenar = ordenar_contraseña_ascendente(contrasenia)
    elif opcion == "b" or opcion == "B":
        ordenar = ordenar_contraseña_descendente(contrasenia)
    else:
        ordenar = f"La opcion ingresada no es correcta.\n"
    
    return ordenar