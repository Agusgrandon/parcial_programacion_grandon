from validaciones import solicitar_contrasenia, nivel_de_seguridad
from analisis import contar_caracteres, buscar_caracter, mostrar_invertida

continuar = True

while continuar:
    print("1) Ingresar contraseña")
    print("2) validar nivel de seguridad")
    print("3) contar tipos de caracteres")
    print("4) buscar caracter especifico")
    print("5) mostrar contraseña invertida")
    print("6) generar reporte estadistico")
    print("7) verificar si es palindromo")
    print("8) ordenar caracteres de la contraseña")
    print("9) salir")
    
    ingresar_opcion = int(input("Ingresa una opcion: "))

    match ingresar_opcion: 
        case 1:
            contrasenia = solicitar_contrasenia()
            print(contrasenia)
        case 2:
            validar_seguridad_de_contrasenia = nivel_de_seguridad(contrasenia)
            print(validar_seguridad_de_contrasenia)
        case 3:
            contar_datos = contar_caracteres(contrasenia)
            print(contar_datos)
        case 4:
            buscar_caracter_especial = buscar_caracter(contrasenia)
            print(buscar_caracter_especial)
        case 5:
            mostrar_contraseña_invertida = mostrar_invertida(contrasenia)
            print(mostrar_contraseña_invertida)
        case 6:
            print("hola")
        case 7:
            print("hola")
        case 8:
            print("hola")
        case 9:
            continuar = False
        case _:
            print("La opcion ingresada no es correcta, intentelo nuevamente")