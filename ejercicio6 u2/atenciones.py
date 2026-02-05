class atencion:
    __dni:int
    __fecha:str
    __importe:float
    def __init__(self,xdni,xfec,ximp):
        self.__dni=xdni
        self.__fecha=xfec
        self.__importe=ximp
    def getDni(self):
        return self.__dni
    def getFecha(self):
        return self.__fecha
    def getImporte(self):
        return self.__importe
    def __str__(self):
        return f'DNI {self.__dni}, FECHA {self.__fecha}, IMPORTE ${self.__importe}'
    
