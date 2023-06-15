import os

"""
systemname - almacena el nombre del sistema operativo.
nodename - almacena el nombre de la máquina en la red.
release - almacena el release o actualización del sistema operativo.
version - almacena la versión del sistema operativo.
machine - almacena el identificador de hardware, por ejemplo, x86_64.
"""
print(os.name) # Como tengo windows me da nt
#os.mkdir("pruebaModuloOs")
print(os.listdir()) # Se crea una ruta en la raiz del programa

# Creación recursiva de directorios

"""
La función makedirs permite la creación recursiva de directorios, lo 
que significa que se crearán todos los directorios de la ruta
"""
#os.makedirs("pruebaModuloOs/my_second_directory")
#os.chdir("pruebaModuloOs")
print(os.listdir())

