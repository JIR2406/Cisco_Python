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

"""Funcion choice y sample"""
# choice(secuencia)
# sample(secuencia, elementos_a_elegir=1)
# La primera variante elige un elemento 'aleatorio' de la secuencia de entrada y lo devuelve
# El segundo crea una lista que consta del elemento de la secuencia de entrada
from random import choice, sample
my_list=[1,2,3,4,5,6,7,8,9,10]
print(choice(my_list))
print(sample(my_list,5))
print(sample(my_list,10))

"""
Las capas son:
# Tu codigo se encuentra en la parte superior
# Python se encuentra directamente debajo de el 
# La sieuinte capa de la piramide se llama SO el
  entorno de Python proporciona algunas de sus funcionalidades utilizando los servicios del sistema operativo
# La capa mas inferior es el hardware, el procesador, las interfaces de red, los dispositivos de interfaz humana
  y toda otra maquinaria
"""
