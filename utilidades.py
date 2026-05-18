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