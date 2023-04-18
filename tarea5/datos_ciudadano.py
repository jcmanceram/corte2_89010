'''+---------------------+
    |     Ciudadano       |
    +---------------------+
    | - __nombre: str     |
    | - __edad: int       |
    | - __documento: str  |
    +---------------------+
    | + getNombre() : str  |
    | + getEdad() : int    |
    | + getDocumento() : str |
    | + setNombre(nombre: str) : void |
    | + setEdad(edad: int) : void |
    | + setDocumento(documento: str) : void |
    | - __documentov() : str |
    | + getDocumentoV() : str |
    | - __indice() : str |
    | + getMayor() : str   |
    +---------------------+
'''
class Ciudadano ():
    def __init__(self,nombre:str, edad:int, documento:str):
        self.__nombre =  nombre
        self.__edad =  edad
        self.__documento =  documento
    #---------------------Getters------------------------
    def getNombre(self):
        return self.__nombre

    def getEdad(self):
        return self.__edad

    def getDocumento(self):
        return self.__documento

    #---------------------Setters------------------------
    def setNombre(self, nombre:str):
        self.__nombre = nombre
    def setEdad(self, edad:int):
         self.__edad = edad
    def setDocumento(self,documento:str):
         self.__documento = documento 
    #----------------verificacion de datos -------------
    def __documentov (self):
        documento = self.__documento 
        str(documento)
        if len(documento)<=7 or len(documento)>=11:
            return str('La cédula debe tener entre 8 y 10 dígitos')
        else:
            return documento
    def getDocumentoV(self):
        return self.__documentov()
    
    #----------------- mayor de edad--------------------
    def __indice(self):
        mayorDeEdad = self.__edad
        if mayorDeEdad >=18 :
            return str('Es mayor de edad.')
        else:
            return str('Es menor de edad.')
    def getMayor(self):
        return self.__indice()

def main ():
    nombre = input('ingrese su nombre: ')
    edad = int(input('ingrese su edad: '))
    documento = input('ingrese su documento: ')
    persona = Ciudadano(nombre,edad,documento)
    persona.getNombre()
    persona.getEdad ()
    persona.getDocumento ()
    print(f'Nombre: {persona.getNombre()} - Edad: {persona.getEdad()} - C.C {persona.getDocumentoV()}')
    print(persona.getMayor())
if __name__=='__main__':
    main()
