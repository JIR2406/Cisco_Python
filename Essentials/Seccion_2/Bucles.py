#Bucle While sencillo
while True:
    romper=input("¿Deseas salir del bucle? y/n:\t")
    if romper == 'y':
        print(" == Saliendo del bucle == ")
        break
    else:
        print("El bucle continua")
else: #Se ejecuta si no se entra en el bucle
    print("Fuera del bucle")
#Bucle for
cont=0
for i in "Mississipi":
    if i=='i':
        cont+=1
print(cont)
palabra=input("Ingresa una palabra:\t")
palabra=palabra
extra=""
for letter in palabra:
    if letter=='A':
        extra+=letter
    elif letter=='E':
        extra+=letter
    elif letter=='I':
        extra+=letter
    elif letter=='O':
        extra+=letter
    elif letter=='U':
        extra+=letter
    else:
        print(letter)
else:
    print("Fuera del for") #Se ejecuta si no se entra en el bucle
