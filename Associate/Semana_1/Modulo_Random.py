# Puede operar con numeros pseudoaleatorios
# Un generador de numeros aleatorio toma un valor llamado semilla
# lo trata como un valor de entrada, calcula un numero aleatorio basado en el

# Empezamos importando random
from random import random
for i in range(10):
    print(random())

# La funcion seed() es capaz de directamente establecer la semilla del generador
# seed() establece la semilla con la hora actual
# seed(int_value) estalece la semilla con el valor entero int_value

from random import random, seed
seed(1)
for i in range(5):
    print(random())

"""Las funciones randrage y randint"""
# Si se desean valores aleatorios enteros una de las siguientes funciones encajaria mejor:
from random import randrange, randint
# randrange(fin)
# randrange(inicio,fin)
# randrange(inicio, fin, incremento)
# randrange(izquiera, derecha)
print(randrange(1,10))

# Las primeras tres invocaciones generaran un valor entero tomando pseudoaleatoriamente del rango
# range(fin)
# range(inicio,fin)
# range(inicio, fin, incremento)
print(randrange(100))

"""Tienen una desventaja"""
# Pueden producir valores repetidos incluso si el numero de invocaciones posteriores no es mayor que el rango especificado
