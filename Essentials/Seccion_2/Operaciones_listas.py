# Rebanada: Elemento de la sintaxis que permite hacer una copia nueva de una listo o partes de una
list_1=[1,2,3,4,5,6]
list_2=list_1[1:3] # my_list[inicio : fin]
list_1[0]=2
print(list_2)

# my_list[start:end]
new_list=list_1[1:-1] # Todos los elementos menos las esquinas
print(new_list)

new_list=list_1[-1:1] # Lista vacia
print(new_list)

new_list=list_1[:3] # Inicia desde 0 hasta N-1
print(new_list)

new_list=list_1[0:] # Del 0 al ultimo
print(new_list)

new_list=list_1[:] # De inicio a fin
print(new_list)

# Se pueden eliminar rebanadas
del new_list[1:3]
print(new_list)

# Operadores in y not in
# Revisar la lista para verificar si un valor especifico esta almacenado dentro de la lista o no
# elem in my_list
# elem not in my_list
# Devuelven booleanos
# in verifica si un elemento dato dentro del argmento esta actualmente almacenado en algun lugar de la lista
# not int verifica si un elemento no se encuentra dentro de la lista

my_list = [0,3,12,8,2]
print(5 in my_list)
print(5 not in my_list)
print(12 in my_list)

#Aplicaciones avanzadas
row=[]
for i in range(8):
    row.append("WHITE_PAWN")

# Comprension de lista, la sintaxis especial para completar o llevar listas masivas
# Datos que se usan para completar la lista ("WHITE_PAWN")
# Cuantas veces se producen los datos dentro de la lista (for in range(8))
row=["WHITE_PAWN" for i in range(8)]
print(row)

# Otro ejemplo del uso de lista
squares=[1,2,3,4,5,6,7,8,9]
odds = [x for x in squares if x % 2 != 0]
print(odds)

# Arreglos de dos dimensiones "Matrices"
board=[]
for i in range (4):
    row =["Vacio" for i in range(4)]
    board.append(row)
print(board)

# Una manera mas corta de hacer esto
board = [[2 for i in range(8)] for j in range(8)]
for i in range(8):
    print("||",end="")
    for j in range(8):
        print(board[i][j],end="||")
    print("\n")

