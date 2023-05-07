class pila:

    def __init__(self):
        self.__stack=[]
    
    def push(self,dato): # Este es el constructor
        self.__stack.append(dato) # Para darle un atributo tenemos que iniciarlo con el self.
        # Ademas al poner el doble __ se encapsulan los datos
    
    def pop(self):
        val = self.__stack[-1]
        del self.__stack[-1]
        return val
    
    def getTope(self):
        return len(self.__stack)
    
pila1= pila()
pila1.push("1")
pila1.push("2")
pila1.push("3")

for i in range(0,pila1.getTope()):
    print(pila1.pop())