from Paquetes import suml, prodl
""" 
Cuando se ejecuta un archivo directamente, su variable __name__ se establece a __main__;
Cuando un archivo se importa como un módulo, su variable __name__ se establece al nombre del archivo (excluyendo a .py)
"""
if __name__=='__main__':
    zeroes = [0 for i in range(5)]
    ones = [1 for i in range(5)]
    print(suml(zeroes))
    print(prodl(ones))

    #La variable se llama path (ruta), y es accesible a través del módulo llamado sys. Así es como puedes verificar su valor:
    import sys
    for p in sys.path:
        print(p)
    
    """
    Esta es una posible solucion para agregar una ruta a Path para poder importar correctamente un modulo
    from sys import path
    path.append('..∖∖modules')
    import module
    """
    from sys import path
    path.append('C:\\Users\\Latitude 7490\\OneDrive\\Documentos\\GitHub\\Cisco_Python-1\\Associate\\Semana_1\\extra') 
    import extra.iota as ioat
    print(ioat.FunI())
    from random import randint
    