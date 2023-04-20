class Ciudadano ():
    def __init__(self):
        self.__nombre =  None
        self.__edad = None
    
    def getNombre (self):
        return self.__nombre
    def setNombre (self, nombre:str):
        self.__nombre = nombre

    def getEdad(self):
        return self.__edad
    def setEdad(self,edad:int):
        self.__edad = edad
    
class Chef(Ciudadano):
    def __init__(self):
        super().__init__()
        self.__universidad = None
        self.__trabajo = None
    def setUniversidad(self,universidad:str):
        self.__universidad = universidad
    def getUniversidad(self):
        return self.__universidad
    def setTrabajo(self,trabajo: str):
        self.__trabajo = trabajo
    def getTrabajo(self):
        return self.__trabajo
    def frase (self):
        return 'parrillero'
    
class Contador(Ciudadano):
    def __init__(self):
        super().__init__()
        self.__universidad = None
        self.__trabajo = None
    def setUniversidad(self,universidad:str):
        self.__universidad = universidad
    def getUniversidad(self):
        return self.__universidad
    def setTrabajo(self,trabajo: str):
        self.__trabajo = trabajo
    def getTrabajo(self):
        return self.__trabajo
    def frase (self):
        return 'independiente hace 3 años'
    
class Ingeniero(Ciudadano):
    def __init__(self):
        super().__init__()
        self.__universidad = None
        self.__trabajo = None
    def setUniversidad(self,universidad:str):
        self.__universidad = universidad
    def getUniversidad(self):
        return self.__universidad
    def setTrabajo(self,trabajo: str):
        self.__trabajo = trabajo
    def getTrabajo(self):
        return self.__trabajo
    def frase (self):
        return 'independiente hace 8 años '
def darsaludo (obj):
    return obj.frase()
 
def main():
    persona1 = Chef()
    persona1.setNombre('Miguel')
    persona1.setEdad(47)
    persona1.setUniversidad('Universidad de la sabana')
    persona1.setTrabajo('tacos MX')

    persona2 = Contador()
    persona2.setNombre('Rodolfo')
    persona2.setEdad(50)
    persona2.setUniversidad('Universidad de San Buenaventura')
    persona2.setTrabajo('ryg contaduria')

    persona3 = Ingeniero()
    persona3.setNombre('Carlos')
    persona3.setEdad(51)
    persona3.setUniversidad('EAN')
    persona3.setTrabajo('M&S Soluciones')

    print(f'{persona1.getNombre()} tengo {persona1.getEdad()} años estudie en la {persona1.getUniversidad()}. actualmente trabjo en {persona1.getTrabajo()} y soy',darsaludo(persona1))
    print('\n')
    print(f'{persona2.getNombre()} tengo {persona2.getEdad()} años estudie en la {persona2.getUniversidad()}. actualmente trabjo en {persona2.getTrabajo()} y soy',darsaludo(persona2))
    print('\n')
    print(f'{persona3.getNombre()} tengo {persona3.getEdad()} años estudie en la {persona3.getUniversidad()}. actualmente trabjo en {persona3.getTrabajo()} y soy',darsaludo(persona3))
if __name__=='__main__':
    main()