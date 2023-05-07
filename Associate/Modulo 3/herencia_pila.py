from pila import pila as pl

class AddingStack(pl): # Esta clase hace herencia al colocar la otra clase en los parentesis
    def __init__(self):
        super().__init__()
        self.__suma=0 #Tenemos que inicializarlo
        
    def get_sum(self):
        return self.__suma

    def push(self, val):
        self.__suma += val
        pl.push(self, val)

    def pop(self):
        val = pl.pop(self)
        self.__suma -= val
        return val

pila2 = AddingStack()

pila2.push(2)
pila2.push(3)
print(pila2.pop())
