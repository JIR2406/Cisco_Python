# Se crea un arrelo
# Los elementos de una lista pueden ser de diferentes tipos
# Lista: Coleccion de elementos, pero cada elemento es un escalar
numbers=[1,2,3,4,5] #Es una lista de cinco valores todos ellos numericos
numbers[0]=10 #Agregamos un valor manualmente
numbers[0]=numbers[4] #Cambiamos el elemento del numero 0
print("Contenido de la lista",numbers)

# Podemos acceder a cada uno de los elementos manualmente el elemento maximo es n-1
# print(numbers[1])

# Funcion len()
# Toma el nombre de la lista como un argumento y devuelve el numero de elementos almacenados actualmente
print(len(numbers))

# Instruccion del()
# Cualquier elemento de la lista puede ser eliminado en cualquier momento
del(numbers[1])
print(numbers)

# Los indices negativos son validos y pueden ser utiles
# Un elemento con un indice igual a -1 es el ultimo en la lista
# [0,1,2,3,4,5]
# [-6,-5,-4,-3,-2,-1]
print(numbers[-1])

# Añador un elemento al final de la lista existente
# list.append("Value")
numbers.append(3)

# El metodo insert() agrega un nuevo elemento en cualquier lugar de la lista
# list.insert(location, value)
numbers.insert(2,3)

# Añadir datos a la lista desde un for
my_list=[]
for i in range(5):
    dato=int(input(f"Ingresa dato para la posicion {i}:\t"))
    my_list.insert(i,dato)
print(my_list)

# Recorremos los datos de la lista
# Sumamos cada dato de la lista
total=0
for i in range(len(my_list)):
    total+=my_list[i]
print(total)

# Podemos intercambiar datos de una lista a la vez
# lista[0], lista[4] = lista[4], lista[0]

# Para una cantidad mayor de elementos
# for i in range(length):
#    my_list[i], my_list[length-i-1]= my_list[lenght-i-1],my_list[i]
# print(my_list)

# La lista es un tipo de dato que se utiliza para almacenar multiples objetos
# Es una collecion ordenada y mutable de elementos separados por comas entre corchetes
lista=[1,None,True,"Hola mundo"]

# Las listas pueden estar anidadas
my_list_2=[1,'a',["lista",64,[0,1],False]]

# Se puede borrar la lista entera
del my_list_2