lista_original = [9, 10, 7, 5, 8, 4]
for j in range(len(lista_original)-1):
    for i in range(len(lista_original)-1):  # Numero de comparaciones
        if lista_original[i] > lista_original[i+1]:  # Comparar elementos adyacentes
            lista_original[i], lista_original[i+1] = lista_original[i+1], lista_original[i]# Intercambian elementos
    print(f"Comparacion #{j+1}",lista_original)
