def verificar_letra(contrasenia):
    letra = False

    for i in range(len(contrasenia)):
        if ((contrasenia[i] >= 'a' and contrasenia[i] <= 'z') or (contrasenia[i] >= 'A' and contrasenia[i] <= 'Z')):
            letra = True

    return letra

def verificar_numero(contrasenia):
    numero = False

    for i in range(len(contrasenia)):
        if contrasenia[i] >= '0' and contrasenia[i] <= '9':
            numero = True

    return numero

def verificar_caracter_especial(contrasenia):
    caracter = False

    for i in range(len(contrasenia)):
        if contrasenia[i] >= '!' and contrasenia[i] <= '/':
            caracter = True
    
    return caracter

def menu_de_opciones():
    
    print("1) Ingresar contraseña")
    print("2) Validar nivel de seguridad")
    print("3) Contar tipos de caracteres")
    print("4) Buscar caracter especifico")
    print("5) Mostrar contraseña invertida")
    print("6) Generar reporte estadistico")
    print("7) Verificar si es palindromo")
    print("8) Ordenar caracteres de la contraseña")
    print("9) Salir")

def menu_ordenar_asc_desc():

    print("Ingresa la opcion de como queres ordenar la contraseña")
    print("A: De forma ascendente")
    print("B: De forma descendente")