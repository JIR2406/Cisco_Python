class Persona:
    def __init__(self, id, nombre, apellidoP, apellidoM, fechaN,telefono) -> None:
        self.id = id
        self.__nombre = nombre
        self.__apellidoP = apellidoP
        self.__apellidoM = apellidoM
        self.__fechaN = fechaN
        self.__telefono = telefono
        self.__rfc = ""
    def setRFC(self):
        rfc = ""
        rfc += self.__apellidoP[0]
        for i in range(0,len(self.__apellidoM)):
            if i < 2:
                rfc += self.__apellidoM[i]
        for j in range(0,len(self.__nombre)):
            if j < 2:
                rfc += self.__nombre[j]
        
        self.__rfc = rfc.upper()
    
    def __str__(self) -> str:
        print(f"ID:\t{self.id}")
        print(f"Nombre: {self.__nombre}")
        print(f"Apellido Paterno: {self.__apellidoP}")
        print(f"Apellido Materno: {self.__apellidoM}")
        print(f"Fecha de nacimiento: {self.__fechaN}")
        print(f"Telefono: {self.__telefono}")
        print(f"RFC: {self.__rfc}")