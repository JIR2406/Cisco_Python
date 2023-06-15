from os import strerror

try:
	file = open('newtext.txt', 'wt') # Un nuevo archivo (newtext.txt) es creado.
	for i in range(10):
		s = "línea #" + str(i+1) + "\n"
		for char in s:
			file.write(char)
	file.close()
except IOError as e:
	print("Se produjo un error de E/S: ", strerror(e.errno))
 
 
"""
 ByteArray habla sobre archivos binarios que tenemos que informarte sobre una de las clases
 especializadas de Python usa para almacenar datos amorfos
 
 Los datos amorfos son datos que no tienen forma especifica son solo una serie de bytes
 
 
"""

data= bytearray(10) # Objeto capas de almacenar diez bytes

for i in range(len(data)):
    data[i] = 10 - i

for b in data:
    print(hex(b))

data = bytearray(10)

for i in range(len(data)):
    data[i] = 10 + i

try:
    bf = open('file.bin', 'wb')
    bf.write(data)
    bf.close()
except IOError as e:
    print("Se produjo un error de E/S:", strerror(e.errno))


#Leer archivo
try:
    binary_file = open('file.bin', 'rb')
    data = bytearray(binary_file.read(5))
    binary_file.close()

    for b in data:
        print(hex(b), end=' ')

except IOError as e:
    print("Se produjo un error de E/S:", strerror(e.errno))