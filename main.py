from validaciones import solicitar_contrasenia, nivel_de_seguridad
from analisis import contar_caracteres, buscar_caracter, mostrar_invertida, verificar_palindromo
from utilidades import menu_de_opciones, menu_opcion_de_orden, titulo_del_programa
from estadisticas import reporte_estadistico

continuar = True
titulo_del_programa()

while continuar:

    menu_de_opciones()
    ingresar_opcion = int(input("Ingresa una opcion: "))

    match ingresar_opcion: 
        case 1:
            contrasenia = solicitar_contrasenia()
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
            generar_reporte_estadistico = reporte_estadistico(contrasenia)
            print(generar_reporte_estadistico)
        case 7:
            palabra_palindromo = verificar_palindromo(contrasenia)
            print(palabra_palindromo)
        case 8:
            opcion_de_ordenar = menu_opcion_de_orden(contrasenia)
            print(opcion_de_ordenar)
        case 9:
            continuar = False
            print("Adiós 👋")
        case _:
            print("La opcion ingresada no es correcta, intentelo nuevamente")