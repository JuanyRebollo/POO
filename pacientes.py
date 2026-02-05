class paciente:
    __dni:int
    __nombre:str
    __unidad:str
    def __init__(self,xdni,xnom,xuni):
        self.__dni=xdni
        self.__nombre=xnom
        self.__unidad=xuni
    def getDni(self):
        return self.__dni
    def getNombre(self):
        return self.__nombre
    def getUnidad(self):
        return self.__unidad
    def __str__(self):
        return f'DNI {self.__dni}, NOMBRE {self.__nombre}, UNIDAD ${self.__unidad}'
    def __lt__(self,otro):
        return self.getNombre()< otro.getNombre()