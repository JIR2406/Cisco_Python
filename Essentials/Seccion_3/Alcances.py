#El alcance de un nombre, es la parte del codigo donde el nombre es reconocido correctamente
"""
° Una variable que existe fuera de una funcion tiene un alcance dentro del cuerpo de la funcion 
excluyendo a aquellas que tienen el mismo nombre
° El alcance de una variable existe fuera de una funcion solo se puede implementar dentro de una funcion cuando su valor es leido
"""
# global: Extender el alcance de una variable incluyendo el cuerpo de las funciones
global name

"""Recursividad"""
#Tecnica donde una funcion se invoca a si misma
def fib(n): #Funcion recursiva de fibbonaci
    if n<1:
        return None #Caso general 1
    if n<3:
        return 1 #Caso general 2
    return fib(n-1)+fib(n-2) #Caso base