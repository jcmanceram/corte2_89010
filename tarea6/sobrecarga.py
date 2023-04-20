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
    def setUniversida(self,universidad:str):
        self.__universidad = universidad
    def getUniversidad(self):
        return self.__universidad
    def setTrabajo(self,trabajo: str):
        self.__trabajo = trabajo
    def getTrabajo(self):
        return self.__trabajo
    def frase (self):
        return 'Soy parrillero'
    
class Contador(Ciudadano):
    def __init__(self):
        super().__init__()
        self.__universidad = None
        self.__trabajo = None
    def setUniversida(self,universidad:str):
        self.__universidad = universidad
    def getUniversidad(self):
        return self.__universidad
    def setTrabajo(self,trabajo: str):
        self.__trabajo = trabajo
    def getTrabajo(self):
        return self.__trabajo
    def frase (self):
        return 'llevo 5 años trabajando independiente'
    
class Ingeniero(Ciudadano):
    def __init__(self):
        super().__init__()
        self.__universidad = None
        self.__trabajo = None
    def setUniversida(self,universidad:str):
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
    persona1.setUniversida('Universidad de la sabana')
    persona1.setTrabajo('tacos MX')

    persona2 = Contador()
    persona2.setNombre('Rodolfo')
    persona2.setEdad(50)
    persona2.setUniversida('Universidad de San Buenaventura')
    persona2.setTrabajo('ryg contaduria')

    persona3 = Ingeniero()
    persona3.setNombre('Carlos')
    persona3.setEdad(51)
    persona3.setUniversida('EAN')
    persona3.setTrabajo('M&S Soluciones ')

    print(f'{Chef.getNombre()}\ntengo {Chef.getEdad()} años\nestudie en: {Chef.getUniversidad()}\ntrabjo en {Chef.getTrabajo()}',darsaludo(Chef))
    print(f'{Contador.getNombre()}\ntengo {Contador.getEdad()} años\nestudie en: {Contador.getUniversidad()}\ntrabjo en {Contador.getTrabajo()}',darsaludo(Contador))
    print(f'{Ingeniero.getNombre()}\ntengo {Ingeniero.getEdad()} años\nestudie en: {Ingeniero.getUniversidad}\ntrabjo en {Ingeniero.getTrabajo()}',darsaludo(Chef))
if __name__=='__mani__':
    main()