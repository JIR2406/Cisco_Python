# Caracteres de control: Su propósito es controlar dispositivos de entrada y salida
# Punto de código: Es un numero que compone un caracter
"""
El código ASCII emplea ocho bits para cada signo. Ocho bits significan 256 caracteres diferentes. 
Los primeros 128 se usan para el alfabeto latino estándar (tanto en mayúsculas como en minúsculas).
"""

# Unicode: Asigna caracteres únicos (letras, guiones, ideogramas, etc.) a más de un millón de puntos de código

# UCS-4 emplea 32 bits (cuatro bytes) para almacenar cada carácter, y el código es solo el número único de los
# puntos de código Unicode.

# UTF-8 emplea tantos bits para cada uno de los puntos de código como realmente necesita para representarlos.

# BOM (Byte Order Mark), una Marca de Orden de Bytes es una combinación especial de bits que anuncia la codificación
# utilizada por el contenido de un archivo (por ejemplo, UCS-4 o UTF-B).

pass

"""
El operador in no debería sorprenderte cuando se aplica a cadenas, 
simplemente comprueba si el argumento izquierdo (una cadena) se puede encontrar en cualquier lugar dentro del argumento derecho (otra cadena).
El resultado es simplemente True (Verdadero) o False (Falso).
"""

"""
Comenzaremos con la función llamada min().
Esta función encuentra el elemento mínimo de la secuencia pasada como argumento. 
Existe una condición - la secuencia (cadena o lista) no puede estar vacía, de lo contrario obtendrás una excepción ValueError.
"""

"""
Del mismo modo, una función llamada max() encuentra el elemento máximo de la secuencia.
"""

"""
El método index() (es un método, no una función) busca la secuencia desde el principio, 
para encontrar el primer elemento del valor especificado en su argumento.
Nota: el elemento buscado debe aparecer en la secuencia, su ausencia causará una excepción ValueError.
El método devuelve el índice de la primera aparición del argumento 
print("aAbByYzZaA".index("b"))
"""

"""
La función list() toma su argumento (una cadena) y crea una nueva lista que contiene todos los caracteres de la cadena, uno por elemento de la lista.
"""

"""
El método count() cuenta todas las apariciones del elemento dentro de la secuencia. La ausencia de tal elemento no causa ningún problema."""

# https://docs.python.org/3.4/library/stdtypes.html#string-methods.

