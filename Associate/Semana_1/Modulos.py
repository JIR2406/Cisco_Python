"""Si se desea que dicho proyecto de software se complete con exito, se debe tener los medios que permitan:
    - Dividir todas las tareas entre los desarrolladores
    - Unir todas las partes creadas en un todo funcional
"""
# A tal proceso se le denomina descomposicion
# Modulo: Archivo que contiene definiciones y sentencias de Python

"""Manejo de modulos"""
# Cuando se desea utilizar un modulo ya existente
# Cuando se desea crear un nuevo modulo ya sea para uso propio o para facilitar la vida de otros programadores
# en este caso te conviertes en el proveedor

# Un modulo se identifica por su nombre
# Todos los modulos forman parte de la biblioteca estandar de python

"""NameSpace"""
# Es un espacio en el que existen algunos nombre y los nombres no entran en conflicto entre si
# Dentro de un namespace cada nombre debe permanecer unico

"""Importacion de un modulo""" 
# Para que un modulo sea utilizable hay que importarlo
# La importacion debe de colocarse antes del primer uso de cualquiera de las entidades del modulo
import math #Importamos el modulo math # import math, sys
print(math.sin(math.pi/2)) #Sacamos el sen de 1/2 pi
"""
Estructura: 
- Nombre del modulo (math)
- Un punto (.)
- El nombre de la entidad (pi)
"""

"""Otra forma de importar"""
# from: Con que modulo vamos a trabajar
# Nombre del modulo (math)
# Palabra reservada import
# Nombres de las entidades a trabajar 
from math import pi,sin
print(math.sin(math.pi/2)) #Sacamos el sen de 1/2 pi

# Esta instruccion importa todas las entidades del modulo indicado
from sys import *

"""La palabra clave as"""
# Si se importa un modulo y no se esta conforme con el nombre del modulo en particular puede darsele otro nombre
# A esto se le llama aliasing o renombrado
# import modulo as nuevo_Nombre
import sys as sistema 

# Despues de una importacion de alias el nombre original del modulo se vuelve inaccesible
# Tambien funciona para las entidades
from math import sin as sen, pi as PI

"""Funcion dir()"""
# Tiene una condicion para su uso, el modulo debe haber sido importado como un todo
# dir(): Devuelve una lista ordenada alfabeticamente la cual tiene el nombre de las entidades dispobibles
# en el modulo
import math
for i in dir(math):
    print(i, end="\t") 

