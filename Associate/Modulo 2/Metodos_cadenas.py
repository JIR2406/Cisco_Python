"""
Si deseas saber el valor del punto de código ASCII/UNICODE de un carácter específico, 
puedes usar la función ord() (proveniente de ordinal).

La función necesita una cadena de un carácter como argumento - incumplir este requisito 
provoca una excepción TypeError, y devuelve un número que representa el punto de código del argumento.
"""
#chr()
"""
Si conoces el punto de código (número) y deseas obtener el carácter correspondiente, puedes usar la función llamada chr().
La función toma un punto de código y devuelve su carácter.
"""

"""
La variante de un parámetro del método center() genera una copia de la cadena original,
tratando de centrarla dentro de un campo de un ancho especificado.
El centrado se realiza realmente al agregar algunos espacios antes y después de la cadena.
"""

"""
El método endswith() 
comprueba si la cadena dada termina con el argumento especificado y devuelve True(verdadero) o False(falso), dependiendo del resultado.
"""
# Demostración del método endswith():
if "epsilon".endswith("on"):
    print("si")
else:
    print("no")

"""
El método find() es similar al método index(), el cual ya conoces, busca una subcadena y devuelve el índice de la primera aparición de esta subcadena, pero:

Es más seguro, no genera un error para un argumento que contiene una subcadena inexistente (devuelve -1 en dicho caso).
Funciona solo con cadenas, no intentes aplicarlo a ninguna otra secuencia.
"""

# Demostración del método find():
print("Eta".find("ta"))
print("Eta".find("mma"))

"""
El método sin parámetros llamado isalnum() comprueba si la cadena contiene solo dígitos o caracteres alfabéticos (letras) y 
devuelve True (verdadero) o False (falso) de acuerdo al resultado.

El método isalpha() es más especializado, se interesa en letras solamente.

Al contrario, el método isdigit() busca solo dígitos, cualquier otra cosa produce False (falso) como resultado.
"""

"""
El método isspace() identifica espacios en blanco solamente, no tiene en cuenta ningún otro carácter (el resultado es entonces False).

El método join() es algo complicado, así que déjanos guiarte paso a paso:

Como su nombre lo indica, el método realiza una unión y espera un argumento del tipo lista; se debe asegurar que todos los elementos de la lista sean cadenas: de lo contrario, el método generará una excepción TypeError.
Todos los elementos de la lista serán unidos en una sola cadena pero...
 la cadena desde la que se ha invocado el método será utilizada como separador, puesta entre las cadenas.
La cadena recién creada se devuelve como resultado.

El método sin parámetros lstrip() devuelve una cadena recién creada formada a partir de la original eliminando todos los espacios en blanco iniciales.

El método replace() con dos parámetros devuelve una copia de la cadena original en la que todas las apariciones del primer argumento han sido reemplazadas por el segundo argumento.

"""
# Demostración del método replace():
print("www.netacad.com".replace("netacad.com", "pythoninstitute.org"))
print("This is it!".replace("is", "are"))
print("Apple juice".replace("juice", ""))

"""

"""