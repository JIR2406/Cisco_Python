from persona import Persona as pa
from arbol import ArbolBinario as ab
import random
def llenadoDatos():
    id=random.randrange(0,1000)
    nombre=input("Ingresa el nombre:\t")
    apellidoP=input("Ingresa el apellido paterno:\t")
    apellidoM=input("Ingresa el apellido materno:\t")
    fecha=input("Ingresa la fecha de nacimiento\t")
    telefono=input("Ingresa un numero de telefono:\t")
    obj=pa(id,nombre,apellidoP,apellidoM,fecha,telefono)
    obj.setRFC()
    return obj
    
if __name__ == "__main__":
   arbol=ab()
   while(True):
    print("MENU")
    print("1- Ingresa registro")
    print("2- Buscar por ID")
    print("3- Eliminar registro por ID")
    print("4- Eliminar todos los registros")
    print("5- Mostrar todos los registros")
    print("6- Salir")
    op=input("Ingresa una opcion:\t")
    match (op):
        case "1":
            obj=llenadoDatos()
            arbol.insertar(obj)
            pass
        case "2":
           pass
        case "3":
           pass
        case "4":
           arbol.eliminar_todo()
           print("Usuarios eliminados exitosamente")
           pass
        case "5":
            datos=arbol.imprimir_inorden()
            if len(datos)!=0:
               for i in datos:
                  print(i.__str__())    
            else:
               print("No hay usuarios registrados")
        case "6":
           break