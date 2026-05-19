def contar_caracteres(contrasenia):
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
    
    mensaje = f"La contraseña tiene {contador_letras} letras, {contador_numeros} numeros, {contador_caracter_especial} caracteres especiales y {contador_espacio} espacios."

    return mensaje

def buscar_caracter(contrasenia):

    solicitar_caracter = input("Ingresa el caracter que queres buscar: ")
    contador_caracter = 0
    posiciones = []

    for i in range(len(contrasenia)):
        if contrasenia[i] == solicitar_caracter:
            contador_caracter += 1
            posiciones += [i]

        if contador_caracter > 0:
            mensaje = f"El caracter aparece {contador_caracter} veces, y esta en la posicion {posiciones}"
        else:
            mensaje = f"El caracter ingresado no existe en la contraseña"

    return mensaje

def mostrar_invertida(contrasenia):

    invertida = ""

    for i in range(len(contrasenia) - 1, -1, -1):
        invertida += contrasenia[i]

    mensaje = f"Contraseña invertida: {invertida}"

    return mensaje

def verificar_palindromo(contrasenia):

    invertida = ""

    for i in range(len(contrasenia) - 1, -1, -1):
        invertida += contrasenia[i]

    if invertida == contrasenia:
        mensaje = f"La palabra es palíndromo "
    else:
        mensaje = f"La palabra no es palíndromo "

    return mensaje

def ordenar_contraseña_ascendente(contrasenia):

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

    return resultado
  