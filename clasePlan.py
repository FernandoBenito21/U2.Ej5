class PlanAhorro:
    __cod = ''
    __modelo = ''
    __version = ''
    __valor = ''
    __cuotas = 60
    __CantCuotasMin = 10
    def __init__(self, cod, modelo, version, importe):
        self.__cod = int(cod)
        self.__modelo = modelo
        self.__version = version
        self.__valor = float(importe)
    def __str__ (self):
        return "%s %s %s" %(self.__cod,self.__modelo,self.__version)
    def getValor(self):
        return (self.__valor)
    def getCuotas(self):
        return(self.__cuotas)
    def getCod(self):
        return(self.__cod)
    def getModelo(self):
        return(self.__modelo)
    def actualizaValor(self,importe):
        self.__valor = importe
    @classmethod
    def getCantCuotas(cls):
        return (cls.__CantCuotasMin)
    @classmethod
    def getCuotas(cls):
        return (cls.__cuotas)
    @classmethod
    def modificaCantCuotas(cls,CuotasLicitas):
        cls.__CantCuotasMin = CuotasLicitas