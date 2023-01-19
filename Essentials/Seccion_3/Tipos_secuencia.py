"""
Un tipo de secuencia es un tipo de dato en Python el cual es capaz de almacenar mas de un valor
los cuales pueden ser secuencialmente examinados
"""
# Una secuencia es un tipo de dato que puede ser escaneado por el bucle for
"""
Mutabilidad: Propiedad de cualquier tipo de dato en Python que describe su disponibilidad su disponibilidad
para poder cambiar libremente durante la ejecucion de un programa

° Existen dos tipos de datos: Mutables e Inmutables
"""
# Tupla: Secuencia inmutable
tupla_1=(1,2,3,4,5)
print(tupla_1)
# ===Cada elemento de una tupla puede ser de distinto tipo===
tupla_2=() # Tupla vacia
#Para recorrer una tupla:
for i in tupla_1:
    print(i)

# No intentes modificar el contenido de la tupla
# Puede tener la funcion len() y los operadores logicos
t1=(1,)
t2=(2,)
t3=(3,123)
t1,t2,t3=t2,t3,t1 #Cambia los valores de la tupla
print(t1,t2,t3)

"""Diccionarios"""
# Es otro tipo de estructura de datos de Python
# No es una secuencia y ademas es mutable
# Su sintaxis: nombre={"clave":"valor"}
diccionario={"Alan":"Diaz","Jair":"Garduño"}
# La palabra que se esta buscando se denomina key
# La palabra que se obtiene del diccionario se denomina value
# Cada clave debe de ser unica
# Una clave puede ser de cualquier tipo de dato
# Se puede usar la funcion len()
# Herramienta de un solo sentido
diccionary={"cat":"gato","perro":"chow chow","puerco":"mini pig"} 
words = ['perro', 'cat','araña']
for word in words:
    if word in diccionary:
        print(word, "->" , diccionary[word])
    else:
        print(word, "no esta en el diccionario")

"""Metodo Keys()"""
# El metodo retorna o regresa una lista de todas las claves dentro del diccionario
print("="*20)
for key in diccionary.keys():
    print(key, "->", diccionary[key])

"""Metodo Items"""
#vEste metodo retorna una lista de tuplas, donde cada tupla es un par de cada clave con su valor
print("="*20)
for spanish, french in diccionary.items():
    print(spanish, "->",french)

"""Modificar, agregar y eliminar valores"""
#vAsigna un valor a una clave existente es sencillo, son mutables
print("="*20)
diccionary["cat"]="gatito"
for spanish, french in diccionary.items():
    print(spanish, "->",french)

"""Funcion sorted()"""
#vSi queremos que la salida este ordenada hacemos lo siguiente
print("="*20)
for key in sorted(diccionary.keys()):
    print(key)

"""Funcion values()"""
# Regresa una lista de valores
print("="*20)
for french in diccionary.values():
    print(french)

"""Agregar nuevas claves"""
#Claves que no hayan existido antes
print("="*20)
diccionary['labrador']='golderretriver'

"""Funcion update()"""
#Agrega datos al final
diccionary.update({"pato":'gallina'})
print(diccionary)

"""Eliminar una clave"""
# Se remueve el valor asociado, los valores no pueden existir sin sus claves
print("="*20)
del diccionary['pato']
print(diccionary)
# Al eliminar una clave no existente provoca un error

# Para eliminar el ultimo elemento de la lista se usa popitem()
print("="*20)
diccionary.popitem()
print(diccionary)

#Se puede crear una tupla con la funcion tuple()