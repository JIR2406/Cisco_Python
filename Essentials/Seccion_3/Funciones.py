"""
Si un fragmento de codigo comienza a aparecer en mas de una ocasion considera la posibilidad de aislarlo
Si un fragmento de codigo se hace tan extenso para leerlo o entenderlo se hace complicado
Descomposicion: Compartir el tranajo, compartir la responsabilidad
Se debe escribir un conjunto ien definido y claro de funciones
Se debe descomponer el problema para permitir que el producto sea implementado como un conjunto de funciones
escritas por separado empacadas juntas en diferentes modulos 
"""
# def function_name():
#   cuerpo de la funcion

# Cuando se invoca una funcion Python recuerda el lugar donde esto ocurre
# El cuerpo de la funcion es entonces ejecutando
# Al llegar al final de la funcion Python regresa al lugar inmediato despues de donde ocurrio la invocacion

# NO INVOCAR LA FUNCION ANTES DE DEFINIRLA

"""Funciones parametrizadas"""
# Los parametros solo existen dentro de las funciones en donde han sido definidos
# La asignacion de un valor a un parametro de una funcion se hace en el momento en que la funcion se manda a llamar

# def function(parameter):
#   ####

# Los parametros solo existen dentro de las funciones
# Los argumentos existen fuera de las funciones


def message(number):
    print("Ingresa un numero: ", number)
message(10)
# Una funcion puede tener tantos parametros como se desee

"""Paso de parametros posicionales"""
# Paso de parametros posicionales: Los argumentos pasados de esta manera son llamados argumentos posicionales

def my_function(a, b, c):
    print(a, b, c)
my_function(1, 2, 3)

"""Paso de argumentos de palabra clave"""
# El significado del argumento esta definido por su nombre
# No se debe de utilizar el nombre de un parametro que no existe

def introduction(first_name, last_name):
    print("Hola, mi nombre es: ", first_name, last_name)
introduction(last_name="Skywalker", first_name="Luke")

"""Funciones parametrizadas - mas detalles"""
# Funciones que tienen parametros fijos
# Aprovecho a hacer una sobre carga de metodos
def introduction(first_name, last_names="Garduño"):
    print("Hola, mi nombre es",first_name,last_names)
introduction(first_name="Jair")