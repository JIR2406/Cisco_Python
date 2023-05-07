"""Funcion return"""
#Tiene dos variables diferentes
# Return sin expresion
def ejemplo():
    print("Estamos en la funcion")
    return
    print("Nunca se ejecutara esto")
ejemplo()

#Return con una expresion
def suma(a,b):
    return a+b
print("El resultado de la suma es:\t",suma(4,2))

"""Consecuencias de usarla"""
# Terminacion inmediata de la ejecucion de la funcion
# Evaluara el valor de la expresion y lo devolvera como el resultado de la funcion
# Regresa un valor el cual se puede guardar en una variable

"""Valor None"""
# Un valor que es ninguno
# No debe participar en ninguna expresion
# Palabra reservada 'None'
# Se usa cuando se le asigna a una  variable o cuando se compara con una variable

"""Efectos y resultados: Listas y Funciones"""
def list_sum(lst): #Recibe una lista
    s=0
    for i in lst:
        s+=i
    return s
print(list_sum([5,4,3])) #Podemos enviar una lista por parametro

# Crear una lista por funciones
def crear_lst(n): #Pasamos el tamaño del array
    lst=[]
    for i in range(0,n):
        lst.insert(0,i)
    return lst
lst=crear_lst(5)
print(lst)