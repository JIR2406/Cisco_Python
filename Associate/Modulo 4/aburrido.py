class intento:
    def __init__(self) -> None:
        self.nombre=""
        self.apellidoP=""
        self.appelidoM=""
        self.id=""
        
    def setNombre(self,nombre):
        self.nombre=nombre
        
    def setApellidoP(self,apellidoP):
        self.apellidoP=apellidoP
        
    def setApellidoM(self,apellidoM):
        self.appelidoM=apellidoM
    def __str__(self) -> str:
        print("ID:\t",self.id)
        print("El cliente:\t",self.nombre," ",self.apellidoP," ",self.appelidoM)

    def set_numID(self): #Codigo que hace un numero de identificacion con un apellido y con un nombre
        for i in self.apellidoP: # Llena una cadena con letras mezcladas de su nombre y apellido
            for j in self.nombre:
                self.id+=i+j
        self.id=self.id.lower()
        aux=""
        for k in range(0,len(self.id)): # Las transformamos a codigo ascci
            if k<10:
                aux+=str(ord(self.id[k]))
        aux2=""
        for p in range(0,len(aux)): # Delimitamos el tamaño del ID
            if p<11:
                aux2+=aux[p]
        self.id=aux2 # Asignamos el ID final
            
        
obj=intento()
obj.setNombre(input("Ingresa un nombre:\t"))
obj.setApellidoP(input("Ingresa el apellido paterno:\t"))
obj.setApellidoM(input("Ingresa el apellido materno:\t"))
obj.set_numID()
obj.__str__()