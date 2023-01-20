# Permite acceder a los datos de la plataforma subyacente es decir 'Hardware'
from platform import platform, machine, processor, system, version, python_implementation as python_im, python_version_tuple as ptuple
# aliased: Cuando se estrablece a True puede hacer que la funcion presente los nombres de capa subyacente alternativos
# en luagar de los comunes
# terse: cuando se establece a True puede convencer a la funcion de presentar una forma mas breve del resultado
print(platform(aliased=False,terse=False))  #Devuelve una cadena que describe el entorno
print(platform())
print(platform(1))
print(platform(0,1))

"""Funcion machine"""
# Conocer el nombre generico del procesador
print(machine())

"""Funcion processor"""
# Devuelve una cadena con el nombre real del procesador
print(processor())

"""Funcion system"""
# Devuelve el nombre generico del sistema operativo
print(system())

"""Funcion version"""
# La version del sistema operativo se proporciona como una cadena
print(version())

"""Funcion python_implementation y python_version_tuple"""
# python_implementation devuelve una cadena que denota la implementacion de Python
print(python_im())
# python_version_tuple() devuelve una tupla de tres elementos los cuales contienen
# 1.- La parte mayor de la version de Python
# 2.- La parte menor
# 3.- El numero del nivel del parche 
for i in ptuple():
    print(i)
