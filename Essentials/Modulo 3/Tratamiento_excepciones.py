"""
try:
    # Es un lugar donde tu puedes hacer algo
    # Sin pedir permiso

except:
        # Es un espacio dedicado
        # Exclusivamente para los errores

"""

# try: Marca el lugar donde intentas hacer algo
# except: Lugar donde puedes manejar la excepcion

try:
    value = int(input("Ingresa un numero natural:\t"))
    print(f' El numero reciproco de {value} es: ', 1/value)
except:
    print(f"El numero ingresado no es un numero natural")

"""Lidiar con mas de una excepcion"""
# Se pueden colocar tantas excepciones como necesitemos
# No se puede colocar la misma excepcion dos veces

try:
    value = int(input("Ingresa un numero natural:\t"))
    print(f' El numero reciproco de {value} es: ', 1/value)
except ValueError:
    print("El numero ingresado no es un numero natural")
except ZeroDivisionError:
    print("La division entre cero no esta permitida en nuestro universo")

"""Excepcion predeterminada"""
# No tiene un nombre especifico podemos decir que es anonimo
# El except por defecto debe ser el ultimo except siempre

try:
    value = int(input("Ingresa un numero natural:\t"))
    print(f' El numero reciproco de {value} es: ', 1/value)
except ValueError:
    print("El numero ingresado no es un numero natural")
except:
    print("Ocurrio un error inesperado")

"""Excepciones utiles"""
# ZeroDivisionError: Aparece cuando intentas forzar una division de un numero entre cero
# ValueError: Ocurre cuando una funcion recie un argumento de un tipo adecuado pero su valor es inaceptable
# TypeError: Cuando se intenta aplicar un dato cuyo tipo no se puede aceptar en el contexto actual
# AttributeError: Ocurre cuando intentas activar un metodo que no eciste en un elemento
# SyntaxError: Cuando el control llega a una linea de codigo que viola gramatica de Python

"""Depurador"""
# Es un software especializado que puede controlar como se ejecuta tu programa
# - Ejecutar codigo linea por linea
# - Inspeccionar todos los estados de las variables
# - Cambiar sus valores en cualquier momento sin modificar el codigo fuente
# - Detener la ejecucion del programa cuando se cumplen o no ciertas condiciones

"""print debugging(depuracion)"""
# A veces se llama depuracion interactiva

"""Consejos utiles"""
# Intenta decirle a alguien
# Aislar el problema
# Analizar todos los cambios que has introducido en el codigo
# Tomar un descanso
# Ser optimista

"""Pruebas unitarias"""
# Asumen que las pruebas son partes inseparables del codigo y la preparacion de los datos de prueba es una
# parte inseparable de la codificacion
# Debes equipar el codigo con una interfaz que pueda ser utilizada por un entorno de pruebas automatizado
# Python proporciona un modulo dedicado llamano 'unittest' 