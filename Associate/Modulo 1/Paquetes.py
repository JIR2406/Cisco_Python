"""Un modulo es un contenedor lleno de funciones
puedes empaquetar tantas funciones como desees en un módulo y distribuirlo por todo el mundo"""

# Paquete: Juega un papel similar al de una carpeta o directorio
# en el mundo de los archivos
# La inicialización se realiza sólo una vez, cuando se produce la primera importación, 
# por lo que las asignaciones realizadas por el módulo no se repiten innecesariamente
 
__counter = 0 
 
def suml(the_list):
  global __counter
  __counter += 1
  the_sum = 0
  for element in the_list:
   the_sum += element
  return the_sum
 
 
def prodl(the_list):
  global __counter
  __counter += 1
  prod = 1
  for element in the_list:
   prod *= element
  return prod
 
 
if __name__ == "__main__":
  print("Prefiero ser un módulo, pero puedo hacer algunas pruebas para usted.")
  my_list = [i+1 for i in range(5)]
  print(suml(my_list) == 15)
  print(prodl(my_list) == 120)

# Explicacion codigo de arriba
"""
Una cadena (quizás una multilínea) colocada antes de las instrucciones de cualquier módulo
(incluidas las importaciones) se denomina doc-string, y debe explicar brevemente el propósito y el contenido del módulo.
Las funciones definidas dentro del módulo (suml() y prodl()) están disponibles para ser importadas.
Se ha utilizado la variable __name__ para detectar cuando se ejecuta el archivo de forma independiente, 
y se aprovechó esta oportunidad para realizar algunas pruebas sencillas.
"""

# Inicializacion de un modulo:
"""
La inicialización de un módulo se realiza mediante un código independiente (que no forma parte de ninguna función) 
ubicado dentro del archivo del módulo. Como un paquete no es un archivo, esta técnica es inútil para inicializar paquetes.
En su lugar, debes usar un truco diferente, Python espera que haya un archivo con un nombre muy exclusivo dentro de 
la carpeta del paquete: __init__.py.
El contenido del archivo se ejecuta cuando se importa cualquiera de los módulos del paquete. Si no deseas ninguna 
inicialización especial, puedes dejar el archivo vacío, pero no debes omitirlo.
"""

