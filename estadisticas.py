"""Generar reporte estadístico 

Mostrar: 
longitud total,  
porcentaje de letras,  
porcentaje de números,  
pocentaje de símbolos,  
cantidad de caracteres repetidos consecutivos. Por ejemplo: aaBB22!! --> Ejemplo: 

1 repetición de a, 

1 repetición de B, 

1 repetición de 2, 

1 repetición de !. """

def reporte_estadistico(contrasenia):

    longitud = len(contrasenia)
    contador_letras = 0
    contador_numeros = 0
    contador_caracter_especial = 0
    letras_repetidas = ""

    for i in range(len(contrasenia)):
        if ((contrasenia[i] >= 'a' and contrasenia[i] <= 'z') or (contrasenia[i] >= 'A' and contrasenia[i] <= 'Z')):
            contador_letras += 1
        elif contrasenia[i] >= '0' and contrasenia[i] <= '9':
            contador_numeros += 1
        else:
            contador_caracter_especial += 1
    
    for i in range(len(contrasenia) - 1):
        if contrasenia[i] == contrasenia[i + 1]:
            letras_repetidas += f"1 repeticion de {contrasenia[i]}\n"

    porcentaje_letras = (contador_letras * 100) / longitud
    porcentaje_numeros = (contador_numeros * 100) / longitud
    porcentaje_caracteres_especiales = (contador_caracter_especial * 100) / longitud

    mensaje = (f"La longitud de la contraseña es de {longitud} caracteres.\n"
               f"El porcentaje de letras en la contraseña es del {porcentaje_letras}%.\n"
               f"El porcentaje de numeros en la contraseña es del {porcentaje_numeros}%.\n"
               f"El porcentaje de caracteres especiales en la contraseña es del {porcentaje_caracteres_especiales}%.\n"
               f"{letras_repetidas}")
    
    return mensaje